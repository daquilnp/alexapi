import imdb
import json
from word_to_numbers import convert_numbers
def get_movie(movie_to_query, movie_year = ""):
	try:
		ia = imdb.IMDb() # by default access the web.

		# Search for a movie (get a list of Movie objects).
		if not movie_year:
			movie_to_query = convert_numbers(movie_to_query)
			if movie_to_query[1] == 0:
				return 0
			movie_to_query = "{0} {1}".format(movie_to_query[0], movie_year)
		s_result = ia.search_movie(movie_to_query)
		# Print the long imdb canonical title and movieID of the results.
		m = s_result[0]
		ia.update(m)
		return m
	except:
		return 0
	

def get_m_title(m):
	try:
		title = str(m["title"])
	except:
		title = ""
	return title	

def get_m_year(m):
	try:
		year = str(m["year"])
	except:
		year = ""
	return year

def get_m_votes(m):
	try:
		votes = str(m["votes"])
	except:
		votes = "an unknown amount of"
	return votes

def get_m_rating(m):
	try:
		rating = str(m["rating"])
	except:
		rating = -1
	return rating

def get_m_cast(m):
	try:
		m_cast = m["cast"]
		cast_range = 5
		if len(m_cast) < cast_range:
			cast_range = len(m_cast)
		cast_result = ""
		for i in range(cast_range):
			actor = m_cast[i]['name']
			if (i == (cast_range - 1)):
				cast_result = cast_result + "and " + actor
			else:
				cast_result = cast_result + actor + ", "
		return cast_result
	except:
		return ""






