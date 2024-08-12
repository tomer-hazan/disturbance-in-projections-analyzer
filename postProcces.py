import cv2
import numpy as np
from vimba import Vimba
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

import util

def find_defrances_in_given_image_set_and_make_video():
    frame_list = util.accuire_images_as_ndarrays(5,"images")
    dif_list = []
    scaller = 50
    for i in range(len(frame_list)):
        frame_list[i] = util.limits( frame_list[i])
        # cv2.imshow("frame " +str(i),frame_list[i])
    if (len(frame_list) > 1):  # subtracting adjacent frames to make a ndarray of the changes
        for i in range(len(frame_list) - 1):
            dif = util.getDifFrame(frame_list[i], frame_list[i+1], 0)*scaller
            dif_list.append(dif)
            cv2.imwrite("images/dif "+str(i)+".jpg", dif)
    # util.create_video_from_images_list(dif_list,"post procceses diffrances 30",1)
    cv2.waitKey(0)

def process():
    frame = util.accuire_images_as_ndarrays(1, "testMetirial")[0]
    sum_lines = [row.sum() for row in frame]
    plt.plot(sum_lines)
    plt.show()

def work_on_already_dif_images():
    dif_list = util.accuire_images_as_ndarrays(29,"testMetirial","dif")
    if (len(dif_list) > 1):  # subtracting adjacent frames to make a ndarray of the changes
        for i in range(len(dif_list)):
            dif = util.minLimit(dif_list[i],10)
            dif_list[i]=dif*30

    util.create_video_from_images_list(dif_list,"post procceses diffrances",1)
    # cv2.waitKey(0)
def main():
    find_defrances_in_given_image_set_and_make_video()
if __name__ == '__main__':
    main()