import cv2

img = cv2.imread("boochan.jpg")

#resize
# print(img.shape)
# resize_img = cv2.resize(img,(500,500))
# cv2.imshow('img',img)
# cv2.imshow("resize image",resize_img)
# cv2.waitKey(0)

#crop
cv2.imshow('img',img)
cropped_img = img[50:220,50:220]
cv2.imshow('cropped image',cropped_img)
cv2.waitKey(0)