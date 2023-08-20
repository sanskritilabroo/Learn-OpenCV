import numpy as np
import cv2
img=cv2.imread("opencv-logo.png")
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(imgray,100,255,cv2.THRESH_BINARY)
contours=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(len(contours))
cv2.drawContours(img,contours[0],-1,(0,255,0),3)

cv2.imshow("image",img)
cv2.imshow("Image Gray",imgray)
cv2.waitKey(0)
cv2.destroyAllWindows() 
 