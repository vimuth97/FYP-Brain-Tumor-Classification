from PIL import Image
import numpy

# im = Image.open('C:/Users/user/Documents/FYP test images/file_example_TIFF_10MB.tiff')
im = Image.open('C:/Users/user/Documents/FYP test images/test.tiff')
imarray = numpy.array(im)
imarray.shape
im.show()
