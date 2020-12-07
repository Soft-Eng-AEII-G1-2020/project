import file_management
import binary_conversion
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow,QRadioButton, QScrollArea, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QShortcut, QPlainTextEdit, QPushButton, QFileDialog, QApplication
from PyQt5.QtCore import Qt, QSize


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.tableOfOuts = []
        self.gridTop = QGridLayout()
        self.gridTop.setSpacing(10)
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setWindowTitle("Binary files converter")
        self.binaryFileIsLinear = 1
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

        self.binfile = file_management.BinFile()
        self.binConverter = binary_conversion.BinConverter()

    def setMenu(self):
        self.menu = self.menuBar()
        self.fileMenu = self.menu.addMenu("Menu")
        self.fileMenu.addAction('Exit \t Esc', self.close)
        self.shortcut_open = QShortcut(QKeySequence('Esc'), self)
        self.shortcut_open.activated.connect(self.close)

    def setGui(self):
        self.inText = QPlainTextEdit()
        self.outText = QPlainTextEdit()
        self.btnOne = QPushButton("Open File")
        self.btnMany = QPushButton("Open Many")
        self.btnSave = QPushButton("Save")
        self.btnSaveAll = QPushButton("Save All")
        self.btnConvert = QPushButton("Convert")
        self.btnConvertAll = QPushButton("Convert All")
        self.btnReset = QPushButton("Reset")
        self.b1 = QRadioButton("Linear")
        self.b2 = QRadioButton("Iterative")
        self.gridTop.addWidget(self.btnOne, 0, 0)
        self.gridTop.addWidget(self.btnMany, 0, 1)
        self.gridTop.addWidget(self.b1, 1, 0)
        self.gridTop.addWidget(self.b2, 1, 1)
        self.setTextareas()
		
    def btnstate(self,b):
       self.binaryFileIsLinear = b

    def resetGrid(self):
        for i in reversed(range(self.grid.count())):
            if(self.grid.itemAt(i).widget()):
                self.grid.itemAt(i).widget().setParent(None)
            else:
                for j in reversed(range(self.grid.itemAt(i).layout().count())):
                    self.grid.itemAt(i).itemAt(j).widget().setParent(None)
                self.grid.itemAt(i).layout().setParent(None)

    def setTextareas(self):
        self.resetGrid()
        self.grid.addWidget(self.inText, 0, 0)
        self.grid.addWidget(self.outText, 0, 1)

    def addConvertedRow(self, i):
        hb = QHBoxLayout()
        label = QLabel()
        text = self.binfile.get_read_file_name_by_index(i)
        label.setText(text)
        label.setFixedWidth(260)
        hb.addWidget(label)
        saveMe = QPushButton("Save")
        saveMe.clicked.connect(lambda: self.saveAFileFromMany(i))
        hb.addWidget(saveMe)
        self.myGrid.addLayout(hb)

    def setItemList(self, count, isInFile):
        self.resetGrid()
        self.scrollArea = QScrollArea()
        self.myGrid = QVBoxLayout()
        self.scrollWidget = QWidget()
        self.scrollWidget.setFixedWidth(460)
        for i in range(count):
            if(isInFile):
                hb = QHBoxLayout()
                label = QLabel()
                text = self.binfile.get_read_file_name_by_index(i)
                label.setText(text)
                label.setFixedWidth(260)
                hb.addWidget(label)
                openMe = QPushButton("Open")
                convMe = QPushButton("Convert")
                openMe.clicked.connect(lambda: self.openAFileFromMany(i))
                convMe.clicked.connect(lambda: self.convAFile(i))
                hb.addWidget(openMe)
                hb.addWidget(convMe)
                self.myGrid.addLayout(hb)
            else:
                self.addConvertedRow(i)
        self.myGrid.addStretch()
        self.scrollWidget.setLayout(self.myGrid)
        self.scrollArea.setWidget(self.scrollWidget)
        self.grid.addWidget(self.scrollArea, 0, 0)

    def step1Buttons(self):
        for i in reversed(range(self.gridTop.count())):
            self.gridTop.itemAt(i).widget().setParent(None)
        self.inText.setPlainText("")
        self.outText.setPlainText("")
        self.setTextareas()
        self.gridTop.addWidget(self.btnOne, 0, 0)
        self.gridTop.addWidget(self.btnMany, 0, 1)
        self.gridTop.addWidget(self.b1, 1, 0)
        self.gridTop.addWidget(self.b2, 1, 1)

    def step2Buttons(self):
        for i in reversed(range(self.gridTop.count())):
            self.gridTop.itemAt(i).widget().setParent(None)
        self.gridTop.addWidget(self.btnReset, 0, 0)
        self.gridTop.addWidget(self.btnConvert, 0, 1)

    def step2ButtonsMany(self):
        for i in reversed(range(self.gridTop.count())):
            self.gridTop.itemAt(i).widget().setParent(None)
        self.gridTop.addWidget(self.btnReset, 0, 0)
        self.gridTop.addWidget(self.btnConvertAll, 0, 1)

    def step3Buttons(self):
        for i in reversed(range(self.gridTop.count())):
            self.gridTop.itemAt(i).widget().setParent(None)
        self.gridTop.addWidget(self.btnReset, 0, 0)
        self.gridTop.addWidget(self.btnSave, 0, 1)

    def step3ButtonsAll(self):
        for i in reversed(range(self.gridTop.count())):
            self.gridTop.itemAt(i).widget().setParent(None)
        self.gridTop.addWidget(self.btnReset, 0, 0)
        self.gridTop.addWidget(self.btnSaveAll, 0, 1)

    def bindButtons(self):
        self.btnReset.clicked.connect(self.step1Buttons)
        self.btnSave.clicked.connect(self.saveAFile)
        self.btnConvert.clicked.connect(self.startProcesing)
        self.btnOne.clicked.connect(self.openAFile)
        self.btnMany.clicked.connect(self.openManyFiles)
        self.btnSaveAll.clicked.connect(self.saveManyFiles)
        self.btnConvertAll.clicked.connect(self.startProcesingMany)
        self.b1.toggled.connect(lambda:self.btnstate(1))
        self.b2.toggled.connect(lambda:self.btnstate(0))

    def startProcesing(self):
        self.step3Buttons()
        text = self.inText.toPlainText()
        text = self.convertFromBinary(text)
        self.outText.setPlainText(text)

    def openAFileFromMany(self, i):
        text = self.binfile.get_read_file_content_by_index(i)
        text = ' '.join('{:02X}'.format(c) for c in text)
        self.inText.setPlainText(text)
        self.setTextareas()
        self.step2Buttons()

    def convAFile(self, i):
        text = self.binfile.get_read_file_content_by_index(i)
        text = ' '.join('{:02X}'.format(c) for c in text)
        self.inText.setPlainText(text)
        self.setTextareas()
        self.startProcesing()

    def startProcesingMany(self):
        self.resetGrid()
        self.scrollArea = QScrollArea()
        self.myGrid = QVBoxLayout()
        self.scrollWidget = QWidget()
        self.scrollWidget.setFixedWidth(460)
        count = self.binfile.get_file_count()
        self.step3ButtonsAll()

        self.scrollWidget.setLayout(self.myGrid)
        self.grid.addWidget(self.scrollArea, 0, 0)

        self.convertEachFile(count)
        self.myGrid.addStretch()
        self.scrollArea.setWidget(self.scrollWidget)

    def convertEachFile(self, count):
        for i in range(count):
            text = self.binfile.get_read_file_content_by_index(i)
            text = ' '.join('{:02X}'.format(c) for c in text)
            text = text.encode('ascii').decode('unicode-escape')
            out = self.convertFromBinary(text)
            self.tableOfOuts.append(out)
            self.addConvertedRow(i)

    def openAFile(self):
        fileName = QFileDialog.getOpenFileName(
            self.w,
            "Select a binary file",
            "",
            "Binary file (*.bin);; All files (*.*)")
        if fileName[0] != "":
            self.binfile.load_file(fileName[0])
            data = self.binfile.get_read_file_content_by_index(0)
            stringFromData = ' '.join('{:02X}'.format(c) for c in data)
            self.inText.setPlainText(stringFromData)
            self.step2Buttons()

    def openManyFiles(self):
        dirName = QFileDialog.getExistingDirectory(
            self.w,
            "Select Directory",
        )
        if dirName != "":
            self.binfile.load_folder(dirName)
            self.step2ButtonsMany()
            count = self.binfile.get_file_count()
            self.setItemList(count, 1)

    def saveAFileFromMany(self, i):
        text = self.tableOfOuts[i]
        self.outText.setPlainText(text)
        self.saveAFile()

    def saveAFile(self):
        fileName = QFileDialog.getSaveFileName(
            self.w,
            "Select a text file",
            "",
            "Text file (*.txt);; All files (*.*)")
        if fileName[0]:
            file = open(fileName[0], "w", encoding="utf-8")
            file.write(self.outText.toPlainText())
            file.close()
        self.binfile.reset()
        self.step1Buttons()

    def saveManyFiles(self):
        # go to single file saving mode if there's just one file
        if self.binfile.is_single_file():
            self.saveAFile()
            return
        # select directory
        fileName = QFileDialog.getSaveFileName(
            self.w,
            "Select a name for your text files",
            "Find a directory",
            "Text file (*.txt);; All files (*.*)"
        )
        if fileName[0]:
            count = len(self.tableOfOuts)
            for i in range(count):
                text = self.tableOfOuts[i]
                self.binfile.save_file_by_index(fileName[0], i, text)
            # reset the file manager
            self.binfile.reset()
            self.tableOfOuts = []
            self.step1Buttons()

    def convertFromBinary(self, data):
        return self.binConverter.convert(data,self.binaryFileIsLinear)


app = QApplication([])
app.setStyle('Fusion')
win = Window()
win.show()
app.exec_()
