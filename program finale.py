import cv2
import numpy as np
import pytesseract
import picamera
from gtts import gTTS
import os
import time
from PIL import Image


time.sleep(2)


def get_string(img_path):

    # Read image with opencv
  with picamera.PiCamera() as camera:
    camera.resolution = (1024, 720)
    camera.capture("f1.jpg")   
    print("picture taken.")
    capture = cv2.imread(img_path) 
    time.sleep(1)
    #capture = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(img, kernel, iterations=1)
    #img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    #cv2.imwrite("removed_noise.jpg", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    #cv2.imwrite("capture.jpg", capture)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(img_path))

    # Remove template file
    #os.remove(temp)

    return result

time.sleep(1)
    

print ('--- Start recognize text from image ---')

result1=get_string("f1.jpg")

print (result1)
time.sleep(5)

tts = gTTS(text=result1 , lang='en')
tts.save("result.mp3")
os.system("mpg321 result.mp3")


print ("------ Done -------")
