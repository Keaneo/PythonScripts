from PIL import Image, ImageFilter
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import time

def ConvToPIL(img):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    return img

def ConvToCV2(img):
    img = np.array(img)
    img = img[:,:,::-1].copy()
    return img


root = tk.Tk()
root.withdraw()

#file_path = filedialog.askopenfilename()

vid = cv2.VideoCapture(0) 
time.sleep(1)
#im = Image.open(file_path).convert('RGB')
delay = 0

while True:
    time.sleep(delay)
    #im = im.filter(ImageFilter.GaussianBlur(10))

    ret, image = vid.read()
    #image = ConvToCV2(im)


    cv2.imshow("Original", image)#cv2.resize(image, (640, 480)))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, threshhold = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY) 

    kernel = np.ones((1, 1), np.uint8) 

    erosion = cv2.erode(threshhold, kernel, iterations = 1) 


    working = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
    working = cv2.morphologyEx(working, cv2.MORPH_CLOSE, kernel)


    contours, hierarchy = cv2.findContours(working, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image = working
    image = cv2.resize(image, (640, 480))
    image = ConvToPIL(image)
    image = image.filter(ImageFilter.GaussianBlur(1))
    image = image.filter(ImageFilter.SMOOTH)
    image = image.filter(ImageFilter.SHARPEN)
    image = ConvToCV2(image)
    cv2.imshow("Printed", image)
    #cv2.destroyAllWindows()

    if cv2.waitKey(0) & 0xFF == ord('q'):
        #cv2.destroyAllWindows()
        break
vid.release()
cv2.destroyAllWindows()
exit()

