import cv2
import numpy as np

# Use the defined path variable with proper path formatting
img_path = "Lesson1/boochan.jpg"
img = cv2.imread(img_path)

# Add error handling
if img is None:
    print(f"Error: Could not load image from {img_path}")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find and draw contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        x1,y1,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)

cv2.imshow("Original Image", img)
cv2.imshow("Threshold Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()