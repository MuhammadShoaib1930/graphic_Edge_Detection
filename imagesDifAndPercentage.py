import cv2 as cv
import numpy as np

img1 = cv.imread('apple1.png')
img1_gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
img1_reSize = cv.resize(img1_gray,(200,200))
img1_reSize = cv.Canny(img1_reSize,100,200)

img2 = cv.imread('apple1.png')
img2_gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
img2_reSize = cv.resize(img2_gray,(200,200))
img2_reSize = cv.Canny(img2_reSize,100,200)

diff_images = cv.absdiff(img1_reSize,img2_reSize)

similar_pixels = np.sum(diff_images == 0)
total_pixels = diff_images.size
similarity_percentage= (similar_pixels/total_pixels)*100

cv.imshow("T1",img1_reSize)
cv.imshow("T2",img2_reSize)
print(similarity_percentage)
cv.waitKey(0)
cv.destroyAllWindows()