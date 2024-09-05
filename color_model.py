import cv2
import numpy as np

# Load the color image
img = cv2.imread('example_image.jpg')

# Split the image into B, G, R components
B, G, R = cv2.split(img)

# Convert the image to HSV and YCrCb color spaces
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Split HSV and YCrCb images into their components
H, S, V = cv2.split(hsv_img)
Y, Cr, Cb = cv2.split(ycrcb_img)

# Create a window to display images
cv2.imshow('Original Image', img)

# Display the individual color channels
cv2.imshow('Red Channel', R)
cv2.imshow('Green Channel', G)
cv2.imshow('Blue Channel', B)

# Display the HSV channels
cv2.imshow('Hue Channel', H)
cv2.imshow('Saturation Channel', S)
cv2.imshow('Value/Intensity Channel', V)

# Display the YCrCb channels
cv2.imshow('Luminance (Y) Channel', Y)
cv2.imshow('Chrominance (Cb) Channel', Cb)
cv2.imshow('Chrominance (Cr) Channel', Cr)

# Wait until a key is pressed and destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
