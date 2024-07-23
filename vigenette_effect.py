import cv2
import numpy as np

image = cv2.imread('website.jpg')
rows, cols = image.shape[:2]

#genrating vigneete mask using Gaussian kernals
kernal_x = cv2.getGaussianKernel(cols,200)
kernal_y = cv2.getGaussianKernel(rows,200)
kernal = kernal_y * kernal_x.T

#normalizing the kernal 
kernal = kernal/np.linalg.norm(kernal)

#genrating a mask to image 
mask = 255 * kernal
output = np.copy(image)

#appling the mask to each channel in the input image
for i in range(3):
    output[:,:,i] = output[:,:,i] * mask
cv2.imshow('Original', image)
cv2.imshow('Vignette', output)
cv2.waitKey(0)