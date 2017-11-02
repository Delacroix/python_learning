class AnonymousSurvey():
    """Collecting anonymous survey"""
    def __init__(self, question):
        """Storing a question, and ready for response"""
        self.question = question
        self.responses = []

    def show_questions(self):
        """Show survey"""
        print(question)