import numpy 
import cv2
img = cv2.imread('horse.jpg',0)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
  
 
cv2.imshow('image', img)
cv2.imwrite('horse_gray.jpg', img)
  

cv2.waitKey(0)          
cv2.destroyAllWindows() 



