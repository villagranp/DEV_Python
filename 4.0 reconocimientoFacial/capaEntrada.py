import cv2
import os
#import imutils
import numpy

model='Josue Guillen'
mainRoute = r"C:\Users\pablo.villagran\Documents\DEV_Python\4.0 reconocimientoFacial\Data"
finalRoute= mainRoute+'\\'+model
if not os.path.exists(finalRoute):
    os.makedirs(finalRoute)


#noise=cv2.CascadeClassifier("C:\\Users\\pablo.villagran\\Documents\\DEV_Python\\4.0 reconocimientoFacial\\haarcascade_frontalface_default.xml")
#prefix r"String" to use a Raw String
noise=cv2.CascadeClassifier(r"C:\Users\pablo.villagran\Documents\DEV_Python\4.0 reconocimientoFacial\haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)
id = 0

while True:
    response,capture = camera.read()
    if response == False: 
        break
    #capture.imutils.resize(capture,width=640)
    grayScale = cv2.cvtColor(capture,cv2.COLOR_BGR2GRAY)
    face = noise.detectMultiScale(grayScale,1.3, 3)
    idCapture = capture.copy()
    
    for (x,y,e1,e2) in face:
        cv2.rectangle(capture, (x,y), (x+e1,y+e2), (40,40,200), 2)
        faceCaptured = idCapture[y:y+e2,x:x+e1]
        faceCaptured = cv2.resize(faceCaptured, (260,260), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(finalRoute+'\\'+'faceCaptured_{}.jpg'.format(id), faceCaptured)
        id += 1
    cv2.imshow('reading...',capture)
    
    if id > 550:
        break
    
    if(cv2.waitKey(1) == ord("q")):
        break
camera.release()
cv2.destroyAllWindows()