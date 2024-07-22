import cv2
import numpy as np

image = cv2.imread('website.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#performing thw edge detection
#using Sobel Filter
gradient_soblex = cv2.Sobel(image, -1, 1, 0)
gradient_sobley = cv2.Sobel(image, -1, 0, 1)
gradient_soblexy = cv2.addWeighted(gradient_soblex, 0.5, gradient_sobley, 0.5, 0)

#using Laplacian Filter
gradient_laplacian = cv2.Laplacian(image, -1)

#using Canny Filter
canny_output = cv2.Canny(image, 80, 150)

cv2.imshow('Sobel X', gradient_soblex)
cv2.imshow('Sobel Y', gradient_sobley)
cv2.imshow('Sobel X+Y', gradient_soblexy)
cv2.imshow('Laplacian', gradient_laplacian)
cv2.imshow('Canny', canny_output)

cv2.waitKey()