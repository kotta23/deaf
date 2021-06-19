from threading import Thread
from collections import deque
import os
import time
import numpy as np
import cv2
# Load image based on OLED display height.  Note that image is converted to 1 bit color.

    
class ImageViewer(Thread):
    def __init__(self):
        super(ImageViewer, self).__init__()
        self.__buffer = deque(maxlen=10)
        

    def run(self) -> None:
        while True:
            if len(self.__buffer ):
                words_to_say = self.__buffer.popleft()
                if len(words_to_say):
                    words = words_to_say.split()
                    for word in words:
                        target_path = os.path.join(os.getcwd(), "images", f"{word}.bmp")
                        print(target_path)
                        if os.path.isfile(target_path):
                            image =  cv2.imread(target_path)
                        else:
                            image = np.full((64,128,3), 255,np.uint8 )
                            cv2.putText(image,word,(30,30),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),2)
                        cv2.imshow("image viewer", image)
                        cv2.waitKey(3000)
                    cv2.destroyAllWindows()
    def add_cmd(self, cmd):
        self.__buffer.append(cmd)

