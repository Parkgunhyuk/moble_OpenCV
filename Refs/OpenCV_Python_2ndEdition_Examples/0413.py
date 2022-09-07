# 0413.py
import cv2
src2 = cv2.imread('./data/S2.jpg')
src = cv2.resize(src2,(500,500))
gray   = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
hsv    = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow('gray',  gray)
cv2.imshow('yCrCv', yCrCv)
cv2.imshow('hsv',   hsv)

cv2.waitKey()    
cv2.destroyAllWindows()
