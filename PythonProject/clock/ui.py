import tkinter as tk
from tkinter import messagebox
from utils import get_current_time, get_formatted_time, play_alarm_sound
import threading
import time

class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alarm Clock")
        self.geometry("400x300")
        self.configure(bg="lightblue")

        # Initialize alarm time and flag
        self.alarm_time = None
        self.alarm_set = False

        # Add the GUI components
        self.create_widgets()

        # Start updating the current time display
        self.update_current_time()

    def create_widgets(self):
        """Create and place widgets in the GUI."""
        # Current time display
        self.current_time_label = tk.Label(self, text="Current Time:", font=("Helvetica", 14), bg="lightblue")
        self.current_time_label.pack(pady=10)

        self.time_display = tk.Label(self, text="", font=("Helvetica", 18, "bold"), bg="lightblue")
        self.time_display.pack(pady=10)

        # Alarm time input fields
        self.hour_input = tk.Entry(self, width=5)
        self.hour_input.insert(0, "HH")
        self.hour_input.pack(pady=5)

        self.minute_input = tk.Entry(self, width=5)
        self.minute_input.insert(0, "MM")
        self.minute_input.pack(pady=5)

        self.period_input = tk.Entry(self, width=5)
        self.period_input.insert(0, "AM/PM")
        self.period_input.pack(pady=5)

        # Set alarm button
        self.set_alarm_button = tk.Button(self, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=5)

        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_program)
        self.exit_button.pack(pady=5)

    def update_current_time(self):
        """Continuously update and display the current time."""
        current_time = get_current_time()
        self.time_display.config(text=current_time)

        # Check if the alarm should go off
        if self.alarm_set and current_time == self.alarm_time:
            self.trigger_alarm()

        # Call this method again after 1000 milliseconds (1 second)
        self.after(1000, self.update_current_time)

    def set_alarm(self):
        """Set the alarm time based on user input and display a confirmation."""
        hours = self.hour_input.get()
        minutes = self.minute_input.get()
        period = self.period_input.get()

         # Validate and format the input time
        try:
            self.alarm_time = get_formatted_time(hours, minutes, period)
            self.alarm_set = True
            messagebox.showinfo("Alarm Set", f"Alarm set for {self.alarm_time}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid time.")

    def trigger_alarm(self):
        """Trigger the alarm by playing sound and showing a message."""
        self.alarm_set = False  # Reset the alarm flag
        threading.Thread(target=play_alarm_sound).start()  # Play sound in a separate thread
        messagebox.showinfo("Alarm", "Time to wake up!")

    def exit_program(self):
        """Exit the program gracefully."""
        self.destroy()
