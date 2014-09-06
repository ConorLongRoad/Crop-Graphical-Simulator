from graphic_field_item_class import *

class CropGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """This class provides a pixmap item with a present image for the crop"""

    #Constructor
    def __init__(self, graphicsList):
        super().__init__(graphicsList)

        self.crop = None

    def updateStatus(self):
        if self.crop._status == "Seed":
            self.setPixmap(QPixmap(self.availableGraphics[0]).scaleToWidth(25,1))
        elif self.crop._status == "Seedling":
            self.setPixmap(QPixmap(self.availableGraphics[1]).scaleToWidth(25,1))
        elif self.crop._status == "Young":
            self.setPixmap(QPixmap(self.availableGraphics[2]).scaleToWidth(25,1))
        elif self.crop._status == "Mature":
            self.setPixmap(QPixmap(self.availableGraphics[3]).scaleToWidth(25,1))
        elif self.crop._status == "Old":
            self.setPixmap(QPixmap(self.availableGraphics[4]).scaleToWidth(25,1))

    def grow(self, light, water):
        self.crop.grow(light, water)

    def report(self):
        return self.crop.report()

    def _harvestCrop(self):
        self.scene().harvestCrop(self)
        
    def contextMenuEvent(self, event):
        menu = QMenu("Crop")
        remove = menu.addAction("Harvest Crop")

        #Connection
        remove.triggered.connect(self._harvestCrop)

        #Run Menu
        menu.exec_(event.screenPos())
