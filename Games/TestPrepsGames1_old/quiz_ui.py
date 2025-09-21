import tkinter as tk

class QuizUI:
    def __init__(self, root, quiz_manager):
        self.root = root
        self.quiz = quiz_manager
        self.time_limit = 30
        self.time_left = self.time_limit
        self.timer_id = None

        self.setup_ui()
        self.next_question()

    def setup_ui(self):
        self.root.title("Geography Quiz")
        self.question_label = tk.Label(self.root, font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(self.root, font=("Arial", 12))
        self.feedback_label.pack()

        self.score_label = tk.Label(self.root, font=("Arial", 12))
        self.score_label.pack()

        self.timer_label = tk.Label(self.root, font=("Arial", 12), fg="blue")
        self.timer_label.pack()

    def start_timer(self):
        self.time_left = self.time_limit
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.feedback_label.config(text=f"⏰ Time's up! Correct answer: {self.correct_answer}", fg="orange")
            self.update_score_display()
            self.root.after(1500, self.next_question)

    def next_question(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        question = self.quiz.get_next_question()
        if not question:
            self.end_quiz()
            return

        mode, country, capital = question
        if mode == "country_to_capital":
            self.question_label.config(text=f"What is the capital of {country}?")
            self.correct_answer = capital
        else:
            self.question_label.config(text=f"{capital} is the capital of which country?")
            self.correct_answer = country

        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.start_timer()

    def check_answer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        user_answer = self.answer_entry.get()
        correct = self.quiz.check_answer(user_answer, self.correct_answer)

        if correct:
            self.feedback_label.config(text="✅ Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"❌ Incorrect. The correct answer is {self.correct_answer}.", fg="red")

        self.update_score_display()
        self.root.after(1500, self.next_question)

    def update_score_display(self):
        total_answered = self.quiz.current_index
        percentage = round((self.quiz.score / total_answered) * 100, 1)
        self.score_label.config(text=f"Score: {self.quiz.score} / {total_answered} ({percentage}%)")

    def end_quiz(self):
        self.question_label.config(text="🎉 Quiz Complete!")
        self.feedback_label.config(text=f"Final Score: {self.quiz.score} / {self.quiz.total_questions}")
        self.submit_button.config(state=tk.DISABLED)
        self.answer_entry.config(state=tk.DISABLED)