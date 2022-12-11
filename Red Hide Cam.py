import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)
background = 0
time.sleep(3)

for _ in range(30):
    ret, background = cam.read()

background = np.flip(background, axis=1)

while cam.isOpened():
    ret, frame1 = cam.read()
    if cv2.waitKey(10) == ord("q"):
        break
    frame1 = np.flip(frame1, axis=1)
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (35, 35), 0)

    lower = np.array([0, 120, 70])
    upper = np.array([10, 255, 255])
    mask01 = cv2.inRange(hsv, lower, upper)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask02 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask01 + mask02
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    frame1[np.where(mask == 255)] = background[np.where(mask == 255)]

    cv2.imshow("cam", frame1)

cam.release()
cv2.destroyAllWindows()
