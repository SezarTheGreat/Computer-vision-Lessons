import cv2
import os
import numpy as np

img_path = "boochan.jpg"
img = cv2.imread(os.path.join('.',img_path))
if img is None:
    raise FileNotFoundError(f"Image file not found or failed to load: {img_path}")

# convert to grayscale before running Canny (expects single-channel)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_edge = cv2.Canny(gray, 100, 200)

# cv2 dilate
img_edge_d = cv2.dilate(img_edge,np.ones((3,3),dtype=np.int8))

# cv2 erode
img_edge_e = cv2.erode(img_edge_d,np.ones((3,3),dtype=np.int8))

# show the edge image
cv2.imshow("Original Image",img)
cv2.imshow("Edges", img_edge)
cv2.imshow("Canny Dilate",img_edge_d)
cv2.imshow("Eroded Image",img_edge_e)
cv2.waitKey(0)
cv2.destroyAllWindows()