import cv2

img = cv2.imread("boochan.jpg")

bgr_clr = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray_clr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_clr = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("image",img)
cv2.imshow("convert image to bgr",bgr_clr)
cv2.imshow("convert image to gray",gray_clr)
cv2.imshow("convert image to hsv",hsv_clr)
cv2.waitKey(0)
cv2.destroyAllWindows()