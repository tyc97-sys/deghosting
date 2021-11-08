import cv2 as cv
import numpy as np

'''Contrast measure'''


def Contrast_Measure(img_list):
    # We apply a Laplacian filter to the grayscale version of each image, and take the absolute value of the filter response.
    laplacian_filter = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]], dtype='float64')

    img_laplacian = []
    for img in img_list:
        img_laplacian.append(abs(cv.filter2D(img, -1, laplacian_filter)))

    return img_laplacian


def Saturation_Measure(img_list):
    # Standard deviation within the R, G and B channel.

    img_saturation = []
    for img in img_list:
        B = img[:, :, 0]
        G = img[:, :, 1]
        R = img[:, :, 2]

        mu = (B + G + R) / 3
        saturation = ((B - mu) ** 2 + (G - mu) ** 2 + (R - mu) ** 2) ** 0.5
        img_saturation.append(saturation)

    return img_saturation


def Well_Exposure_Measure(img_list):
    img_well_exposure = []
    sigma = 0.2
    for img in img_list:
        B = img[:, :, 0]
        G = img[:, :, 1]
        R = img[:, :, 2]

        B_Gaussian = np.exp(-0.5 * (((B - 0.5) ** 2) / (2 * (sigma) ** 2)))
        G_Gaussian = np.exp(-0.5 * ((G - 0.5) ** 2) / (2 * (sigma) ** 2))
        R_Gaussian = np.exp(-0.5 * ((R - 0.5) ** 2) / (2 * (sigma) ** 2))

        well_exposure = B_Gaussian * G_Gaussian * R_Gaussian

        img_well_exposure.append(well_exposure)

    return img_well_exposure


def Creat_Weight_Map(C, S, E):
    img_weight_map = []

    for c, s, e in zip(C, S, E):
        weight_map = c * s * e
        img_weight_map.append(weight_map)

    return img_weight_map