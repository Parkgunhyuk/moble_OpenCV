# 0601.py
import cv2
import numpy as np

src = cv2.imread('./data/psy.jpg', cv2.IMREAD_GRAYSCALE)
src2 = cv2.resize(src,(600,600))
dst1= cv2.boxFilter(src2, ddepth=-1, ksize=(11, 11))
dst2 = cv2.boxFilter(src2, ddepth=-1, ksize=(21, 21))

dst3 = cv2.bilateralFilter(src2, d=11, sigmaColor=10, sigmaSpace=10)
dst4 = cv2.bilateralFilter(src2, d=-1, sigmaColor=10, sigmaSpace=10)

cv2.imshow('dst1',  dst1)    
cv2.imshow('dst2',  dst2)
cv2.imshow('dst3',  dst3)
cv2.imshow('dst4',  dst4)
cv2.waitKey()    
cv2.destroyAllWindows()
