import cv2
import numpy as np

image = cv2.imread('website.jpg')

image_resized = cv2.resize(image, None, fx=1.5, fy=1.5)


#------------ PHAse 2
#removing impurities from image 
image_cleared = cv2.medianBlur(image_resized, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)

image_cleared = cv2.edgePreservingFilter(image_cleared, sigma_s=5)



#----------Phase 3
#Bilatral image filtering
image_filtered = cv2.bilateralFilter(image_cleared, 3, 10, 5)

for i in range(2):
    image_filtered = cv2.bilateralFilter(image_filtered, 3, 20, 10)

for i in range(3):
    image_filtered = cv2.bilateralFilter(image_cleared, 5, 30, 10)

# for i in range(3):
#     image_filtered = cv2.bilateralFilter(image_cleared, 5, 40, 10)
    
# for i in range(2):
#     image_filtered = cv2.bilateralFilter(image_cleared, 3, 40, 5)
    

#-------------Phase 4
#sharpaning the image using addWeighted
gaussian_mask = cv2.GaussianBlur(image_filtered, (7,7), 2)
image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
image_sharp = cv2.addWeighted(image_filtered, 1.4, gaussian_mask, -0.2, 10)

#displaying images
cv2.imshow('Final Image', image_sharp)
cv2.imshow('Clear IMpurities', image_cleared)
cv2.imshow('original', image_resized)
cv2.waitKey(0)

