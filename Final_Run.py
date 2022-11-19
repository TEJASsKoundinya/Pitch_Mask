from PIL import Image, ImageFilter
import cv2
import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join
from PIL import Image


onlyfiles = [f for f in listdir("Images_test_set")
             if isfile(join("Images_test_set", f))]

print(onlyfiles)
destination = 'Images_test_set/'
destination0 = 'Output_BW_test_set/'
destination1 = 'Border/'
destination2 = 'Mask/'
for i in onlyfiles:
   path = destination0+i
   path2 = destination+i
   bgrimg = cv2.imread(path2)
   img = cv2.imread(path)
   bgrimg = cv2.resize(bgrimg, (400, 500))
   img = cv2.resize(img, (400, 500))
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   ret, gray = cv2.threshold(gray, 127, 255, 0)
   gray2 = gray.copy()
   cv2.imshow('output0', gray2)
   mask = np.zeros(gray.shape, np.uint8)
   contours, hier = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
   for cnt in contours:
      if 2000 < cv2.contourArea(cnt) < 5000000:
         cv2.drawContours(img, [cnt], 0, (0, 255, 0), 2)
         cv2.drawContours(mask, [cnt], 0, 255, -1)
         cv2.drawContours(bgrimg, [cnt], 0, (0, 255, 0), 2)
   cv2.imwrite(destination1+i,img) 
   cv2.imshow('BGRout', bgrimg)     
   cv2.imshow('output', img)
   #cv2.imshow(mask)
   cv2.waitKey(1000)




