from __future__ import print_function

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GradePercentageIntent":
        return get_percentage_grade(intent, session)
    if intent_name == "GradePassIntent":
        return get_pass_grade(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Exam Grade Estimator. " \
                    "Here you can determine how much you need to get in the exam to get your target mark " \
                    "in the course. Just ask, I am going into the exam with a 78 percent, what do I need on the 40 percent exam " \
                    "to get 82 percent in the course. Or, if you are the watch movies through exam type, just ask, " \
                    "I am going into the exam with a 65 percent, what do I need in order to pass the course"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Tell me the mark you want in the course " \
    "and  I will guess the grade you need on your exam based on the grade you have going into it."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using the exam grade estimator. " \
                    "Good luck on your exams! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_percentage_grade(intent, session):

    card_title = intent['name']
    session_attributes = {}
    should_end_session = True

    if 'current_grade' in intent['slots'] and 'exam_percentage' in intent['slots'] and 'desired_grade' in intent['slots']:
        if 'value' in intent['slots']['current_grade'] and 'value' in intent['slots']['exam_percentage'] and 'value' in intent['slots']['desired_grade']:

            current_grade = int(intent['slots']['current_grade']['value'])
            exam_percentage = int(intent['slots']['exam_percentage']['value'])
            desired_grade = int(intent['slots']['desired_grade']['value'])


            so_far_grade = float(current_grade)*(1 - exam_percentage/100.0)
            needed_exam_grade = float((desired_grade - so_far_grade))/exam_percentage
            percent_needed = str(needed_exam_grade*100)
            if (needed_exam_grade < 0):
                percent_needed = "literally below 0"


            speech_output = "In order to get " + str(desired_grade) + " percent in the course, " \
            "you need to get " + percent_needed + " percent on the exam." 

                            
            reprompt_text = "Tell me the mark you want in the course " \
            "and  I will guess the grade you need on your exam based on the grade you have going into it."


        else:
            speech_output = "Your command is incomplete. Please try again or ask for help."
            reprompt_text = "Your command is incomplete. Please try again or ask for help."
    else:
        speech_output = "I'm not sure what your question was. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your question was. " \
                        "Please try again."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_pass_grade(intent, session):

    card_title = intent['name']
    session_attributes = {}
    should_end_session = True

    if 'current_grade' in intent['slots'] and 'exam_percentage' in intent['slots']:
        if 'value' in intent['slots']['current_grade'] and 'value' in intent['slots']['exam_percentage']:

            current_grade = int(intent['slots']['current_grade']['value'])
            exam_percentage = int(intent['slots']['exam_percentage']['value'])
            desired_grade = 50


            so_far_grade = float(current_grade)*(1 - exam_percentage/100.0)
            needed_exam_grade = float((desired_grade - so_far_grade))/exam_percentage
            percent_needed = str(needed_exam_grade*100)
            if (needed_exam_grade < 0):
                percent_needed = "literally below 0"


            speech_output = "In order to pass the course, " \
            "you need to get " + percent_needed + " percent on the exam." 

                            
            reprompt_text = "Tell me the mark you want in the course " \
            "and  I will guess the grade you need on your exam based on the grade you have going into it."


        else:
            speech_output = "Your command is incomplete. Please try again or ask for help."
            reprompt_text = "Your command is incomplete. Please try again or ask for help."
    else:
        speech_output = "I'm not sure what your question was. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your question was. " \
                        "Please try again."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }