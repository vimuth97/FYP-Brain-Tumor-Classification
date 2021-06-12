import os
import nibabel as nib
import matplotlib.pyplot as plt
import pandas as pd
import torch
import numpy

# rootdir = "C:/Users/user/Documents/FYP test images/miccai2020-data.eastus.cloudapp.azure.com/CPM-RadPath_2020_Training_Data/Radiology"
rootdir = "C:/Users/user/Documents/FYP test images/test1"
cases = {}


def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slc in enumerate(slices):
        axes[i].imshow(slc.T, cmap="gray", origin="lower")


def read_label(labels, id):
    for index, data in labels.iterrows():
        if (data['CPM_RadPath_2019_ID']) == id:
            if data['class'] == 'G':
                return 0
            if data['class'] == 'A':
                return 1
            else:
                return 2


def read_mri():
    for subdir, dirs, files in os.walk(rootdir):
        if len(subdir.split('\\')) == 1:
            continue
        else:
            cases[subdir.split('\\')[-1]] = []
            for file in files:
                fileName = os.path.join(rootdir, subdir, file)
                img = nib.load(fileName)
                img = img.get_fdata()  # change to numpy
                # print(img.shape)
                cases[subdir.split('\\')[-1]].append(img)

    # imgDisplay = cases['1'][0]
    # slice_0 = imgDisplay[120, :, :]
    # slice_1 = imgDisplay[:, 120, :]
    # slice_2 = imgDisplay[:, :, 78]
    # show_slices([slice_0, slice_1, slice_2])
    # plt.suptitle("3D MR Image")
    # plt.show()
    print(len(cases))

    labels = pd.read_csv('training_data_classification_labels.csv')
    labeled_data = []

    for case in cases:
        single_np = numpy.stack(cases[case], axis=0)
        labeled_data.append((torch.from_numpy(single_np).float(), read_label(labels, case)))

    return labeled_data
