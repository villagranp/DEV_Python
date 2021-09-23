import numpy
import cv2

def orderPoints(point):
    n_points = numpy.concatenate([point[0],point[1],point[2],point[3]]).tolist()
    yOrder = sorted(n_points, key=lambda n_points:n_points[1])
    x1Order =  yOrder[:2]
    x1Order = sorted(x1Order, key=lambda x1Order:x1Order[0])
    x2Order = yOrder[2:4]
    x2Order = sorted(x2Order, key=lambda x2Order: x2Order[0])
    return[x1Order[0],x1Order[1], x2Order[0], x2Order[1]]


def objectAlignment(image, width, height):
    alignImage = None
    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    umbralType, umbral = cv2.threshold(grayScale, 150 ,255, cv2.THRESH_BINARY)
    cv2.imshow('umbral', umbral)
    contour = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contour = sorted(contour, key=cv2.contourArea, reverse=True)[:1]
    for cont in contour:
        epsilon=0.01 * cv2.arcLength(cont, True)
        approx = cv2.approxPolyDP(cont, epsilon, True)
        if len(approx) == 4 :
            points = orderPoints(approx)
            pointsInt = numpy.float32(points)
            pointsSize = numpy.float32([[0,0], [width,0],[0,height],[width,height]])
            M = cv2.getPerspectiveTransform(pointsInt,pointsSize)
            alignImage = cv2.warpPerspective(image, M, (width,height))
    return alignImage
 
videoCapture = cv2.VideoCapture(0)
if not videoCapture.isOpened():
    print("No hya camaras disponibles")
    exit()

while True:
    typeCamera,camera = videoCapture.read()
    if typeCamera == False:
        break
    videoSize = objectAlignment(camera, width= 677, height= 480)
    if videoSize is not None:
        puntos = []
        grayImage = cv2.cvtColor(videoSize,cv2.COLOR_BGR2GRAY)
        blurImage = cv2.GaussianBlur(grayImage,(3,3),1)
        _,umbralScale = cv2.threshold(blurImage,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow('umbralized', umbralScale)
        contour = cv2.findContours(umbralScale, cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(videoSize, contour, -1, (255,0,0), 2)
        sumarized1val = 0.0
        sumarized2val = 0.0
        for counto in contour:
            area = cv2.contourArea(counto)
            momentum = cv2.moments(counto)
            if (momentum["m00"] == 0):
                momentum["m00"] = 1.0
            x=int(momentum["m10"]/momentum["m00"])
            y=int(momentum["m01"]/momentum["m00"])
            print(area)        
            if area < 93000 and area > 8000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(videoSize, 'Moneda de X Encontrada', (50,50), font,0.75, (0,0,255),2)
                sumarized1val += 1
                
            if area < 8000 and area > 6000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(videoSize, 'Moneda de Y Encontrada', (50,50), font,0.75, (0,0,255),2)
                sumarized2val += 0.5
            
        sumtotal = sumarized1val + sumarized2val
        print('sumatoria total: ',round(sumtotal))
        cv2.imshow('Reading',videoSize)
        cv2.imshow('original',camera)
    if(cv2.waitKey(1) == ord("q")):
        break
videoCapture.release()
cv2.destroyAllWindows()
    

