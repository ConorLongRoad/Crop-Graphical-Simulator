from PyQt4.QtGui import *

class FieldReportDialog(QDialog):
    """This class creates a report for the field"""

    #Constructor
    def __init__(self, report):
        super().__init__()
        self.setWindowTitle("Field Report")

        #Labels for the crop stats
        self.cropTypeLabel = QLabel("Crop Type")
        self.cropStatusLabel = QLabel("Crop Status")
        self.cropDaysGrowingLabel = QLabel("Days Growing")
        self.cropGrowthLabel = QLabel("Growth")

        #Labels for the animal stats
        self.animalTypeLabel = QLabel("Animal Type")
        self.animalStatusLabel = QLabel("Animal Status")
        self.animalDaysGrowingLabel = QLabel("Days Growing")
        self.animalWeightLabel = QLabel("Weight")

        #Labels for other cases
        self.noCropsLabel = QLabel("There are no crops in this field")
        self.noAnimalsLabel = QLabel("There are no animals in this field")
        self.nothingLabel = QLabel("The field is empty")

        self.closeButton = QPushButton("Dismiss Report")

        #Layout
        self.reportLayout = QGridLayout()
        self.layout = QVBoxLayout()

        row = 1

        if len(report["Crops"]) == 0 and len(report["Animals"]) == 0:
            self.reportLayout.addWidget(self.nothingLabel, 0, 0)
        else:
            if len(report["Crops"]) > 0:
                self.reportLayout.addWidget(self.cropTypeLabel, 0, 0)
                self.reportLayout.addWidget(self.cropStatusLabel, 0, 1)
                self.reportLayout.addWidget(self.cropDaysGrowingLabel, 0, 2)
                self.reportLayout.addWidget(self.cropGrowthLabel, 0, 3)
                #Create crop report details
                for crop in report["Crops"]:
                    self.reportLayout.addWidget(QLabel(str(crop["Type"])), row, 0)
                    self.reportLayout.addWidget(QLabel(str(crop["Status"])), row, 1)
                    self.reportLayout.addWidget(QLabel(str(crop["Days growing"])), row, 2)
                    self.reportLayout.addWidget(QLabel(str(crop["Growth"])), row, 3)
                    row += 1
            else:
                self.reportLayout.addWidget(self.noCropsLabel, 0, 0)
            if len(report["Animals"]) > 0:
                self.reportLayout.addWidget(self.animalTypeLabel, row, 0)
                self.reportLayout.addWidget(self.animalStatusLabel, row, 1)
                self.reportLayout.addWidget(self.animalDaysGrowingLabel, row, 2)
                self.reportLayout.addWidget(self.animalWeightLabel, row, 3)
                row += 1
                for animal in report ["Animals"]:
                    self.reportLayout.addWidget(QLabel(str(animal["Type"])), row, 0)
                    self.reportLayout.addWidget(QLabel(str(animal["Status"])), row, 1)
                    self.reportLayout.addWidget(QLabel(str(animal["Days growing"])), row, 2)
                    self.reportLayout.addWidget(QLabel(str(animal["Weight"])), row, 3)
                    row += 1
            else:
                self.reportLayout.addWidget(self.noAnimalsLabel, row, 0)

        self.layout.addLayout(self.reportLayout)
        self.layout.addWidget(self.closeButton)
        self.setLayout(self.layout)

        #Connections
        self.closeButton.clicked.connect(self.close)
