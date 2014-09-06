from PyQt4.QtGui import *
from PyQt4.QtCore import *

import Field_Resources

class QDragLabel(QLabel):
    """This class provides an image label that can be dragged and dropped"""

    #Constructor
    def __init__(self, picture):
        super().__init__()
        self.setPixmap(picture.scaledToWidth(35,1))
        self.mimetext = None

    def mouseMoveEvent(self, event):
        #If the left mouse button is used
        if event.buttons() == Qt.LeftButton:
            data = QByteArray() #Create a QBiteArray. we don'
            mimeData = QMimeData() #Tells us which label is being dragged and dropped
            mimeData.setData(self.mimetext, data) #Passes in 2 values

            drag = QDrag(self) #Set up drag itself
            drag.setMimeData(mimeData) #Set the data for the drag
            drag.setHotSpot(self.rect().topLeft()) #Where am I dragging from

            dropAction = dragstart(Qt.MoveAction) #Drag starts

class WheatDragLabel(QDragLabel):
    """This class provides a wheat label that can be dragged and dropped"""
    def __init__(self):
        super().__init(QPixmap(":/Wheat_Seed.png"))
        self.mimeText = "application/x-wheat"

class PotatoDragLabel(QDragLabel):
    """This class provides a potato label that can be dragged and dropped"""
    def __init__(self):
        super().__init(QPixmap(":/Potato_Seed.png"))
        self.mimeText = "application/x-potato"

class CowDragLabel(QDragLabel):
    """This class provides a cow label that can be dragged and dropped"""
    def __init__(self):
        super().__init(QPixmap(":/Cow_Baby.png"))
        self.mimeText = "application/x-cow"

class SheepDragLabel(QDragLabel):
    """This class provides a sheep label that can be dragged and dropped"""
    def __init__(self):
        super().__init(QPixmap(":/Sheep_Baby.png"))
        self.mimeText = "application/x-sheep"
