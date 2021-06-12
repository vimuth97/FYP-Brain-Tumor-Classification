# conda install -c conda-forge tifffile
# conda install -c anaconda imagecodecs
# conda install -c conda-forge opencv
# pyimagej env

import tifffile as tf
import cv2


# image = tf.imread('C:/Users/user/Documents/FYP test images/file_example_TIFF_10MB.tiff')
image = tf.imread('C:/Users/user/Documents/FYP test images/test.tiff', key=0)


matrix = image[:, :, :]
print(matrix)
print(image.shape)
print(image.size)

cv2.imshow("Grey_image", image)  # view the image in a window
cv2.waitKey(0)
cv2.destroyAllWindows()
