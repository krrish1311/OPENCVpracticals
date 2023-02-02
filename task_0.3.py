import cv2
import numpy
p1=cv2.imread("download.jfif")
p2=cv2.imread("images.jfif")
cp1 =p1[0:169,0:299]
photo1=numpy.hstack((cp1,p2))
import cv2
cv2.imshow("hi", photo1)
cv2.waitKey()
cv2.destroyAllWindows()
photo2=numpy.vstack((cp1,p2))
                
cv2.imshow("hi", photo2)
cv2.waitKey()
cv2.destroyAllWindows()
