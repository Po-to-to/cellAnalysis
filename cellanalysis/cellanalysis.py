# +
from skimage import io # conda install scikit-image
from aicsimageio import AICSImage # pip install aicsimageio és pip install aicspylibczi


class Image:
    """basic image class which stores the image metadata:
            - image location (path)
            - image type 
            - channel info (chn_no: number of channels; nucl_chn: nucleus channel)
            - etc."""

    def __init__(self, path):
        # or __post_init__
        # definiáljuk a self.image_path paramétert!
        self.image_path = path
        #self.channel_number = chn_no
        #self.nucleus_channel = nucl_chn 

    def load_image(self):
        """loads the image data and stores it in self.image"""
        
        self.image = io.imread_collection(load_pattern = self.image_path)
        
        #self.image = 
        
        # io.imread funkció vagy AICSImage(path)
        # használjuk a self.image_path paramétert!
        

    def display_image(self):
        """displays the image channels on a pyplot figure"""
        
        fig = io.imshow_collection(self.image)
        
        
        #pass


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
