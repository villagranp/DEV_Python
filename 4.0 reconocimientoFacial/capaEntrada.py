import cv2
import numpy

#noise=cv2.CascadeClassifier("C:\\Users\\pablo.villagran\\Documents\\DEV_Python\\4.0 reconocimientoFacial\\haarcascade_frontalface_default.xml")
#prefix r"String" to use a Raw String
noise=cv2.CascadeClassifier(r"C:\Users\pablo.villagran\Documents\DEV_Python\4.0 reconocimientoFacial\haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)
while True:
    _,capture = camera.read()
    grayScale = cv2.cvtColor(capture,cv2.COLOR_BGR2GRAY)
    face = noise.detectMultiScale(grayScale,1.3, 3)
    for (x,y,e1,e2) in face:
        cv2.rectangle(capture, (x,y), (x+e1,y+e2), (40,40,200), 2)
        
    cv2.imshow('reading...',capture)
    
    if(cv2.waitKey(1) == ord("q")):
        break
camera.release()
cv2.destroyAllWindows()