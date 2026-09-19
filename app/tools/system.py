import psutil
from datetime import datetime


def get_current_time():
    current_time = datetime.now().strftime("%I:%M %p")

    return f"The current time is {current_time}."


def get_battery_status():
    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information is unavailable."

    percentage = battery.percent

    if battery.power_plugged:
        return f"Battery is at {percentage}% and the laptop is plugged in."

    return f"Battery is at {percentage}% and the laptop is running on battery."