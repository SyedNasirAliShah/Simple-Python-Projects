from plyer import notification
import winsound  # --> if we want to beep voice
from playsound import playsound
from gtts import gTTS
import time  # For sleep in while loop

def save_mp3_file(text, name):
    """
    Converts text to speech and saves it as an MP3 file.
    """
    try:
        tts = gTTS(text)
        tts.save(name)
    except Exception as e:
        print(f"Error in saving MP3 file: {e}")


def remind_water():
    """
    Sends a hydration reminder notification and plays an audio alert.
    """
    try:
        # Display a desktop notification
        notification.notify(
            title="Hydration Reminder",
            message="It's time to drink water",
            timeout=10
        )
        
        # Play the notification sound
        
        playsound("notify.mp3")

    except FileNotFoundError:
        print("Error: The MP3 file 'notify.mp3' is missing. Please generate it.")
    except Exception as e:
        print(f"An error occurred during notification: {e}")


def main():
    """
    Continuously reminds the user to drink water at specified intervals.
    """
    text = "It's time to drink water"
    name = "notify.mp3"

    # Save the notification MP3 file
    save_mp3_file(text, name)

    print("Hydration Reminder System Started!")
    print("Press Ctrl+C to exit.\n")

    # Set the interval (in seconds) between reminders
    interval = 3600  # Default: 1 hour

    while True:
        try:
            remind_water()
            time.sleep(interval)  # Wait for the specified interval
        except KeyboardInterrupt:
            print("\nHydration Reminder System Stopped. Stay Hydrated!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
