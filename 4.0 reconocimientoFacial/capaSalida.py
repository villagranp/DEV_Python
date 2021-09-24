import cv2
import os
import numpy

mainRoute = "C:\\Users\\pablo.villagran\\Documents\\DEV_Python\\4.0 reconocimientoFacial\\Data"
listData = os.listdir(mainRoute)
trainingEigen = cv2.face.EigenFaceRecognizer_create()
trainingEigen.read('C:\\Users\\pablo.villagran\\Documents\\DEV_Python\\4.0 reconocimientoFacial\\TrainingEigenFaceRecognizer.xml')
noise=cv2.CascadeClassifier(r"C:\Users\pablo.villagran\Documents\DEV_Python\4.0 reconocimientoFacial\haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

while True:
    _,capture = camera.read()
    grayScale = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)
    idCapture = grayScale.copy()
    faces = noise.detectMultiScale(grayScale,1.3, 3)
    for (x,y,e1,e2) in faces:
        faceCaptured = idCapture[y:y+e2,x:x+e1]
        faceCaptured = cv2.resize(faceCaptured, (260,260), interpolation=cv2.INTER_CUBIC)
        result = trainingEigen.predict(faceCaptured)
        cv2.putText(capture, '{}'.format(result), (x, y-5), 1, 1.3, (255,0,100), 1, cv2.LINE_AA )
        if result[1] < 9000:
            cv2.putText(capture, '{}'.format(listData[result[0]]), (x, y-25), 1, 1.3, (255,0,100), 2, cv2.LINE_AA )
            cv2.rectangle(capture, (x,y), (x+e1,y+e2), (100,100,255), 2)
        else:
            cv2.putText(capture, 'No Identificado', (x, y-25), 1, 1.3, (255,0,100), 2, cv2.LINE_AA )
            cv2.rectangle(capture, (x,y), (x+e1,y+e2), (100,100,255), 2)
        
    cv2.imshow('Reading...',capture)
    if(cv2.waitKey(1) == ord("q")):
        break
    
camera.release()
cv2.destroyAllWindows()
    





