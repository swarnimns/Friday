import pyautogui
from datetime import datetime
from pathlib import Path


def take_screenshot():
    screenshot_folder = Path("screenshots")
    screenshot_folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = screenshot_folder / f"screenshot_{timestamp}.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

    return f"Screenshot saved to {screenshot_path}"