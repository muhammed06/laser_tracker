__author__ = 'bilmuh'
Hmindeg = 55
Hmaxdeg = 65
Smindeg = 100
Smaxdeg = 255
Vmindeg = 100
Vmaxdeg = 255
"""
cv2.namedWindow("kontrol", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("minH", "kontrol", 125, 1, Hmindeg)
cv2.createTrackbar("maxH", "kontrol", 125, 1, Hmaxdeg)
cv2.createTrackbar("minS", "kontrol", 255, 1, Smindeg)
cv2.createTrackbar("maxS", "kontrol", 255, 1, Smaxdeg)
cv2.createTrackbar("minV", "kontrol", 255, 1, Vmindeg)
cv2.createTrackbar("maxV", "kontrol", 255, 1, Vmaxdeg)
"""