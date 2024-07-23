import cv2
import numpy as np

def changeRadius(val):
    global radius 
    radius = val

def changeFocus(val):
    global value
    value = val

image = cv2.imread('website.jpg')
rows, cols = image.shape[:2]
value = 1
radius = 130
mask = np.zeros((int(rows*(value*0.1+1)),int(cols*(value*0.1+1))))

cv2.namedWindow('Trackbars')
cv2.createTrackbar('Radius', 'Trackbars', radius, 500, changeRadius)
cv2.createTrackbar('Focus', 'Trackbars', value, 10, changeFocus)

while(True):
    #genrating vignette mask using gausssian kernals
    kernal_x = cv2.getGaussianKernel(int(cols*(0.1*value+1)),radius)
    kernal_y = cv2.getGaussianKernel(int(rows*(0.1*value+1)),radius)
    kernal = kernal_y * kernal_x.T

    #normalizing the kernal
    kernal = kernal/np.linalg.norm(kernal)

    #genrating a mask to image
    mask = 255 * kernal
    output = np.copy(image)

    #appiling the mask to each channel int the input image

    mask_imposed = mask[int(0.1*value*rows):,int(0.1*value*cols):]
    for i in range(3):
        output[:,:,i] = output[:,:,i] * mask_imposed
    cv2.imshow('Original', image)
    cv2.imshow('vignette', output)
    key = cv2.waitKey(50)
    if(key==ord('q')):
        break
    elif(key==ord('s')):
        cv2.imwrite('output_mask{}_deviation{}.jpg',output)

