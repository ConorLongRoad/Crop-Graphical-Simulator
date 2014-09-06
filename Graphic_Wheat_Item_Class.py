from graphic_crop_item_class import *
from Wheat_Class import *

import Field_Resources

class WheatGraphicsPixmapItem(CropGraphicsPixmapItem):
    """This class provides a graphical representation of a wheat crop"""

    #Constructor
    def __init__(self):
        self.availableGraphics = [":/Wheat_Seed.png", ":/Wheat_Seedling.png",
                                  ":/Wheat_Young.png", ":/Wheat_Mature.png",
                                  ":/Wheat_Old.png"]
        super().__init__(self.availableGraphics)

        self.crop = Wheat()
