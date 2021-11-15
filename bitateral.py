# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 20:17:41 2021

@author: Jay
"""



import numpy as np
import cv2

import math    
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

def bilateral_filter_own(source, filter_diameter, sigma_i, sigma_s):
    """
    FUNCTION: bilateral_filter_own
        Call to filter the images with bilateral filter
    INPUTS:
        source = image
    PARAM:           
        filter_diameter = filter diameter   
        sigma_i = standard deviation of domain range
        sigma_s = standard deviation of spatial
    OUTPUTS:   
        filtered image
    """
    filtered_image = np.zeros(source.shape)
    i = 0
    while i < len(source):
        j = 0
        while j < len(source[0]):
            apply_bilateral_filter(source, filtered_image, i, j, filter_diameter, sigma_i, sigma_s)
            j += 1
        i += 1
    return filtered_image

def bilateralFilterFromCv2(image, Diameter, sigmaColor, sigmaSpace):#call cv2 func
    return cv2.bilateralFilter(image, Diameter, sigmaColor, sigmaSpace)


def gamma_correction(img, c=1, g=1.5):
    """
    FUNCTION: gamma_correction
        Call to deal with images with gamma correction
    INPUTS: 
        img = image
    PARAM:
        c = parameter, the default is 1
        g = parameter, the default is 1.5
    OUTPUTS:
        gamma correction image.
    """
    return np.power(img/float(np.max(img)),g)


'''
if __name__ == "__main__":

    src = cv2.imread('dog_old.jpg',0)
    filtered_image_func = bilateralFilterFromCv2(src, 5, 60.0, 60.0)
    filtered_image_own  = bilateral_filter_own(src, 5, 60.0, 60.0)

    cv2.imwrite("filtered_image_own.jpg", filtered_image_own)
    image = cv2.imread("filtered_image_own.jpg",0)
    
    cv2.imshow("filtered_image_func.jpg", filtered_image_func)
    cv2.imshow("filtered_image_own.jpg", image)
    cv2.imshow("src.jpg", src)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #/*---------------------------------test for gamma-----------------------------------

    src = cv2.imread('dog_old.jpg',1)
    gamma = gamma_correction(src)
    cv2.imwrite("gamma.jpg", gamma)
    image = cv2.imread("gamma.jpg",1)
    cv2.imshow("gamma.jpg", gamma)
    cv2.imshow("src.jpg", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''





