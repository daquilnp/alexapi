import omdb
import json
import logging
import traceback
import sys
from word_to_numbers import convert_numbers
logging.basicConfig()


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_movie(movie_to_query, movie_year = ""):
	try:
		logger.info("GOING TO OMDb")

		# Search for a movie (get a list of Movie objects).
		movie_to_query = convert_numbers(movie_to_query)
		logger.info("movie received was {0}".format(movie_to_query))
		if not movie_to_query:
			return 0		
		# if not movie_year:
		
		res = omdb.request(t=movie_to_query[0], y=movie_year)
		m = json.loads(res.content)
		logger.info(m)

		return m
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
		logger.info("ERROR IS HERE")
		logger.info(''.join('!! ' + line for line in lines))
		return 0

def get_m_title(m):
	try:
		title = m["Title"]
	except:
		title = ""
	return title	

def get_m_year(m):
	try:
		year = m["Year"]
	except:
		year = ""
	return year

def get_m_votes(m):
	try:
		votes = m["imdbVotes"]
	except:
		votes = "an unknown amount of"
	return votes

def get_m_rating(m):
	try:
		rating = m["imdbRating"]
	except:
		rating = -1
	return rating

def get_m_cast(m):
	try:
		m_cast = m["Actors"]
		m_cast_seperate = m_cast.split(",")
		cast_range = len(m_cast_seperate)
		cast_result = ""
		for i in range(cast_range):
			actor = m_cast_seperate[i]
			if (i == (cast_range - 1)):
				cast_result = cast_result + " and" + actor
			else:
				cast_result = cast_result + actor + ","
		return cast_result
	except:
		return ""






