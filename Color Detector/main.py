import cv2
from util import get_limits
from PIL import Image

color = [0,255,0] #yellow in BGR colorspace
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImg = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_limit,upper_limit = get_limits(color=color)

    mask = cv2.inRange(hsvImg,lower_limit,upper_limit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1,y1,x2,y2 = bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask of the choosen color",mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()