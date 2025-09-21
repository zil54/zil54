from Games.TestPrepsGames.quiz_manager import QuizManager
from Games.TestPrepsGames.quiz_ui import QuizUI
import tkinter as tk

if __name__ == "__main__":
    # PostgreSQL connection config
    db_config = {
        "dbname": "learning_platform",
        "user": "postgres",
        "password": "YUG0slavia",
        "host": "localhost",
        "port": 5432
    }

    root = tk.Tk()
    quiz_manager = QuizManager(db_config)
    quiz_manager.set_mode("text")
    quiz_ui = QuizUI(root, quiz_manager)
    root.mainloop()