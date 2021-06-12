# conda install -c conda-forge nibabel

import nibabel as nib
import os


file = os.path.join("C:/Users/user/Documents/FYP test images", 'test.nii.gz')
img = nib.load(file)  # LOAD .nii IMAGE
print(img.shape)
