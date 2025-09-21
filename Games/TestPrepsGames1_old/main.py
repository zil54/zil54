from Games.TestPrepsGames.quiz_manager import QuizManager
from Games.TestPrepsGames.quiz_ui import QuizUI
import tkinter as tk

if __name__ == "__main__":
    country_capitals = {
        "Guatemala": "Guatemala City",
        "Belize": "Belmopan",
        "El Salvador": "San Salvador",
        "Honduras": "Tegucigalpa",
        "Nicaragua": "Managua",
        "Costa Rica": "San Jose",
        "Panama": "Panama City",
        "Colombia": "Bogota",
        "Venezuela": "Caracas",
        "Ecuador": "Quito",
        "Peru": "Lima",
        "Bolivia": "La Paz",  # School convention
        "Paraguay": "Asuncion",
        "Chile": "Santiago",
        "Argentina": "Buenos Aires",
        "Uruguay": "Montevideo",
        "Brazil": "Brasilia",
        "Guyana": "Georgetown",
        "Suriname": "Paramaribo",
        "French Guiana": "Cayenne",
    }

    root = tk.Tk()
    quiz_manager = QuizManager(country_capitals)
    quiz_ui = QuizUI(root, quiz_manager)
    root.mainloop()