from PIL import Image
import numpy as np

def read_image(path):
    '''
        Reads image from file and converts it into numpy array in greyscale
    '''
    img = Image.open(path).convert('L') 
    img_array = np.asarray(img)
    return img_array.flatten(), img_array.shape

