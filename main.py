import cv2 as cv
import os
import numpy as np
import load
import stackImages

prefix_path = 'source'
path1 = os.path.join(prefix_path, '01')

img = load.Load_Image(path1)

stack_image = stackImages.stackImages(scale=0.5, imgArray=img)

cv.imshow("windows_name", stack_image)
cv.waitKey(0)
//20211106
