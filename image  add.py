from re import A
import cv2

img_a = cv2.imread("./data/ad.jpg")
img_b = cv2.imread("./data/S2.jpg")
img3 = cv2.resize(img_a,(400,400))
img4 = cv2.resize(img_b,(400,400))

img_c = img3 + img4

print(img3[0][0])
print(img4[0][0])
print(img_c[0][0])


cv2.imshow("A", img3)
cv2.imshow("B", img4)
cv2.imshow("C", img_c)
cv2.waitKey(0)
cv2.destroyAllWindows()
