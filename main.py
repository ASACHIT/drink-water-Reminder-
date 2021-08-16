import time

import pyttsx3
from win10toast import ToastNotifier

# A simple reminder that reminds the user to drink water at 30 minute intervals. 
# -----------------------------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)
# -----------------------------------------


def speak(message):
    engine.say(message)
    engine.runAndWait()


n = ToastNotifier()

if __name__ == "__main__":
    while True:
        speak("Drink Water Sachit")
        n.show_toast("Water Alarm", "Drink water Sachit !!",
                     duration=10, icon_path="C:\water_alarm\glass.ico")
        time.sleep(1800)
