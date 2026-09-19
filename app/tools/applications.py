# lets Python start programs on your computer
import subprocess


APPLICATIONS = {
    "notepad": "notepad.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode": "code",
}


def open_application(application):
    application = application.lower()

    if application not in APPLICATIONS:
        return f"I don't know how to open {application}."

    try:
        subprocess.Popen(APPLICATIONS[application])
        return f"Opening {application}."

    except FileNotFoundError:
        return f"{application} is not installed or I can't find it."