import tkinter as tk
from PIL import Image, ImageTk

class QuizUI:
    def __init__(self, root, quiz_manager):
        self.root = root
        self.quiz = quiz_manager
        self.time_limit = 30
        self.time_left = self.time_limit
        self.timer_id = None
        self.correct_answer = ""
        self.choice_buttons = []

        self.setup_ui()
        self.next_question()

    def setup_ui(self):
        self.root.title("Geography Quiz")

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.question_label = tk.Label(self.root, font=("Arial", 16))
        self.question_label.pack(pady=10)

        self.choices_frame = tk.Frame(self.root)
        self.choices_frame.pack()

        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.submit_button = tk.Button(self.root, text="Submit", font=("Arial", 12),
                                       command=self.check_answer)

        self.feedback_label = tk.Label(self.root, font=("Arial", 12))
        self.feedback_label.pack()

        self.score_label = tk.Label(self.root, font=("Arial", 12))
        self.score_label.pack()

        self.timer_label = tk.Label(self.root, font=("Arial", 12), fg="blue")
        self.timer_label.pack()

    def show_image(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((300, 200))
            self.tk_image = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_image)
        except Exception as e:
            self.image_label.config(text="Image not found", image="")

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

        for btn in self.choice_buttons:
            btn.destroy()
        self.choice_buttons.clear()
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()

        question = self.quiz.get_next_question()
        if not question:
            self.end_quiz()
            return

        country, capital, image_path, direction = question
        self.correct_answer = capital if direction == "country_to_capital" else country

        self.question_label.config(
            text=f"What is the capital of {country}?" if direction == "country_to_capital"
                 else f"{capital} is the capital of which country?"
        )

        self.show_image(image_path)
        self.feedback_label.config(text="")

        if self.quiz.get_mode() == "multiple_choice":
            choices = self.quiz.get_choices(self.correct_answer, direction)
            for choice in choices:
                btn = tk.Button(self.choices_frame, text=choice, font=("Arial", 12),
                                command=lambda c=choice: self.check_answer(c))
                btn.pack(pady=5)
                self.choice_buttons.append(btn)
        else:
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.pack()
            self.submit_button.pack()

        self.start_timer()

    def check_answer(self, selected_choice=None):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        user_answer = selected_choice if selected_choice else self.answer_entry.get()
        correct = self.quiz.check_answer(user_answer, self.correct_answer)

        if correct:
            self.quiz.score += 1
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
        self.timer_label.config(text="")
        for btn in self.choice_buttons:
            btn.config(state=tk.DISABLED)
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()