import numpy
import cv2
img1=cv2.imread('bird.jpg')
h1=img1.shape[0]
w1=img1.shape[1]
c1=img1.shape[2]
pixel1= img1[int(h1/2),int(w1/2)]

img2=cv2.imread('cat.jpg')
h2=img2.shape[0]
w2=img2.shape[1]
c2=img2.shape[2]
pixel2= img2[int(h2/2),int(w2/2)]

img3=cv2.imread('flowers.jpg')
h3=img3.shape[0]
w3=img3.shape[1]
c3=img3.shape[2]
pixel3= img3[int(h3/2),int(w3/2)]

img4=cv2.imread('horse.jpg')
h4=img4.shape[0]
w4=img4.shape[1]
c4=img4.shape[2]
pixel4= img4[int(h4/2),int(w4/2)]


filename = 'example.csv'

with open (filename, 'w') as f:
    
    

    f.write('%s,%d,%d,%d,%d,%d,%d\n' % ('bird.jpg',h1, w1,c1,pixel1[0],pixel1[1],pixel1[2]))
    f.write('%s,%d,%d,%d,%d,%d,%d\n' % ('cat.jpg',h2, w2,c2,pixel2[0],pixel2[1],pixel2[2]))
    f.write('%s,%d,%d,%d,%d,%d,%d\n' % ('flowers.jpg',h3, w3,c3,pixel3[0],pixel3[1],pixel3[2]))
    f.write('%s,%d,%d,%d,%d,%d,%d\n' % ('horse.jpg',h4, w4,c4,pixel4[0],pixel4[1],pixel4[2]))












    


cv2.waitKey(0)
cv2.destroyAllWindows()

