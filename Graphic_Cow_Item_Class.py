from graphic_animal_item_class import *
from Cow_Class import *

import field_Resources

class CowGraphcisPixmapItem(AnimalGraphicsPixmapItem):
    """This class provides a graphical representation of a cow"""

    #Constructor
    def __init__(self):
        self.availableGraphics = [":/Cow_Baby.png", ":/Cow_Poor.png",
                                  ":/Cow_Fine.png", ":/Cow_Prime.png"]

        super().__init__(self.avaibleGraphics)

        self.animal = Cow("")
