import cv2
import numpy
joker1=cv2.imread("joker-1.png")
joker2=cv2.imread("joker-2.png")
photo1 = joker1
photo2 = joker2
joker1 = joker1[0:517,0:860]
joker2 = joker2[0:517,0:860]
cphoto1 = photo1[94:(94+342),309:(309+342)]
cphoto2 = photo2[121:(121+379),250:(250+379)]
i=0
while i<=341 :
    j=0
    while j<=341 :
        photo1[94+i][309+j] = cphoto2[i][j]
        #photo2[121+i][250+j] = cphoto1[i][j]
        
       
        j=j+1

    i=i+1
cv2.imshow('hello', photo1)
cv2.waitKey()
cv2.destroyAllWindows() 
   
photo2[121:(121+342),250:(250+342)] = cphoto1
cv2.imshow('bye', photo2)
cv2.waitKey()
cv2.destroyAllWindows()     
       
