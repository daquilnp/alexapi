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

HELP_MESSAGE = 'Welcome to Movie Raider. This app can currently tell you the i m d b, rating of a movie as well' \
    	' as the cast of a movie. To ask for the rating of a movie, say "Alexa, ask movie raider the rating for the incredibles".' \
    	' To ask for the cast of a movie, say "Alexa, ask movie raider the cast of snow dogs". If the movie stats given are not for' \
    	' the movie you wanted, try again and add the year of the movie at the end. Just say "Alexa, ask movie raider the rating for' \
    	' taken created in 2008". It should be noted that if numbers are included in the movie name the app will have a more difficult time' \
    	' finding it. However, sequels to movies such as Iron Man 2 or Iron Man 3 will work perfect. Likewise, movies such as 300 or 101 dalmatians' \
    	' will also return a correct result.'

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

    welcome_msg = render_template(HELP_MESSAGE)

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
		
			result_string = '{2} on ten is the current I m d b, movie rating for {0} from {1}'.format(		 m_entities[1], 
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
		
			result_string = '{2} on ten is the current I m d b, movie rating for {0} from {1}'.format(		 m_entities[1], 
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

@ask.intent("AMAZON.StopIntent")
def stop():
	return statement("Stopping. Thank you for using movie raider!")

@ask.intent("AMAZON.CancelIntent")
def cancel():
	return statement("Cancelled. Thank you for using movie raider!")

@ask.intent("AMAZON.HelpIntent")
def help():
	return statement(HELP_MESSAGE)

@ask.session_ended

def end_of_session():
	logger.info("Session Ended")
	return "", 200

if __name__ == '__main__':

    app.run(debug=True)





