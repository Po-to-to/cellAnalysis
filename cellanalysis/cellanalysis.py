# +
from skimage import io # conda install scikit-image
from aicsimageio import AICSImage  # pip install aicsimageio és pip install aicspylibczi
from pathlib import Path
import matplotlib.pyplot as plt


class Image:
    """basic image class which stores the image metadata:
            - image location
            - image type
            - channel info
            - etc."""

    def __init__(self, file_path: str):
        # or __post_init__
        # definiáljuk a self.image_path paramétert!
        # self.channel_number
        # self.nucleus_channel 
        self.image_path = Path(file_path)

        self.ext = self.image_path.suffix
        if self.ext not in ['.tif', '.czi']:
            raise ValueError(f"Extention '{self.ext}' is not supported!")

    def load_image(self):
        """loads the image data and stores it in self.image"""
        if self.ext == '.tif':
            self.image = io.imread(self.image_path)
        elif self.ext == '.czi':
            aics_image = AICSImage(self.image_path)
            self.image = aics_image.get_image_data('YX')
        

    def display_image(self):
        """displays the image channels on a pyplot figure"""
        plt.imshow(self.image, cmap='gray')
        plt.show()


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
        pass

    def analyse_experiment(self):
        pass

    def display_cells(self, cellIds):
        """displays a collection of cells by IDs in a single plot
            
            Useful for checking a collection a cells with same properties (e.g. size, fluorescence, etc.)"""
        pass
