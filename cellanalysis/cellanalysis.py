# +
from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
from skimage import io # conda install scikit-image
from aicsimageio import AICSImage  # pip install aicsimageio és pip install aicspylibczi
from pathlib import Path
import matplotlib.pyplot as plt
from os import listdir
import numpy as np


class Image:
    """basic image class which stores the image metadata:
            - image location
            - image type
            - channel info
            - etc."""

    def __init__(self, image_path):
        # or __post_init__
        # self.channel_number
        # self.nucleus_channel 
        self.image_path = Path(image_path)
        
        
    def display_image(self):
        """displays the image channels on a pyplot figure"""
        plt.imshow(self.image/self.image.max(), cmap='gray') #https://forum.image.sc/t/display-multi-channel-images-with-scikit-image/51009
        plt.show()
        
    def set_background(self,):
        """int or array"""
        pass

    def subtract_background(self):
        pass

    
    
class ZeissCziImage(Image):
    """built to load .czi images"""
    
    def __init__(self, path):
        super().__init__(path)
        self.ext = self.image_path.suffix
        if self.ext not in ['.czi']:
            print(f"Extention '{self.ext}' is not supported!")
     
    def load_image(self):
        aics_image = AICSImage(self.image_path)
        self.image = aics_image.get_image_data('YXZ')

        
        
class ImageXpressImage(Image):
    """built to load .tif images"""
    
    def __init__(self, folder, well, pos):
        self.well = well
        self.pos = pos
        super().__init__(folder)   
                    
            
    def load_image(self):
        imgs = listdir(self.image_path)
        imgs = [im for im in imgs if f"_{self.well}_" in im] # list comprehension
        imgs = [im for im in imgs if f"_{self.pos}" in im]
        imgs = [im for im in imgs if f"_thumb" not in im]
        imgs = [io.imread(f"{self.image_path}/{im}") for im in imgs]
        imgs = [im.reshape(im.shape[0], im.shape[1], 1) for im in imgs]
        self.image = np.concatenate(imgs, axis=2)

# -

class CellDetector:
    """class with cell and nucleus detecting methods and detector specific attributes"""
    
    def __init__(self):
        # or __post_init__
        pass

    def predict_cells(self):
        pass

    def predict_nuclei(self):
        pass

class Experiment:
    """top class of the package"""

    def __init__(self):
        pass

    def get_images(self):
        """collects all the images belonging to the experiment (Image classes)"""
        ## should create a list/dictionary/tuple of images
        # img.load_image()
        pass

    def analyse_experiment(self):

        pass

    def display_cells(self, cellIds):
        """displays a collection of cells by IDs in a single plot
            
            Useful for checking a collection a cells with same properties (e.g. size, fluorescence, etc.)"""
        pass
