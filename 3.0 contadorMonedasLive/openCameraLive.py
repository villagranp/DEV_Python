import numpy
import cv2

def orderPuntos(puntos):
    n_puntos = numpy.concatenate()


videoCapture = cv2.VideoCapture(0)
if not videoCapture.isOpened():
    print("No hya camaras disponibles")
    exit()

while True:
    typeCamera,camera = videoCapture.read()
    grayScale = cv2.cvtColor(camera, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("en vivo", grayScale)
    if(cv2.waitKey(1) == ord("q")):
        break
videoCapture.release()
cv2.destroyAllWindows()
    

