import random

class QuizManager:
    def __init__(self, country_capitals):
        self.country_capitals = country_capitals
        self.questions = self.generate_questions()
        self.total_questions = len(self.questions)
        self.current_index = 0
        self.score = 0

    def generate_questions(self):
        questions = []
        for country, capital in self.country_capitals.items():
            questions.append(("country_to_capital", country, capital))
            questions.append(("capital_to_country", country, capital))
        random.shuffle(questions)
        return questions

    def get_next_question(self):
        if self.current_index < self.total_questions:
            mode, country, capital = self.questions[self.current_index]
            self.current_index += 1
            return mode, country, capital
        return None

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.lower():
            self.score += 1
            return True
        return False