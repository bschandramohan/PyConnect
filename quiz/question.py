class QuestionData:
    def __init__(self, question_data, answer_data):
        self.question = question_data
        self.answer = answer_data

    def print(self):
        print("Question:" + self.question)
        print("Answer:" + self.answer)
