import cv2

img = cv2.imread("boochan.jpg")

k_size = 5
blurred_img = cv2.blur(img,(k_size,k_size))
gaussian_img = cv2.GaussianBlur(img,(k_size,k_size),3)
median_blur = cv2.medianBlur(img,k_size)

cv2.imshow("Original Image",img)
cv2.imshow("Blurred image",blurred_img)
cv2.imshow("Gaussian Blur",gaussian_img)
cv2.imshow("Median Blur",median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()