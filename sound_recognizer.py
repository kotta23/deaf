import speech_recognition as sr
import os
recognizer = sr.Recognizer()

from googletrans import Translator
import arabic_reshaper
from bidi.algorithm import get_display
translator = Translator()

def recognize_speech_from_mic():
    global recognizer
    print('espeak "please say something.."')
    #os.system('''arecord -f S16_LE -d 5 -r 44100 --device="hw:1,0"  test.wav''')
    with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
        audio = recognizer.record(source) 
    print('espeak "decodeing"')
    
    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        word_to_say_0 = get_display(arabic_reshaper.reshape(str(recognizer.recognize_google(audio, language="ar-EG"))))
        #word_to_say_0 = recognizer.recognize_google(audio)
        #print(word_to_say_0)
        response["transcription"] = word_to_say_0
        
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    return response



# words_to_say = recognize_speech_from_mic().get('transcription')
# from image_viewer_thread import ImageViewer
# image_viewer = ImageViewer()
# image_viewer.start()
# image_viewer.add_cmd(words_to_say , True)
