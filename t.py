import speech_recognition as sr

from googletrans import Translator

#arabic reshaper
import arabic_reshaper
from bidi.algorithm import get_display

translator = Translator()

recognizer = sr.Recognizer()

#with sr.WavFile("test.wav") as source:    

dict = {
    "hello":"مرحبا",
    "Federation":"اتحاد",
    "Here are you":"اتفضل",
    "Egypt":"مصر",
    "Eat":"يأكل",
    "Close":"يغلق",
    "Book":"كتاب",
    "I":"انا",
}
