from survey import AnonymousSurvey

#Define a question, and build an object represent for anonymous survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#Show question and store responses
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = raw_input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Show survey result
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
