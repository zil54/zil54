"""The binary search algorithm has a time complexity of O(log n).
Why?
- Binary search works by repeatedly dividing the search space in half.
- In each iteration, it eliminates half of the remaining elements, making it logarithmic in complexity.
- This results in an efficient search, especially compared to O(n) linear search, which checks each element one by one.
Breakdown:
- Start with n elements.
- After the first comparison, you have n/2 elements left.
- After the second comparison, n/4 remain.
- This continues until you reach a single element.
Mathematically, the number of comparisons needed is log₂(n), leading to O(log n) complexity."""

import tkinter as tk
import logging
from algorithm_visualizer import AlgorithmVisualizer


class BinarySearchVisualizer(AlgorithmVisualizer):
    """Concrete implementation of binary search visualization."""

    def get_title(self):
        return "Binary Search Visualization"

    def start_visualization(self):
        """Start binary search animation with logging."""
        try:
            target = int(self.entry.get())
            logging.info("Starting binary search for target: %d", target)

            left, right = 0, len(self.data) - 1

            # Reset button colors
            for btn in self.buttons:
                btn.config(bg="light blue")

            self.animate_search(left, right, target)
        except ValueError:
            logging.error("Invalid input: Please enter a number.")
            self.label.config(text="Enter a valid number!", fg="red")

    def animate_search(self, left, right, target):
        """Recursive animation for binary search steps."""
        if left > right:
            logging.warning("Target %d not found!", target)
            for btn in self.buttons:
                btn.config(bg="red")
            return

        mid = (left + right) // 2
        logging.debug("Checking middle index %d: %d", mid, self.data[mid])
        self.buttons[mid].config(bg="yellow")  # Highlight midpoint
        self.root.after(500, self.process_step, mid, left, right, target)

    def process_step(self, mid, left, right, target):
        """Continue binary search based on comparison."""
        if self.data[mid] == target:
            logging.info("Target %d found at index %d", target, mid)
            self.buttons[mid].config(bg="light green")  # Target found
            return
        elif self.data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

        # Gray out ignored elements
        for i in range(len(self.data)):
            if i < left or i > right:
                self.buttons[i].config(bg="gray")

        logging.debug("New search range: left=%d, right=%d", left, right)
        self.root.after(500, self.animate_search, left, right, target)


# Tkinter setup
root = tk.Tk()
root.title("Binary Search Animation with Logging")
app = BinarySearchVisualizer(root, [3, 1, 4, 5, 9, 2])
root.mainloop()

class BinarySearch:
    def __init__(self, data):
        """Initialize with a sorted list to ensure binary search works properly."""
        self.data = sorted(data)

    def search(self, target):
        """Perform binary search to locate the target value."""
        left_index = 0
        right_index = len(self.data) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            mid_value = self.data[mid_index]  # Store the middle value for clarity

            if mid_value == target:
                return mid_index  # Target found, return index
            elif mid_value < target:
                left_index = mid_index + 1  # Move search to the right half
            else:
                right_index = mid_index - 1  # Move search to the left half

        return -1  # Target not found


# Example usage
data = [3, 1, 4, 5, 9, 2]
bs = BinarySearch(data)
result = bs.search(4)
print(f"Index of target: {result}")