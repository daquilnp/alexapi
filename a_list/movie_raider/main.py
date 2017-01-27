from flask import Flask
from flask_ask import Ask, statement, question, session
from word_to_numbers import convert_numbers
from omdb_api_comm import *
# from movie_api_comm import *
import sys
import logging
import imdb
import json


MOVIE_NOT_FOUND_MESSAGE = "The movie requested could not be found"

logging.basicConfig()


logger = logging.getLogger()
logger.setLevel(logging.INFO)


app = Flask(__name__)
ask = Ask(app, "/")

def validate_rating_movie_entities(m):
	title = get_m_title(m)
	logger.info("movie received was {0}".format(title))
	votes = get_m_votes(m)
	year = get_m_year(m)
	rating = get_m_rating(m)
	return [votes, title, year, rating]

@ask.launch

def new_game():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)


@ask.intent("RatingIntent")

def rating_answer(movie_to_query):

	m = get_movie(movie_to_query)
	if not m:
		result_string = MOVIE_NOT_FOUND_MESSAGE
	else:
		m_entities = validate_rating_movie_entities(m)
		if (m_entities[3] == -1):
			result_string = "Could not find a movie rating for {0} from {1}".format(m_entities[1], m_entities[2])
		else:
		
			result_string = 'Based on {0} votes, the current I m d b, movie rating for {1} from {2} is {3} on ten'.format(
																											 m_entities[0],
																											 m_entities[1], 
																											 m_entities[2],
																											 m_entities[3])

	return statement(result_string)
@ask.intent("YearwithRatingIntent")

def rating_with_year_answer(movie_to_query, movie_year):
	m = get_movie(movie_to_query, movie_year)
	if not m:
		result_string = MOVIE_NOT_FOUND_MESSAGE
	else:
		m_entities = validate_rating_movie_entities(m)
		if (m_entities[3] == -1):
			result_string = "Could not find a movie rating for {0} from {1}".format(m_entities[1], movie_year)
		else:
		
			result_string = 'Based on {0} votes, the current I m d b, movie rating for {1} from {2} is {3} on ten'.format(
																											 m_entities[0],
																											 m_entities[1], 
																											 m_entities[2],
																											 m_entities[3])

	return statement(result_string)


@ask.intent("CastingIntent")

def cast_answer(movie_to_query):

	m = get_movie(movie_to_query)
	if not m:
		result_string = MOVIE_NOT_FOUND_MESSAGE
	else:
		cast_result = get_m_cast(m)
		if not cast_result:
			result_string = "Could not find cast for requested movie"
		else:
			result_string = "The main actors in " + get_m_title(m) + " from " + get_m_year(m) + " are " + cast_result			

	return statement(result_string)
if __name__ == '__main__':

    app.run(debug=True)