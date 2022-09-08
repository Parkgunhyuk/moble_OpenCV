#0309.py
import numpy as np
import cv2
imageFile = './data/ad.jpg'

img  = cv2.imread(imageFile)
img2 = cv2.resize(img,(512,512))
img3 = np.zeros(shape=(512,512,3), dtype=np.uint8) 
text = 'good              boy'
org = (80,220)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img3,text, org, font, 1, (255,120,0), 2)

size, baseLine = cv2.getTextSize(text, font, 1, 2)
#print('size=', size)
#print('baseLine=', baseLine)
#cv2.rectangle(img3, org, (org[0]+size[0], org[1]-size[1]), (0, 0, 255))
#cv2.circle(img3, org, 3, (0, 255,0), 2)

hap = cv2.add(img2,img3)
cv2.imshow('img', hap)
cv2.waitKey()
cv2.destroyAllWindows()
