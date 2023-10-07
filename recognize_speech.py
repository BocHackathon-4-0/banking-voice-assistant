import speech_recognition as sr
import os
import pyttsx3
from gtts import gTTS


def get_voice():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    recognizer.recognize_google

    with sr.Microphone() as source:
       print("Listening... Say something:")
       recognizer.adjust_for_ambient_noise(source, duration=0.2)  # Adjust for ambient noise
        
       try:
           audio = recognizer.listen(source, timeout=20)  # Listen for up to 20 seconds
           print("Recognizing...")
            
           # Use Google Web Speech API to recognize the speech
           text = recognizer.recognize_google(audio)
            
           # TODO - delete this prints and replace with actions 
           print("You said:", text)
       except sr.WaitTimeoutError:
           print("No speech detected within the timeout period.")
       except sr.UnknownValueError:
           print("Could not understand the audio.")
       except sr.RequestError as e:
           print("Could not request results; {0}".format(e))

    return text



def read_text(text):

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Text to be read aloud
    text_to_read = text

    # Set properties
    # Female voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Speech speed 
    engine.setProperty("rate", 200)
    # Speech Volume
    engine.setProperty("volume", 5.0)    

    # Read the text aloud
    engine.say(text_to_read)

    #Wait for the speech to finish
    engine.runAndWait()

# TODO - check this command. May have to be moved elsewhere
def command_not_correct():
    incorrect_command_message = "I apologize for that! Would you be willing to repeat your demand?"
    read_text(incorrect_command_message)

# works
def replace_my_with_your(text):
    # Split the text into words
    words = text.split()
    
    # Replace 'my' with 'your'
    replaced_words = [word if word.lower() != 'my' else 'your' for word in words]
    
    # Replace me with you
    words_final = [word if word.lower() != 'me' else 'you' for word in replaced_words]

    # Join the words back into a sentence
    replaced_text = ' '.join(words_final)
    
    return replaced_text

# Call functions

# text = get_voice()

# voice_recorded = "You told me to " + text + ". Is everything correct? Shall I proceed with that request?"
# new_voice_recorded = replace_my_with_your(voice_recorded)
# read_text(new_voice_recorded)
