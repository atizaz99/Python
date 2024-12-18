
from datetime import datetime
import winsound

def get_current_time():
    """Returns the current time in hours, minutes, and seconds."""
    return datetime.now().strftime("%I:%M:%S %p")

def get_formatted_time(hours, minutes, period):
    """Formats the input time values into a proper 12-hour time format."""
    return f"{int(hours):02d}:{int(minutes):02d}:00 {period.upper()}"

def play_alarm_sound():
    """Plays an alarm sound when the set time is reached."""
    # Replace with a valid path to your alarm sound file.
    winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)
