import cv2
import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join
from PIL import Image



onlyfiles = [f for f in listdir("Images_test_set")
             if isfile(join("Images_test_set", f))]

print(onlyfiles)

destination0 = 'Output_BW_test_set/'
destination1 = 'Mask/'
destination2 = 'Border/'
for i in onlyfiles:
   path = 'Images_test_set/'+i
   img = cv2.imread(path)
   print(img.shape)
   ### Croping to be done
   gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   (thresh, binary) = cv2.threshold(gray_image, 150, 225, cv2.THRESH_BINARY)
   cv2.imwrite(destination0+i, binary)
   mask = cv2.imread(destination0+i, 0)
   mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
   img[mask == 255] = (36, 255, 12)##change mask 
   cv2.imwrite(destination1+i, img)
   ##Border line appending
   
   cv2.rectangle(img, (12,100), (300,200), (0,0,255), 2)
   cv2.imwrite(destination2+i, img)
   cv2.imshow('image', img)
   #cv2.imshow('mask', mask)
   


   ##########BOX##########
   #
   #cv2.rectangle(Face, (x, y), (x+w, y+h), (255, 255, 255), thickness)
   cv2.waitKey(1000)

   
###################################################333
   #img1 = cv2.cvtColor(binary,cv2.COLOR_BGR2RGB)
   #hsv = cv2.cvtColor(img1, cv2.COLOR_RGB2HSV)
   # define range of brown color in HSV
   #lower_brown = np.array([0, 0, 255])
   #upper_brown = np.array([255, 255, 255])
   # Threshold the HSV image to get only blue colors
   #mask = cv2.inRange(hsv, lower_brown, upper_brown)
   # Bitwise-AND mask and original image
   #patch = cv2.bitwise_and(img1, img1, mask=mask)
   #cv2.waitKey(1000)
   #cv2.imshow('Patch of pitch', patch)
   #cv2.imwrite(destination1+i, patch)
