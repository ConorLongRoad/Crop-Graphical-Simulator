from graphic_field_item_class import *

class AnimalGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """This class provides a pixmap item with a present image for the animal"""

    #Constructor
    def __init__(self, graphicsList):
        super().__init__(graphicsList)

        self.animal = None

    def updateStatus(self):
        if self.animal._status == "Baby":
            self.setPixmap(QPixmap(self.availableGraphics[0]).scaleToWidth(25,1))
        elif self.animal._status == "Poor":
            self.setPixmap(QPixmap(self.availableGraphics[1]).scaleToWidth(25,1))
        elif self.animal._status == "Fine":
            self.setPixmap(QPixmap(self.availableGraphics[2]).scaleToWidth(25,1))
        elif self.animal._status == "Prime":
            self.setPixmap(QPixmap(self.availableGraphics[3]).scaleToWidth(25,1))

    def needs(self):
        return self.animal.needs()

    def grow(self, feed, water):
        self,animal.grow(feed, water)

    def report(self):
        self.animal.report()

    def _removeAnimal(self):
        self.scene().removeAnimal(self)

    def contextMenuEvent(self, event):
        menu = QMenu("Animal")
        remove = menu.Action("Remove Animal")

        #Connection
        remove.triggered.connect(self._removeAnimal)

        #Run menu
        menu.exec_(event.screenPos())
