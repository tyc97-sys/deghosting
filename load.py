import cv2 as cv
import os
import numpy as np

def Load_Source(folder_path):

    file_list = os.listdir(folder_path)

    dir_list = []
    for f in file_list:
        dir_list.append(os.path.join(folder_path, f))

    return dir_list


def Load_Image(dir_list):
    imgdir_list = os.listdir(dir_list)
    print(imgdir_list)
    img_list = []
    for img in imgdir_list:
        imgdir = os.path.join(dir_list, img)
        print(imgdir)

        img_list.append(cv.imread(imgdir))

    return img_list