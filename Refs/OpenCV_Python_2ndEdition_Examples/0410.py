# 0410.py
import cv2
import numpy as np
 
src = cv2.imread('./data/ad.jpg', cv2.IMREAD_GRAYSCALE)
shape = src.shape[0], src.shape[1], 3
dst = np.zeros(shape, dtype=np.uint8)
# BGR = 0 1 2
##dst[:,:,0] = src  # B = 0  
##dst[:,:,1] = src  #G = 1
dst[:,:,2] = src    #R = 2

dst[300:500, 400:900, :] = [200, 155, 255]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()    
cv2.destroyAllWindows()
