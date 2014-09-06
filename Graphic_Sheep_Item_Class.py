from graphic_animal_item_class import *
from Sheep_Class import *

import field_Resources

class SheepGraphcisPixmapItem(AnimalGraphicsPixmapItem):
    """This class provides a graphical representation of a sheep"""

    #Constructor
    def __init__(self):
        self.availableGraphics = [":/Sheep_Baby.png", ":/Sheep_Poor.png",
                                  ":/Sheep_Fine.png", ":/Sheep_Prime.png"]

        super().__init__(self.avaibleGraphics)

        self.animal = Sheep("")
