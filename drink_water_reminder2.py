import time
from plyer import notification
import winsound

def remind_water():
    notification.notify(
        title="Hydration Reminder",
        message="It's time to drink water! Stay hydrated for your health.",
        timeout=10  # Notification will stay on screen for 10 seconds
    )
    # Play a simple system sound
    winsound.MessageBeep(winsound.MB_OK)

if __name__ == "__main__":
    while True:
        remind_water()
        time.sleep(5)  
