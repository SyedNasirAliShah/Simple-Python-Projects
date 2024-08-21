from win32com.client import Dispatch

def voice_shoutout_generator():
    # List of names 
    names = ["Nasir", "Aslam", "Javed", "Miadad"]
    
    # Initialize the SAPI.SpVoice object
    speak = Dispatch("SAPI.SpVoice").speak

    for name in names:
        speak(f"Shoutout to {name}")


voice_shoutout_generator()

# Uncomment the following section if you want to use gTTS for the voice output


# from gtts import gTTS
# import os
#
# def gtts_voice_shoutout():
#     tts = gTTS(text="This is the PC speaking", lang='en')
#     tts.save("pcvoice.mp3")
#     # Play the mp3 file
#     os.system("start pcvoice.mp3")
#

# gtts_voice_shoutout()
