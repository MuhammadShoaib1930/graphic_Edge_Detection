import cv2 as cv
import numpy as np
img = cv.imread('apple1.png',0)
image_resize = cv.resize(img,(300,200))
block_image = image_resize[10:20,0:10]
edg = cv.Canny(image_resize,100,200)
cv.imshow("My WIn",image_resize)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('shoaib.jpg',edg)
