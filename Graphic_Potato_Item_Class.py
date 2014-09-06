from graphic_crop_item_class import *
from Potato_Class import *

import Field_Resources

class PotatoGraphicsPixmapItem(CropGraphicsPixmapItem):
    """This class provides a graphical representation of a potato crop"""

    #Constructor
    def __init__(self):
        self.availableGraphics = [":/Potato_Seed.png", ":/Potato_Seedling.png",
                                  ":/Potato_Young.png", ":/Potato_Mature.png",
                                  ":/Potato_Old.png"]
        super().__init__(self.availableGraphics)

        self.crop = Potato()
