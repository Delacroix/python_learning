class AnonymousSurvey():
    """Collecting anonymous survey"""

    def __init__(self, question):
        """Storing a question, and ready for responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show survey"""
        print(self.question)

    def store_response(self, new_response):
        """Storing a single survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all survey that collected"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)