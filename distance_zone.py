# importing the module
import cv2

img = cv2.imread(r"C:\Users\krish\OneDrive\Desktop\pitchblack.jpeg")

# Drawing rectangles
#White Rectangle for the pitch
cv2.rectangle(img, (0,419), (1000,581),
              (255, 255, 255), 4)
# Red rectangle for yorker
cv2.rectangle(img, (54,419), (89,581),
              (0, 0, 255), 4)

# Blue rectangle for full
cv2.rectangle(img, (95, 419), (177, 581),
              (255, 0, 0), 4)

# Green rectangle for good
cv2.rectangle(img, (182, 419), (355, 581),
              (0, 255, 0), 4)
# Yellow rectangle for short
cv2.rectangle(img, (360, 419), (946,581),
              (0, 255, 255), 4)


cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
