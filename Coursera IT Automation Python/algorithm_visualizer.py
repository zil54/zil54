import tkinter as tk
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.DEBUG  # Adjust logging level as needed
)


class AlgorithmVisualizer(ABC):
    """Abstract base class for algorithm visualizations."""

    def __init__(self, root, data):
        """Initialize common properties for visualization."""
        self.root = root
        self.data = data
        self.buttons = []  # Store buttons representing values
        logging.info("AlgorithmVisualizer initialized with data: %s", self.data)
        self.create_ui()

    def create_ui(self):
        """Setup UI components. Can be customized by subclasses."""
        logging.info("Creating UI for visualization.")

        self.label = tk.Label(self.root, text=self.get_title(), font=("Arial", 14))
        self.label.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for num in self.data:
            btn = tk.Button(self.frame, text=str(num), width=5, font=("Arial", 12), bg="light blue")
            btn.pack(side="left", padx=5)
            self.buttons.append(btn)

        self.entry = tk.Entry(self.root, width=10, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.start_btn = tk.Button(self.root, text="Start", command=self.start_visualization, font=("Arial", 12))
        self.start_btn.pack()

        logging.info("UI setup complete.")

    @abstractmethod
    def start_visualization(self):
        """Abstract method for algorithm execution."""
        pass

    @abstractmethod
    def get_title(self):
        """Abstract method for setting visualization title."""
        pass