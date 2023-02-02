import cv2
import numpy
joker1=cv2.imread("joker-1.png")
joker2=cv2.imread("joker-2.png")
photo1=cv2.imread("joker-1.png")
photo2=cv2.imread("joker-2.png")
model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face1 =  model.detectMultiScale(joker1)
print(face1)
face2 =  model.detectMultiScale(joker2)
print(face2)
cam2 = photo2[121:(121+379),250:(250+379)]
i=0

while i<=341 :
    j=0
    while j<=341 :
        #photo2[121+i][250+j] = cphoto1[i][j]
        photo1[94+i][309+j] = cam2[i][j]
       
        j=j+1

    i=i+1
 

cv2.imshow('hello', photo1)
cv2.waitKey()
cv2.destroyAllWindows()

cphoto1 = joker1[94:(94+342),309:(309+342)]
i=0

while i<=341 :
    j=0
    while j<=341 :
        #photo2[121+i][250+j] = cphoto1[i][j]
        photo2[94+i][309+j] = cphoto1[i][j]
       
        j=j+1

    i=i+1
 

cv2.imshow('hello', photo2)
cv2.waitKey()
cv2.destroyAllWindows()        
