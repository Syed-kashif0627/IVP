#Color Image Processing algorithms 


#1. Color Space Conversion: (RGB to Gray Scale)
import cv2
import matplotlib.pyplot as plt

image=cv2.imread('C:/Users/M.Tech DS006/Desktop/img.jpg')

image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

image_gray=cv2.cvtColor(image_rgb,cv2.COLOR_RGB2GRAY)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1,2,2)
plt.title('GrayScale Image')
plt.imshow(image_gray,cmap='gray')

plt.show()

# RGB to HSV(Hue,Saturation,Value) conversion

imageRGB=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

imageHSV=cv2.cvtColor(imageRGB,cv2.COLOR_RGB2HSV)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(imageRGB)

plt.subplot(1,2,2)
plt.title('HSV Image')
plt.imshow(imageHSV)

plt.show()