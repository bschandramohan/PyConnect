class QuizGame:
    """Quiz Game"""
    TRIVIA_DB_OPEN_API_URL = "https://opentdb.com/api.php?amount=20&category=9&difficulty=easy&type=boolean"

    questions_data = []

    def __init__(self):
        self.print_logo()
        self.get_questions()

    @staticmethod
    def print_logo():
        from quiz.logo import logo
        print("Welcome to the ")
        print(logo)

    def get_questions(self):
        """Imports the questions from external webapp"""
        import requests
        response = requests.get(self.TRIVIA_DB_OPEN_API_URL)

        if response.status_code < 200 or response.status_code >= 300:
            print("Error initializing the game. Please try again later")

        # print(f"Results from response = {response.json()['results']}")

        for result in response.json()['results']:
            from quiz.question import QuestionData
            entry = QuestionData(result["question"], result["correct_answer"])
            self.questions_data.append(entry)

        # for question_data in self.questions_data:
        #     question_data.print()

    def play_game(self):
        """Play the game"""
        continue_game = True
        current_questions_count = 0
        correct_answers_count = 0

        import random
        while continue_game:
            current_question = random.choice(self.questions_data)
            current_questions_count += 1
            print(f"Q{current_questions_count}. {current_question.question}")
            if input("Enter True or False:") == current_question.answer:
                correct_answers_count += 1
                print("Correct")
            else:
                print("Incorrect")

            if current_questions_count == 20:
                continue_game = False
            elif input("Enter n to stop") == 'n':
                continue_game = False

        print(f"\nYou answered {correct_answers_count} correctly out of {current_questions_count}\n")
