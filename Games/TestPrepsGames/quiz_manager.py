import psycopg2
import random

class QuizManager:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor()
        self.questions = self.load_questions()
        self.total_questions = len(self.questions)
        self.current_index = 0
        self.score = 0
        self.mode = "multiple_choice"

    def load_questions(self):
        self.cursor.execute("""
            SELECT country, capital, image_path, direction
            FROM geography_maps
        """)
        rows = self.cursor.fetchall()
        random.shuffle(rows)
        return rows

    def get_next_question(self):
        if self.current_index < self.total_questions:
            row = self.questions[self.current_index]
            self.current_index += 1
            return row  # country, capital, image_path, direction
        return None

    def check_answer(self, user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.lower()

    def get_choices(self, correct_answer, direction):
        # Pull distractors from DB
        column = "capital" if direction == "country_to_capital" else "country"
        self.cursor.execute(f"SELECT DISTINCT {column} FROM geography_maps WHERE {column} != %s", (correct_answer,))
        pool = [row[0] for row in self.cursor.fetchall()]
        choices = random.sample(pool, 3)
        choices.append(correct_answer)
        random.shuffle(choices)
        return choices

    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode