import tkinter as tk
import sys


"""
Both print() and sys.stdout.write() deal with standard output (STDOUT), but they have key differences in functionality and flexibility.
print() vs. sys.stdout.write()
| Feature | print() | sys.stdout.write() | 
| Automatic Formatting | Adds a newline (\n) automatically | Does not add a newline | 
| Data Handling | Converts non-string types automatically | Requires explicit string conversion | 
| Flexibility | Simpler for quick output | More control for logging, redirection, and handling byte streams | 
| Buffering | Uses built-in output buffering | Works directly with sys.stdout, allowing manual buffer flushing |
When to Use sys.stdout.write()?
- Redirecting output to a file or another process (sys.stdout = open('log.txt', 'w')).
- More precise control over output formatting (avoiding unwanted newlines).
- Logging data efficiently, ensuring it stays unbuffered
 
"""

class TimeConverterCLI:
    def __init__(self):
        print("Welcome to this time converter")
        self.run_converter()

    def to_seconds(self, hours, minutes, seconds):
        return hours * 3600 + minutes * 60 + seconds

    def __init__(self):
        print("Welcome to this time converter")
        self.run_converter()

    def to_seconds(self, hours, minutes, seconds):
        """Convert time components into total seconds."""
        return hours * 3600 + minutes * 60 + seconds

    def run_converter(self):
        while True:
            try:
                hours = int(input("Enter the number of hours: "))
                minutes = int(input("Enter the number of minutes: "))
                seconds = int(input("Enter the number of seconds: "))

                total_seconds = self.to_seconds(hours, minutes, seconds)

                # Print result to console
                result_message = f"That's {total_seconds} seconds.\n"
                print(result_message)

                # Write result to STDOUT
                sys.stdout.write(result_message)

            except ValueError:
                error_message = "Please enter valid integers!\n"
                print(error_message)
                sys.stdout.write(error_message)

            while True:  # Loop until valid input (Y/N)
                cont = input("Do you want to do another conversion? [Y/N]: ").strip().upper()
                if cont in ["Y", "N"]:
                    break
                else:
                    error_message = "Invalid selection! Please enter 'Y' to continue or 'N' to quit.\n"
                    print(error_message)
                    sys.stdout.write(error_message)

            if cont == "N":
                goodbye_message = "Goodbye!\n"
                print(goodbye_message)
                sys.stdout.write(goodbye_message)
                sys.exit()  # ⬅️ Proper exit


class TimeConverterGUI:
    """GUI-based time converter with colors and re-run functionality."""

    def __init__(self, root):
        self.root = root
        self.root.title("Time Converter")
        self.root.configure(bg="#2B2D42")  # Dark background theme

        # Labels and entry fields
        tk.Label(root, text="Enter Hours:", fg="white", bg="#420420").grid(row=0, column=0)
        self.hours_entry = tk.Entry(root, bg="#8D99AE", fg="white")
        self.hours_entry.grid(row=0, column=1)

        tk.Label(root, text="Enter Minutes:", fg="white", bg="#420420").grid(row=1, column=0)
        self.minutes_entry = tk.Entry(root, bg="#8D99AE", fg="white")
        self.minutes_entry.grid(row=1, column=1)

        tk.Label(root, text="Enter Seconds:", fg="white", bg="#420420").grid(row=2, column=0)
        self.seconds_entry = tk.Entry(root, bg="#8D99AE", fg="white")
        self.seconds_entry.grid(row=2, column=1)

        # Convert button
        tk.Button(root, text="Convert", command=self.convert_time, bg="#420420", fg="white").grid(row=3, columnspan=2)

        # Result display
        self.result_label = tk.Label(root, text="", fg="black", bg="#cce5cc", font=("Arial", 12, "bold"), width=30)
        self.result_label.grid(row=4, columnspan=2, pady=10)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_fields, bg="#420420", fg="white",
                                      state=tk.DISABLED)
        self.reset_button.grid(row=5, columnspan=2)

        # Quit button to exit UI
        tk.Button(root, text="Quit", command=root.quit, bg="black", fg="white", font=("Arial", 16, "bold")).grid(row=6,
                                                                                                                 columnspan=2,
                                                                                                                 pady=10)


    def to_seconds(self, hours, minutes, seconds):
        """Convert time to total seconds."""
        return hours * 3600 + minutes * 60 + seconds

    def convert_time(self):
        """Retrieve input values, convert to seconds, and display the result."""
        try:
            hours = int(self.hours_entry.get())
            minutes = int(self.minutes_entry.get())
            seconds = int(self.seconds_entry.get())

            total_seconds = self.to_seconds(hours, minutes, seconds)
            self.result_label.config(text=f"That's {total_seconds} seconds!", fg="white", bg="#8D99AE")
            self.reset_button.config(state=tk.NORMAL)  # Enable reset button
        except ValueError:
            self.result_label.config(text="Please enter valid integers!", fg="white", bg="red")

    def reset_fields(self):
        """Clear all input fields and reset the UI."""
        self.hours_entry.delete(0, tk.END)
        self.minutes_entry.delete(0, tk.END)
        self.seconds_entry.delete(0, tk.END)
        self.result_label.config(text="", bg="#EDF2F4")
        self.reset_button.config(state=tk.DISABLED)  # Disable reset but


class ConverterApplication:
    """Handles conversion method selection based on user preference."""

    def __init__(self, mode="CLI"):
        self.mode = mode

    def run(self):
        if self.mode.upper() == "CLI":
            converter = TimeConverterCLI()
            converter.run_converter()
        elif self.mode.upper() == "GUI":
            root = tk.Tk()
            converter = TimeConverterGUI(root)
            root.mainloop()  # Directly start the Tkinter event loop
        else:
            print("Invalid mode selected! Choose 'CLI' or 'GUI'.")



# User selects mode
if __name__ == "__main__":
    mode = input("Enter mode (CLI or GUI): ")
    app = ConverterApplication(mode)
    app.run()



