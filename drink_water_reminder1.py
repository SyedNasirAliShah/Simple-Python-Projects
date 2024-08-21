import time
from win32com.client import Dispatch
import winsound

speak = Dispatch("SAPI.SpVoice").speak
while True:
    time.sleep(5)
    for i in range(2):
        winsound.Beep(4000, 1200)
        speak(f"DRINK WATER REMINDER")