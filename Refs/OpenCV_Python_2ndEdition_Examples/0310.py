#0310.py
import numpy as np
import cv2
imageFile = './data/lena.jpg'
img  = cv2.imread(imageFile) 

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 10 # right


while True:   
    key = cv2.waitKeyEx(30)    
    if key == 0x1B: 
        break;
    
# 방향키 방향전환 
    elif key == 0x270000: # right
        direction = 0
    elif key == 0x280000: # down
        direction = 1
    elif key == 0x250000: # left
        direction = 2
    elif key == 0x260000: # up
        direction = 3
        
# 방향으로 이동 
    if direction == 0:     # right
        x += 100
    elif direction == 1:   # down
        y += 100
    elif direction == 2:   # left
        x -= 100
    else: # 3, up
        y -= 100
        
#   경계확인 
    if x < R:
        x = R
        direction = 0
    if x > width - R:
        x = width - R
        direction = 2
    if y < R:
        y = R
        direction = 1
    if y > height - R:
        y = height - R
        direction = 3
        
# 지우고, 그리기        
    #img = np.zeros((width, height,3), np.uint8) + 255 # 지우기
    img  = cv2.imread(imageFile) 
    cv2.circle(img, (x, y), R, (255, 255, 0), -1) 
    cv2.imshow('img', img)
    
cv2.destroyAllWindows()
