import numpy
import cv2

gaussValue = 3
kernelValue = 3
sigmaX = 0

sourceImage = cv2.imread('C:\PhytonLibs\monedas.jpg')
grayScale = cv2.cvtColor(sourceImage, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(grayScale, (gaussValue, kernelValue ), sigmaX)
canny = cv2.Canny(gauss, 60, 100)

kernel = numpy.ones((kernelValue,kernelValue), numpy.uint8)
close = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
contour, hierachy = cv2.findContours(close.copy() , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Monedas encontradas: {}".format(len(contour)))
cv2.drawContours(sourceImage, contour, -1, (251,60,50),3 )

#diplay the image.
cv2.imshow('Original Image',sourceImage)
#cv2.imshow('GrayScale Image',grayScale)
#cv2.imshow('GaussModel Image',gauss)
#cv2.imshow('CannyModel Image',canny)
#cv2.imshow('MorphClose Model Image',close)


cv2.waitKey(0)
cv2.destroyAllWindows()


