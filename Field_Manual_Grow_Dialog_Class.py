from PyQt4.QtGui import *

class ManualGrowDialog(QDialog):
    """This class creates a dialog to provide light, water and food values"""

    def __init__(self):
        super().__init__()

        #Create widgets
        self.waterSpinBox = QSpinBox
        self.lightSpinBox = QSpinBox
        self.foodSpinBox = QSpinBox()

        self.submitButton = QPushButton("Manually grow field")

        #Set-up spinboxes
        self.waterSpinBox.setRange(0, 10) #The range
        self.lightSpinBox.setRange(0, 10)
        self.foodSpinBox.setRange(0, 100)

        self.waterSpinBox.setSuffix(" Water") #The unchanging text at the end
        self.lightSpinBox.setSuffix(" Light")
        self.foodSpinBox.setSuffix(" Food")

        self.waterSpinBox.setValue(1) #Sets initial value
        self.lightSpinBox.setValue(1)
        self.foodSpinBox.setValue(1)

        #Create layout
        self.layout = QVBoxLayout()

        #Add widget to the layout
        self.layout.addWidget(self.lightSpinBox)
        self.layout.addWidget(self.waterSpinBox)
        self.layout.addWidget(self.foodSpinBox)
        self.layout.addWidget(self.submitButton)

        #Set the window layout
        self.setLayout(self.layout)

        #Connections
        self.submitButton.clicked.connect(self.close)

    def getValues(self):
        return self.lightSpinBox.value(), self.waterSpinBox.value(), self.foodSpinBox.value()
