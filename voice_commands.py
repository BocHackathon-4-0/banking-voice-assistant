# Import recognize speech module
import recognize_speech
import boc_ads


text = recognize_speech.get_voice()
recognize_speech.read_text(text)

def stop_assistance():
    recognize_speech.read_text()
    recognize_speech.read_text(boc_ads.get_random_ad)
    quit()

if ("yes" or "correct" in text):
    text = recognize_speech.get_voice()
elif ("exit" in text):
    recognize_speech.read_text("I hope I helped.")
    stop_assistance()
else:
    recognize_speech.command_not_correct()


