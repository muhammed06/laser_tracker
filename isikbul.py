__author__ = 'bilmuh'
import cv2
import numpy as np
import icerikler

cap = cv2.VideoCapture(0)
eskiy=float(-1.0)
eskix=float(-1.0)
_, imgs = cap.read()
color = tuple(reversed((0,0,0)))
imgs[:] = color
while(True):
    _, frame = cap.read()

    hsvc = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    altYesil = np.array([icerikler.Hmindeg, icerikler.Smindeg, icerikler.Vmindeg])
    ustYesil = np.array([icerikler.Hmaxdeg, icerikler.Smaxdeg, icerikler.Vmaxdeg])
    mask = cv2.inRange(hsvc, altYesil, ustYesil)
    cv2.erode(mask,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
    cv2.dilate(mask,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))

    konum=cv2.moments(mask)
    yeksen = konum["m01"]
    xeksen = konum["m10"]
    alan = konum["m00"]

    if alan>10000:
        yenix = xeksen / alan
        yeniy = yeksen / alan
        if (eskix >= 0 and eskiy >= 0 and yenix >= 0 and yeniy >= 0):
            cv2.circle(imgs,(int(yenix),int(yeniy)),2,(0,255,0),2)

        eskix = yenix
        eskiy = yeniy
    cv2.bitwise_or(imgs,frame,frame)
    cv2.imshow("frame", frame)
    cv2.imshow("maskeli", mask)
    k = cv2.waitKey(30) & 0xff
    if k == 81:
        break

cap.release()
cv2.destroyAllWindows()