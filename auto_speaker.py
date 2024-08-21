# AutoSpeaker in Python

from win32com.client import Dispatch

def initialize_speaker():
    speaker = Dispatch("SAPI.SpVoice")
    return speaker

def set_voice(speaker, voice_index=0):
    voices = speaker.GetVoices()
    speaker.Voice = voices.Item(voice_index)

def set_rate(speaker, rate=0):
    speaker.Rate = rate

def speak(text, gender):
    speaker = initialize_speaker()
    set_voice(speaker, gender)  # 0 for male voice, 1 for male
    set_rate(speaker, 1)   # Set rate (speed) of speech, 0 is default, positive for faster, negative for slower
    speaker.Speak(text)

if __name__ == "__main__":
    gender = 0 # for male
    welcome = "Welcome to the AutoSpeaker!"
    text = "Enter the message to speak or press quit for exit"
    print(f"{welcome}")
    speak(welcome, gender)
    print(f"{text}")
    speak(text, gender)
    friends = ["friend1", "friend2"]
    while True:
        if gender == 0:
            speaker = input(f"{friends[0]}: ")
        else:
            speaker = input(f"{friends[1]}: ")
        if speaker == "quit":
            speak("Ok, bye bye friend", gender)
            break
        speak(speaker, gender)
        gender = 1 - gender