from skimage.external.tifffile import TiffFile
from hillshade import hill_shade
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import ndimage

def calculateDist(array):
    distance = ndimage.distance_transform_edt(array)
    # distance[(distance < 1) | (distance > 3)] = 0
    # distance[(distance >= 1) & (distance <= 3)] = 1
    distance[distance != 1] = 0
    dist = np.ma.masked_where(distance == 0, distance)
    return dist

def visual(background, img_path, interval, iterations):
    rgb = hill_shade(bk_img)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.imshow(rgb)
    plt.pause(1)

    layer = None

    for iter in range(1, iterations+1):
        img_files = os.listdir(img_path)
        if iter % 2 == 0:
            img_files = reversed(img_files)
            layer.remove()
        elif iter > 1 and iter % 2 == 1:
            # layer.remove()
            # plt.clf()
            plt.imshow(rgb)
            plt.pause(1)
            # plt.show()

        for i, img in enumerate(img_files):
            print(img)
            # layer.remove()
            if i>0 :
                layer.remove()
                print("remove {}".format(img))
            # elif i == 0 and iter % 2 == 0:
            #     plt.imshow(rgb)
            img_file= os.path.join(img_path, img)
            with TiffFile(img_file) as tif:
                img_arr = tif.asarray()
            img_arr = np.ma.masked_where(img_arr == 0, img_arr)
            layer = plt.imshow(img_arr,alpha=.5)
            plt.pause(interval)


    return True


if __name__ == '__main__':

    in_file = "../../data/dem_full.tif"
    images = r"C:\temp\ppr\flood"

    with TiffFile(in_file) as tif:
        bk_img = tif.asarray()

    interval = 0.00011

    visual(bk_img,images, interval, 50)
    plt.show()