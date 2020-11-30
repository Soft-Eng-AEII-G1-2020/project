import file_management
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QShortcut, QPlainTextEdit, QPushButton, QFileDialog, QApplication


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.tableOfOuts = []
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

        self.binfile = file_management.BinFile()

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
        self.gridTop.addWidget(self.btnOne, 0, 0)
        self.gridTop.addWidget(self.btnMany, 0, 1)
        self.setTextareas()

    def setTextareas(self):
        for i in reversed(range(self.grid.count())):
            if(self.grid.itemAt(i).widget()):
                self.grid.itemAt(i).widget().setParent(None)
            else:
                for j in reversed(range(self.grid.itemAt(i).layout().count())):
                    self.grid.itemAt(i).itemAt(j).widget().setParent(None)
                self.grid.itemAt(i).layout().setParent(None)
        self.grid.addWidget(self.inText, 0, 0)
        self.grid.addWidget(self.outText, 0, 1)

    def setItemList(self, count, isInFile):
        for i in reversed(range(self.grid.count())):
            if(self.grid.itemAt(i).widget()):
                self.grid.itemAt(i).widget().setParent(None)
            else:
                for j in reversed(range(self.grid.itemAt(i).layout().count())):
                    self.grid.itemAt(i).itemAt(j).widget().setParent(None)
                self.grid.itemAt(i).layout().setParent(None)
        for i in range(count):
            hb = QHBoxLayout()
            label = QLabel()
            text = self.binfile.get_read_file_name_by_index(i)
            label.setText(text)
            hb.addWidget(label)

            if(isInFile):
                openMe = QPushButton("Open")
                convMe = QPushButton("Convert")
                openMe.clicked.connect(lambda: self.openAFileFromMany(i))
                convMe.clicked.connect(lambda: self.convAFile(i))
                hb.addWidget(openMe)
                hb.addWidget(convMe)
            else:
                saveMe = QPushButton("Save")
                saveMe.clicked.connect(lambda: self.saveAFileFromMany(i))
                hb.addWidget(saveMe)
            self.grid.addLayout(hb, i, 0)

    def step1Buttons(self):
        for i in reversed(range(self.gridTop.count())):
            self.gridTop.itemAt(i).widget().setParent(None)
        self.inText.setPlainText("")
        self.outText.setPlainText("")
        self.setTextareas()
        self.gridTop.addWidget(self.btnOne, 0, 0)
        self.gridTop.addWidget(self.btnMany, 0, 1)

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
        self.openAFileFromMany(i)
        self.startProcesing()

    def saveAFileFromMany(self, i):
        text = self.tableOfOuts[i]
        self.outText.setPlainText(text)
        self.saveAFile()

    def startProcesingMany(self):
        count = self.binfile.get_file_count()
        for i in range(count):
            text = self.binfile.get_read_file_content_by_index(i)
            self.tableOfOuts.append(self.convertFromBinary(text))
        self.setItemList(count, 0)
        self.step3ButtonsAll()

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

    def saveAFile(self):
        fileName = QFileDialog.getSaveFileName(
            self.w,
            "Select a text file",
            "",
            "Text file (*.txt);; All files (*.*)")
        if fileName[0]:
            file = open(fileName[0], "w")
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
            "",
            "Text file (*.txt);; All files (*.*)"
        )
        if fileName:
            count = len(self.tableOfOuts)
            for i in range(count):
                text = self.tableOfOuts[i]
                self.binfile.save_file_by_index(fileName[0], i, text)
            # reset the file manager
            self.binfile.reset()
            self.tableOfOuts = []
            self.step1Buttons()

    def convertFromBinary(self, data):
        # todo magic
        data = ' '.join('{:02X}'.format(c) for c in data)
        return data


app = QApplication([])
app.setStyle('Fusion')
win = Window()
win.show()
app.exec_()
