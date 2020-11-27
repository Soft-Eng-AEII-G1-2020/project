from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gridTop = QGridLayout()
        self.gridTop.setSpacing(10)
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setWindowTitle("Binary files converter")

        self.w = QWidget()
        self.vb = QVBoxLayout()

        self.setMenu()
        self.setGui()
        self.bindButtons()
        self.vb.addLayout(self.gridTop)
        self.vb.addLayout(self.grid)

        self.w.setLayout(self.vb)
        self.setCentralWidget(self.w)
        self.setFixedWidth(500)
        self.setFixedHeight(500)

    def setMenu(self):
        self.menu = self.menuBar()
        self.fileMenu = self.menu.addMenu("Menu")
        self.fileMenu.addAction('Exit \t Esc', self.close)
        self.shortcut_open = QShortcut(QKeySequence('Esc'), self)
        self.shortcut_open.activated.connect(self.close)

    def setGui(self):
        self.inText = QPlainTextEdit()
        self.outText = QPlainTextEdit()
        self.grid.addWidget(self.inText, 0, 0)
        self.grid.addWidget(self.outText, 0, 1)
        self.btnOne = QPushButton("Open File")
        self.btnMany = QPushButton("Open Many")
        self.btnSave = QPushButton("Save")
        self.btnConvert = QPushButton("Convert")
        self.btnReset = QPushButton("Reset")
        self.gridTop.addWidget(self.btnOne, 0, 0)
        self.gridTop.addWidget(self.btnMany, 0, 1)

    def step1Buttons(self):
        for i in reversed(range(self.grid.count())):
            self.gridTop.itemAt(i).widget().setParent(None)
        self.inText.setPlainText("")
        self.outText.setPlainText("")
        self.gridTop.addWidget(self.btnOne, 0, 0)
        self.gridTop.addWidget(self.btnMany, 0, 1)

    def step2Buttons(self):
        for i in reversed(range(self.grid.count())):
            self.gridTop.itemAt(i).widget().setParent(None)
        self.gridTop.addWidget(self.btnReset, 0, 0)
        self.gridTop.addWidget(self.btnConvert, 0, 1)

    def step3Buttons(self):
        for i in reversed(range(self.grid.count())):
            self.gridTop.itemAt(i).widget().setParent(None)
        self.gridTop.addWidget(self.btnReset, 0, 0)
        self.gridTop.addWidget(self.btnSave, 0, 1)

    def bindButtons(self):
        self.btnReset.clicked.connect(self.step1Buttons)
        self.btnSave.clicked.connect(self.saveAFile)
        self.btnConvert.clicked.connect(self.startProcesing)
        self.btnOne.clicked.connect(self.openAFile)

    def startProcesing(self):
        self.step3Buttons()
        self.outText.setPlainText(self.inText.toPlainText())

    def openAFile(self):
        self.fileName, selectedFilter = QFileDialog.getOpenFileName(
            self.w, "Select a binary file", "Initial file name", "text file (*.txt)")
        fileIn = open(self.fileName, "r")
        self.inText.setPlainText(fileIn.read())
        self.step2Buttons()

    def saveAFile(self):
        self.fileName, selectedFilter = QFileDialog.getSaveFileName(
            self.w, "Select a text file", "", "text file (*.txt)")
        fileOut = open(self.fileName, "w+")
        fileOut.write(self.outText.toPlainText())


app = QApplication([])
win = Window()
win.show()
app.exec_()
