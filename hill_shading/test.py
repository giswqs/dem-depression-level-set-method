from skimage.external.tifffile import TiffFile
from hillshade import hill_shade
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import ndimage

# in_file = "../../data/sink_full.tif"
# images = r"C:\temp\ppr\flood"
#
# with TiffFile(in_file) as tif:
#     bk_img = tif.asarray()
# bk_img[bk_img < 0] = 0
#
# print(np.max(bk_img))
# print(np.min(bk_img))
#
# rgb = hill_shade(bk_img)
# plt.imshow(rgb)
# plt.show()

def calculateDist(array):
    distance = ndimage.distance_transform_edt(array)
    distance[(distance < 1) | (distance > 3)] = 0
    distance[(distance >= 1) & (distance <= 3)] = 1
    # distance[distance != 1] = 0
    dist = np.ma.masked_where(distance == 0, distance)
    return dist

def visual(background, img_path, interval):
    plt.figure()
    fig = plt.gcf()
    fig.clf()
    ax1 = fig.add_subplot(1,2,1)
    rgb = hill_shade(bk_img)
    ax1.imshow(rgb)

    ax2 = fig.add_subplot(1,2,2)
    ax_u = ax2.imshow(rgb)
    plt.pause(1)

    # bnd = None
    left = None
    right = None
    img_files = os.listdir(img_path)
    img_files = reversed(img_files)
    for i, img in enumerate(img_files):
        print(img)
        if i>0:
            # del ax1.collections[0]
            left.remove()
            right.remove()
        img_file= os.path.join(img_path, img)
        with TiffFile(img_file) as tif:
            img_arr = tif.asarray()
            # img_arr[img_arr == 0] = np.NaN

        dist = calculateDist(img_arr)
        img_arr = np.ma.masked_where(img_arr == 0, img_arr)
        # del ax1.collections[0]
        # ax_u.set_data(img_arr)
        # ax1.contour(dist)
        left = ax2.imshow(dist, cmap = "binary")
        # ax_u.set_data(img_arr)
        right = ax1.imshow(img_arr,alpha=.5)
        # ax2.imshow(img_arr)
        fig.canvas.draw()

        # bnd.remove()
        plt.pause(interval)
    return True


if __name__ == '__main__':

    in_file = "../../data/dem_full.tif"
    images = r"C:\temp\ppr\flood"

    with TiffFile(in_file) as tif:
        bk_img = tif.asarray()

    interval = 0.00011
    visual(bk_img,images, interval)
    plt.show()