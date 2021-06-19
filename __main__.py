import cv2
import os
from ocr_lib import  ocr_space_file, API_KEY
print("hey")
from camera import Camera
from sound_recognizer import recognize_speech_from_mic
from image_viewer_thread import ImageViewer
import requests
from multiprocessing import Queue
import cv2
from gpiozero import Button
from time import sleep
from picamera import PiCamera
print("before camera")
camera = PiCamera()
camera.resolution = (640, 480)
print("after cam.....")
B1_PIN  = 20
B2_PIN  = 21
b1 = Button(B1_PIN, pull_up=True, bounce_time=0.1)
b2 = Button(B2_PIN, pull_up=True, bounce_time=0.1)

images_container = Queue(3)
#cam = Camera(images_container)
#cam.start()
print("after btns")
image_viewer = ImageViewer()
image_viewer.start()

while True:
    
    words_to_say = ""
    if b1.is_pressed:
        print("b1 is pressed")
        camera.start_preview()
        sleep(5)
        camera.capture('hello.png')
        camera.stop_preview()
        try:
            words_to_say = ocr_space_file(filename="hello.png", api_key=API_KEY, language='eng')
        except requests.exceptions.ConnectionError:
            print("fail to communicate")
        #os.remove(".tmp.png")
    elif b2.is_pressed:
        print("b2 is pressed")
        words_to_say = recognize_speech_from_mic().get('transcription')
    
    if not words_to_say is None and len(words_to_say) > 0:
        print(words_to_say)
        image_viewer.add_cmd(words_to_say)
        print("press any key again..")



cam.close()
