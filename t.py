import speech_recognition as sr

from googletrans import Translator

#arabic reshaper
import arabic_reshaper
from bidi.algorithm import get_display

translator = Translator()

recognizer = sr.Recognizer()

#with sr.WavFile("test.wav") as source:    
with sr.WavFile("/home/pi/Desktop/ocr_code/test.wav") as source:    
    r = sr.Recognizer()
    # r.adjust_for_ambient_noise(source)
    audio = recognizer.record(source) 
print('espeak "decodeing"')
try:
    #x = recognizer.recognize_google(audio , language="ar-EG" )
    x = recognizer.recognize_google(audio)

    print(x)

except sr.UnknownValueError:
    x = ('unrecognizable')



#print(x , type(x) , bidi_text_22)
result_1 = translator.translate(x, dest='ar')
reshaped_text = arabic_reshaper.reshape(str(result_1.text))    # correct its shape
bidi_text = get_display(reshaped_text)   
print(bidi_text ,x )

# print(y, type(y))
# result_3 = translator.translate(y, dest='ar')
# reshaped_text = arabic_reshaper.reshape(str(result_3.text))    # correct its shape
# bidi_text_2 = get_display(reshaped_text)   
# print(bidi_text_2 )

