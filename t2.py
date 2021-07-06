from gpiozero import Button
import os
import time
B1_PIN  = 20
B2_PIN  = 21
b1 = Button(B1_PIN, pull_up=True, bounce_time=0.1)
b2 = Button(B2_PIN, pull_up=True, bounce_time=0.1)


while True:
    if b1.is_pressed:
        print("b1 is pressed")
    elif b2.is_pressed:
        print("b2 is pressed")
        time.sleep(0.7)
        os.system('''arecord -f S16_LE -d 5 -r 44100 --device="hw:1,0"  kot.wav''')
