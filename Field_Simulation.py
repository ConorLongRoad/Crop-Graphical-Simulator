import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Graphic_Field_Scene_Class import *
from Graphic_Wheat_Item_Class import *
from Graphic_Potato_Item_Class import *
from Graphic_Sheep_Item_Class import *
from Graphic_Cow_Item_Class import *
from Graphic_Drag_Label_Class import *
from Field_Manually_Grow_Dialog_Class import *
from Field_Report_Dialog_Class import *

class FieldWindow(QMainWindow):
    """This class creates a main window to observe the growth of a simulated field"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Field Simulation")

        #Create toolbars
        self.cropToolBar = QToolBar()
        self.animalToolBar = QToolBar()

        #Create toolbar labels
        self.wheatLabel = WheatDragLabel()
        self.wheatLabel.setToolTip("Add Wheat")

        self.potatoLabel = PototoDragLabel()
        self.potatoLabel.setToolTip("Add Potato")

        self.cowLabel = CowDragLabel()
        self.cowLabel.setToolTip("Add Cow")

        self.sheepLabel = SheepDragLabel()
        self.sheepLabel.setToolTip("Add Sheep")

        #Add labels to toolbars
        self.cropToolBar.addWidget(self.wheatLabel)
        self.cropToolBar.addWidget(self.potatoLabel)

        self.animalToolBar.addWidget(self.cowLabel)
        self.animalToolBar.addWidget(self.sheepLabel)

        #Add toolbars to window
        self.addToolBar(self.cropToolBar)
        self.addToolBar(self.animalToolBar)

        #Task 5------------------------
        self.fieldGraphicsView = QGraphicsView()
        self.fieldGraphicsView.setScene(FieldGraphicsScene(1,5))

        self.fieldGraphicsView.setFixedHeight(400)
        self.fieldGraphicsView.setFixWidth(400)
        self.fieldGraphicsView.setSceneRect(0,0,400,400)
        self.fieldGraphicsView.setHorizontalScrollBarPolicy(1) #No scroll bars
        self.fieldGraphicsView.setVerticalScrollBarPolicy(1) #No scroll bars

        self.fieldReportButton = QPushButton("Field Report")
        self.fieldAutomaticGrowButton = QPushButton ("Automatically Grow Field")
        self.fieldManualGrowButton = QPushButton("Manually Grow Field")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.fieldGraphicsView)
        self.layout.addWidget(self.fieldReportButton)
        self.layout.addWidget(self.fieldAutomaticGrowButton)
        self.layout.addWidget(self.fieldManualGrowButton)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.Layout)
        self.setCentralWidget(self.mainWidget)

        #Task 5 end-----------------

        #Connections
        self.fieldAutomaticGrowButton.clicked.connect(self.automaticallyGrow)
        self.fieldManualGrowButton.clicked.connect(self.manuallyGrow)
        self.fieldReportButton.clicked.connect(self.report)

    def automaticallyGrow(self):
        for days in range(30):
            light = random.randint(1,10)
            water = random.randint(1,10)
            food = random.randint(1,100)
            self.fieldGraphicsView.scene().field.grow(light, food, water)
        self.fieldGraphicsView.scene().updateStatus()

    def manuallyGrow(self):
        dialog = ManualGrowDialog()
        dialog.exec_()
        light, water, food = dialog.getValues()
        self.fieldGraphicsView.scene().field.grow(light, food, water)
        self.fieldGraphicsView.scene().updateStatus()

    def report(self):
        currentReport = self.fieldGraphicsView.scene().fieldReportContents()
        reportDialog = FieldReportDialog(currentReport)
        reportDialog.exec_()

def main():
    Field_Simulation = QApplication(sys.argv) #Create new application
    Field_Window = FieldWindow() #Create new instance of main window
    Field_Window.show() #Make instance visible
    Field_Window.raise_() #Raise Instance to top of window stack
    Field_Simulation.exec_() #Monitor application for events

if __name__ == "__main__":
    main()
