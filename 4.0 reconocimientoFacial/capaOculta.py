import cv2
import os
import numpy
from time import time

mainRoute = "C:\\Users\\pablo.villagran\\Documents\\DEV_Python\\4.0 reconocimientoFacial\\Data"
listData = os.listdir(mainRoute)
ids=[]
faces=[]
id=0
initialTime = time()
for row in listData:
    finalRoute = mainRoute+'\\'+row
    print('Start Reading')
    for file in os.listdir(finalRoute):
        print('Image: ',finalRoute+'\\'+file)
        ids.append(id)
        faces.append(cv2.imread(finalRoute+'\\'+file, 0))
    id +=1
    finalTime = time()
    totalTime = finalTime - initialTime
    print('ID Entrenamiento: ',id,' Tiempo: ',totalTime)

trainingEigen = cv2.face.EigenFaceRecognizer_create()
print('Starting Training')
trainingEigen.train(faces, numpy.array(ids))
print('Save Training as a File')
trainingEigen.write(r"C:\\Users\\pablo.villagran\\Documents\\DEV_Python\\4.0 reconocimientoFacial\\TrainingEigenFaceRecognizer.xml")
print('Training Finished')




