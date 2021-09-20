import cv2
image = cv2.imread('C:\PhytonLibs\contorno.jpg')

#grayScale
grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
umbralType,umbral = cv2.threshold(grayScale,100,255,cv2.THRESH_BINARY)
contour, hierachy = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contour, -1, (251,60,50),3 )


#diplay the image.
cv2.imshow('Original Image',image)
#cv2.imshow('GrayScale Image',grayScale)
#cv2.imshow('Umbralized Image',umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()


