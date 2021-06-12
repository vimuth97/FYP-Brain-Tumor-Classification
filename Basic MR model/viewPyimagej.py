# conda create -n pyimagej pyimagej openjdk=8

import imagej


ij = imagej.init()  # initialize imagej
print("initiated")
j_image = ij.io().open('C:/Users/user/Documents/FYP test images/origin.jpg')
print("opened")
image_j = ij.py.from_java(j_image)
ij.py.show(image_j, cmap='gray')
