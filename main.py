import cv2 as cv
import os
import numpy as np
import load
import stackImages

prefix_path = 'source'
path1 = os.path.join(prefix_path, '01')

img = load.Load_Image(path1)  # img is a list
img_gray = load.RGB2GRAY(img) # img_gray is a list

# stack_image = stackImages.stackImages(scale=0.5, imgArray=img)

cv.imshow("windows_name", img_gray[1])
cv.waitKey(0)