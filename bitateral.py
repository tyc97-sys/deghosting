# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 20:17:41 2021

@author: Jay
"""



import numpy as np
import cv2
import math    


def read_data(directory_name, arr, mode, numOfpicture):
    for i in range (numOfpicture):
        img = cv2.imread(directory_name + "/" + str(i+1) + ".jpg", mode)
        arr.append(img)
        
def store_dataMulti(directory_name, arr, numOfpicture):
    for i in range (numOfpicture):
        cv2.imwrite("./" + directory_name + "/" + str(i+1) + ".jpg", arr[i])

        
def store_dataSingle(src, directory_name, storePicturename):
    cv2.imwrite("./" + directory_name + "/" + str(storePicturename) + ".jpg", src)        
    #cv2.imwrite("./HDR1/gamma.jpg", gamma)

def distance(x, y, i, j):
    """
    :input x:
    :input y:
    :input i:
    :input j:
    :return:
    """
    return np.sqrt((x-i)**2 + (y-j)**2)

def gaussian(x, sigma):
    """
    :input x:
    :param sigma:
    :return:
    """
    return (1.0 / (2 * math.pi * (sigma ** 2))) * math.exp(- (x ** 2) / (2 * sigma ** 2))

def apply_bilateral_filter(source, filtered_image, x, y, diameter, sigma_i, sigma_s):
    """
    :input source:
    :input filtered_image:
    :input x:
    :input y:
    :param diameter:   
    :param sigma_i:
    :param sigma_s:
    :return:
    """
    hl = diameter/2
    i_filtered = 0
    Wp = 0
    i = 0
    
    while i < diameter:
        j = 0
        while j < diameter:
            neighbour_x = x - (hl - i)
            neighbour_y = y - (hl - j)
            if neighbour_x >= len(source):
                neighbour_x -= len(source)
            if neighbour_y >= len(source[0]):
                neighbour_y -= len(source[0])
            gi = gaussian(int(source[int(neighbour_x)][int(neighbour_y)]) - int(source[x][y]), sigma_i)
            gs = gaussian(distance(neighbour_x, neighbour_y, x, y), sigma_s)
            w = gi * gs
            i_filtered += source[int(neighbour_x)][int(neighbour_y)] * w
            Wp += w
            j += 1
        i += 1
    i_filtered = i_filtered / Wp
    filtered_image[x][y] = int(round(i_filtered))

def bilateral_filter_own(sourceList, filter_diameter, sigma_i, sigma_s):
    """
    FUNCTION: bilateral_filter_own
        Call to filter the images with bilateral filter
    INPUTS:
        sourceList
    PARAM:           
        filter_diameter = filter diameter   
        sigma_i = standard deviation of domain range
        sigma_s = standard deviation of spatial
    OUTPUTS:   
        filtered image
    """
    for k in range (len(sourceList)):
        source = sourceList[k]
        filtered_image = np.zeros(source.shape)
        i = 0
        while i < len(source):
            j = 0
            while j < len(source[0]):
                apply_bilateral_filter(source, filtered_image, i, j, filter_diameter, sigma_i, sigma_s)
                j += 1
            i += 1
        sourceList[k] = filtered_image
        print("No.{} is finished".format(k+1))

def bilateralFilterFromCv2(imageList, Diameter, sigmaColor, sigmaSpace):#call cv2 func
    for i in range (len(imageList)):
        imageList[i] = cv2.bilateralFilter(imageList[i], Diameter, sigmaColor, sigmaSpace)
        


def gamma_correction(imgList, c=1, g=1.5):
    """
    FUNCTION: gamma_correction
        Call to deal with images with gamma correction
    INPUTS: 
        imgList
    PARAM:
        c = average gray level in paper (2), the default is 1
        g = parameter, the default is 1.5
    OUTPUTS:
        gamma correction image.
    """
    for i in range (len(imgList)):
        out = imgList[i].copy()
        out = out.astype(np.float32)
        out /= 255.
        out = (1/c * out) ** (1/g)
        out *= 255
        imgList[i] = out.astype(np.uint8)
        



'''
if __name__ == "__main__":
    
    #/*---------------------------------test for bilateral-----------------------------------
    
    Picturelist = []
    numOfpic = 6
    read_data("HDR0", Picturelist, 0, numOfpic)
    bilateral_filter_own(Picturelist, 5, 60.0, 60.0)
    #bilateralFilterFromCv2(Picturelist, 5, 60.0, 60.0)
    store_dataMulti("HDR2", Picturelist, numOfpic)
    
    #/*---------------------------------test for gamma-----------------------------------

    Picturelist = []
    numOfpic = 6
    read_data("HDR0", Picturelist, 1, numOfpic)
    gamma_correction(Picturelist, 1, 1/2.5)
    store_dataMulti("HDR1", Picturelist, numOfpic)

    
'''


