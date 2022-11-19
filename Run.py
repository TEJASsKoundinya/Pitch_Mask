import cv2
import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join
from PIL import Image

## Setting Environment

onlyfiles = [f for f in listdir("Images_test_set")
             if isfile(join("Images_test_set", f))]

print(onlyfiles)

destination0 = 'Output_BW_test_set/'
destination1 = 'Border/'
destination2 = 'Mask/'
destination3 = 'Edge/'


### Loop for each image boundry detection

for i in onlyfiles:
   path = 'Images_test_set/'+i
   img = cv2.imread(path)
   print(img.shape)
   ### Croping to be done
   ## Slicing to crop the image
   ## Gray
   gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   ## Edge
   edges = cv2.Canny(gray_image, threshold1=150, threshold2=200)
   cv2.imwrite(destination3+i, edges)
   ##B&W
   gray_image = cv2.GaussianBlur(gray_image, (5,5), 1)
   blur = cv2.GaussianBlur(gray_image, (0,0), sigmaX=33, sigmaY=33)
   divide = cv2.divide(gray_image, blur, scale=255)
   thresh = cv2.threshold(divide, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
   kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
   morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

   cv2.imshow('Gray_scale', gray_image)
   (thresh, binary) = cv2.threshold(gray_image, 150, 225, cv2.THRESH_BINARY)
   cv2.imwrite(destination0+i, binary)
   
   ## Mask
   mask = cv2.imread(destination0+i, 0)
   mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
   img[mask == 255] = (255, 255, 255)##change mask 
   cv2.imwrite(destination2+i, img)
 
   number_of_white_pix = np.sum(edges == 255)
   number_of_black_pix = np.sum(edges == 0)

   print('Number of white pixels:', number_of_white_pix)
   print('Number of black pixels:', number_of_black_pix)
   cv2.imshow('mask', mask)  

   ## wait
   cv2.waitKey(1000)
