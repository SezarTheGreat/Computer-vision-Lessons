import cv2
import os
import sys

img_path = os.path.join("Lesson1", "boochan.jpg")
img = cv2.imread(img_path)
if img is None:
	print(f"Failed to load image: {img_path}")
	sys.exit(1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Global Threshold with blur applied to the grayscale image
blurred = cv2.blur(gray, (10, 10))
ret, simple_thresh = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)

cv2.imshow("img", img)
cv2.imshow("Thresholding", simple_thresh)

# #Adaptive Threshold
adaptive_thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30)
cv2.imshow("dynamic threshold",adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()