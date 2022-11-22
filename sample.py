import cv2
import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join
from PIL import Image
import cv2

ext = '.png'
destination0 = 'Pitch_Mask/video/image/'
destination1 = 'Pitch_Mask/video/image_mask/'
cap = cv2.VideoCapture('D:/Git-Project/Pitch_Mask/video/choped.mp4')
i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    i = str(i)
    cv2.imshow('Output', frame)
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray_scale', gray_image)
    (thresh, binary) = cv2.threshold(gray_image, 150, 225, cv2.THRESH_BINARY)
    #print(destination0+i+ext)
    cv2.imwrite(destination0+i+ext, binary)
    mask = cv2.imread(destination0+i+ext, 0)
    mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    frame[mask == 255] = (255, 255, 255)##change mask 
    cv2.imwrite(destination1+i+ext, frame)
    cv2.imshow('Output',frame)
    i = int(i)
    i += 1
    

cap.release()
cv2.destroyAllWindows()
