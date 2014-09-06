from PyQt4.QtGui import *

from Field_Class import *
from Graphic_Wheat_Item_Class import *
from Graphic_Potato_Item_Class import *
from Graphic_Cow_Item_Class import *
from Graphic_Sheep_Item_Class import *

import Field_Resources

class FieldGraphicsScene(QGraphicsScene):
    """This class provides a scene to manage the items in the field"""

    #Constructor
    def __init__(self, maxCrops, maxAnimals):
        super().__init__()

        self.field = Field(maxCrops, maxAnimals)

        self.backgroundBrush = QBrush()
        self.backgroundPicture = QPixmap(":/Field_Background.png")
        self.backgroundBrush.setTexture(self.backgroundPicture)
        self.setBackgroundBrush(self.backgroundBrush)

    def harvestCrop(self, cropToHarvest):
        position = self.field._crops.index(cropToHarvest) #Finds the right crop
        self.field.harvestCrop(position) #Remove crop data from field
        self.removeItem(cropToHarvest) #Remove crop graphics from field

    def removeAnimal(self, animalToRemove):
        position = self.field._animals.index(animalToRemove) #Finds the right animal
        self.field.removeAnimal(position) #Remove animal data from field
        self.removeItem(animalToRemove) #Remove animal graphics from field

    def reportContents(self):
        return self.field.reportContents()

    def updateStatus(self):
        for each in self.field._crops:
            each.updateStatus()
        for each in self.field._animals:
            each.updateStatus()
        
    def _dropPosition(self, item):
        cursorPosition = QCursor.pos() #Gets global cursor position
        currentView = self.views()[0]
        scenePosition = currentView.mapFromGlobal(cursorPosition)

        width = item.boundingRect().width() #Gets mouse width position
        height = item.boundingRect().height() #Gets mouse height position

        widthOffset = width/2
        heightOffset = height/2

        dropX = scenePosition.x() - widthOffset
        dropY = scenePosition.y() - heightOffset

        return dropX, dropY

    def _visualiseGraphicItem(self, graphicItemType):
        if graphicItemType == "Crop":
            x, y = self._dropPosition(self.field._crops[-1])
            self.field._crops[-1].setPos(x, y)
            self.addItem(self.field._crops[-1])
            
        elif graphicItemType == "Animal":
            x, y = self._dropPosition(self.field._animals[-1])
            self.field._animals[-1].setPos(x, y)
            self.addItem(self.field._animals[-1])

    def _addGraphicItem(self, result, graphicItemType):
        if result:
            self._visualiseGraphicItem(graphicItemType)
        else:
            errorMessage = QMessageBox()
            errorMessage.setText("No more {0}s can be added to this field".format(graphicItemType))
            errorMessage.exec()

    #This methods over-rides the parent method
    def dragEnterEvent(self, event):
        #What to do if an object is dragged into scene
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        event.accept()

        #What to do if an object is dropped on the scene
        if event.mimeData().hasFormat("application/x-wheat"):
            cropAdded = self.field.plantCrop(WheatGraphicsPixmapItem())
            self._addGraphicItem(cropAdded, "Crop")
        elif event.mimeData().hasFormat("application/x-potato"):
            cropAdded = self.field.plantCrop(PotatoGraphicsPixmapItem())
            self._addGraphicItem(cropAdded, "Crop")
        elif event.mimeData().hasFormat("application/x-cow"):
            animalAdded = self.field.addAnimal(CowGraphicsPixmapItem())
            self._addGraphicItem(animalAdded, "Animal")
        elif event.mimeData().hasFormat("application/x-sheep"):
            animalAdded = self.field.addAnimal(SheepGraphicsPixmapItem())
            self._addGraphicItem(animalAdded, "Animal")
