# +
from skimage import io # conda install scikit-image
from aicsimageio import AICSImage  # pip install aicsimageio és pip install aicspylibczi


class Image:
    """basic image class which stores the image metadata:
            - image location
            - image type
            - channel info
            - etc."""

    def __init__(self,path):
	self.image_path = path
        # or __post_init__
        # definiáljuk a self.image_path paramétert!
        # self.channel_number
        # self.nucleus_channel 

    def load_image(self):
	 if ".tif" in self.image_path:
            self.image = io.imread(self.image_path)
        elif ".czi" in self.image_path:
            self.image = AICSImage(self.image_path)

	 """loads the image data and stores it in self.image"""
        
        # io.imread funkció vagy AICSImage(path)
        # használjuk a self.image_path paramétert!
        

    def display_image(self):
	plt.imshow(self.image)
	
        """displays the image channels on a pyplot figure"""
        


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
