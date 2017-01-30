from flask import Flask
from flask_ask import Ask, statement, question, session
import sys
import logging
import json


INVALID_INPUT = "The Alexa phrase was not said correctly. Invalid values were detected. " \
                "Any values you have successfully added before this are still valid. Please try the last " \
                "phrase again."

HELP_MESSAGE = '"with the info provided such as, what if I wanted a, (insert new desired grade), percent in the course."'

IN_LIST_MODE_MESSAGE = "You are currently in list mode. Please say stop to restart app in regular mode."
logging.basicConfig()


logger = logging.getLogger()
logger.setLevel(logging.INFO)


app = Flask(__name__)
ask = Ask(app, "/")

def is_inputs_valid(input_set):
    try:
        for x in input_set:
            if x is None or x == "?":
                return False
        return True
    except:
        return False
def is_in_list_mode():
    return 'assessment_list' in session.attributes

def get_percent_needed(current_grade, desired_grade, exam_percentage):
    so_far_grade = current_grade*(1 - exam_percentage/100.0)
    needed_exam_grade = (1.0*(desired_grade - so_far_grade))/exam_percentage
    percent_needed = str(needed_exam_grade*100)
    if (needed_exam_grade < 0):
        percent_needed = "literally below 0"
    return percent_needed

@ask.launch

def launch():

    welcome_msg = render_template(HELP_MESSAGE)

    return question(welcome_msg)


@ask.intent("CurrentGradeIntent", convert={'current_grade' : int, 'desired_grade' : int})

def get_current_grade(current_grade, desired_grade):
    if not is_inputs_valid([current_grade, desired_grade]):
        return question(INVALID_INPUT)
    if is_in_list_mode():
        return question(IN_LIST_MODE_MESSAGE)
    elif 'current_grade' not in session.attributes or 'desired_grade' not in session.attributes:
        session.attributes['current_grade'] = current_grade
        session.attributes['desired_grade'] = desired_grade
        result_string = "How much is the exam worth in percentage?"
    else:
        result_string = "you already have a current grade and desired grade in this session. Please tell me " \
                        "how much the exam is worth."
    return question(result_string)

@ask.intent("ExamPercentIntent", convert={'exam_percent' : int})

def exam_grade_calculator(exam_percent):
    if not is_inputs_valid([exam_percent]):
            return question(INVALID_INPUT)
    if is_in_list_mode():
        return question(IN_LIST_MODE_MESSAGE)
    elif 'current_grade' not in session.attributes or 'desired_grade' not in session.attributes:

        result_string = "Please tell me your current grade and desired grade first by saying, I am going into " \
                        "the exam with a, (insert current grade), percent and I want a, (insert desired grade), percent in the course"
        return question(result_string)
    elif session.attributes['current_grade'] is None or \
        session.attributes['desired_grade'] is None:
            result_string = "There was an error during calculation. A numeric value was not acquired correctly " \
                            "Please try again."
            return statement(result_string)
    else:
        current_grade = session.attributes['current_grade']
        session.attributes['exam_percent'] = exam_percent
        desired_grade = session.attributes['desired_grade']

        percent_needed = get_percent_needed(current_grade, desired_grade, exam_percent)

        result_string = "In order to get " + str(desired_grade) + " percent in the course, " \
        "you need to get " + percent_needed + " percent on the exam. Now you can ask me more questions or say stop."

	return question(result_string)

@ask.intent("WhatIfIntent", convert={'new_desired_grade' : int})

def what_if(new_desired_grade):
    if not is_inputs_valid([new_desired_grade]):
            return question(INVALID_INPUT)
    elif 'current_grade' not in session.attributes or 'desired_grade' not in session.attributes \
         or 'exam_percent' not in session.attributes:

        result_string = "Please only use the what if phrase after you have specified a previous current grade and exam percentage. " \
        "Say Help for more detail."
        return question(result_string)
    elif session.attributes['current_grade'] is None or \
        session.attributes['desired_grade'] is None:
            result_string = "There was an error during calculation. A numeric value was not acquired correctly " \
                            "Please try again."
            return statement(result_string)
    else:
        current_grade = session.attributes['current_grade']
        exam_percent = session.attributes['exam_percent']
        session.attributes['desired_grade'] = new_desired_grade

        percent_needed = get_percent_needed(current_grade, new_desired_grade, exam_percent)

        result_string = "In order to get " + str(new_desired_grade) + " percent in the course, " \
        "you need to get " + percent_needed + " percent on the exam. You can ask me more questions or say stop."

	return question(result_string)
@ask.intent("StartListIntent")
def start_list():
    if is_in_list_mode():
        session.attributes['assessment_list'] = []
        return question("Restarted list mode. Insert your first assessment grade and worth in percentage.")
    session.attributes['assessment_list'] = []
    return question("List mode started. To add an item say, I got, (insert assessment grade) on an assessment worth, " \
    "(insert assessment percent). When you have said your last assessment, respond with Done.")


@ask.intent("ListGradesIntent", convert={'assessment_percentage' : int, 'assessment_grade' : int})
def list_grades(assessment_percentage, assessment_grade):
    if not is_inputs_valid([assessment_percentage, assessment_grade]):
            return question(INVALID_INPUT)
    else:
        if "assessment_list" not in session.attributes:
            session.attributes['assessment_list'] = []
        session.attributes['assessment_list'].append([assessment_percentage, assessment_grade])
        size = len(session.attributes['assessment_list']) + 1
    return question("and?")

@ask.intent("DoneListIntent")
def done_list():
    if not is_in_list_mode():
        return question("Please start the list mode first.")
    elif len(session.attributes['assessment_list']) == 0:
        return question("Please add assessments to the list mode first.")
    return question("Please state what you want in the course and how much the exam is worth.")

@ask.intent("CalculateListIntent", convert={'desired_grade' : int})
def calculate_list(desired_grade):
    if not is_inputs_valid([desired_grade]):
            return question(INVALID_INPUT)
    if not is_in_list_mode():
        return question("Please start the list mode first.")
    elif len(session.attributes['assessment_list']) == 0:
        return question("Please add assessments to the list mode first.")
    else:
        current_grade = 0
        current_percentage = 0
        for x in session.attributes['assessment_list']:
            current_grade += x[1] * x[0]*0.01
            current_percentage += x[0]
        logger.info("current grade: " + str(current_grade))
        exam_percent = 100 - current_percentage
        session.attributes['current_grade'] = current_grade
        session.attributes['exam_percent'] = exam_percent
        session.attributes['desired_grade'] = desired_grade

        percent_needed = get_percent_needed(current_grade, desired_grade, exam_percent)

        result_string = "In order to get " + str(desired_grade) + " percent in the course, " \
        "you need to get " + percent_needed + " percent on the exam. Now you can ask me more questions, input a new list or say stop."
        session.attributes['assessment_list'] = []
        return question(result_string)

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
