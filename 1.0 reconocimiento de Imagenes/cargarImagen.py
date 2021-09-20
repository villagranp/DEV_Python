#import sys
#sys.path.append('C:\Python38\Lib\site-packages')
import cv2

image = cv2.imread('C:\PhytonLibs\contorno.jpg')
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


