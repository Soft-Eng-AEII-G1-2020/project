import file_management
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QVBoxLayout, QShortcut, QPlainTextEdit, QPushButton, QFileDialog, QApplication


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
        self.btnSave.clicked.connect(self.saveManyFiles)
        self.btnConvert.clicked.connect(self.startProcesing)
        self.btnOne.clicked.connect(self.openAFile)
        self.btnMany.clicked.connect(self.openManyFiles)

    def startProcesing(self):
        self.step3Buttons()
        self.outText.setPlainText(self.inText.toPlainText())

    def openAFile(self):
        fileName = QFileDialog.getOpenFileName(
            self.w,
            "Select a binary file",
            "",
            "Binary file (*.bin);; All files (*.*)")
        if fileName[0] != "":
            self.binfile.load_file(fileName[0])
            file = self.binfile.next_read()
            data = file.read()
            #with open(fileName[0], "rb") as binary_file:
            #    data = binary_file.read()
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
            file = self.binfile.next_read()
            data = file.read()
            stringFromData = ' '.join('{:02X}'.format(c) for c in data)
            self.inText.setPlainText(stringFromData)
            self.step2Buttons()

    def saveAFile(self):
        fileName = QFileDialog.getSaveFileName(
            self.w,
            "Select a text file",
            "",
            "Text file (*.txt);; All files (*.*)")
        if fileName[0]:
            fileOut = self.binfile.next_write(fileName[0], True)
            fileOut.write(self.outText.toPlainText())
        self.binfile.reset()
        self.step1Buttons()
    
    def saveManyFiles(self):
        #go to single file saving mode if there's just one file
        if self.binfile.is_single_file():
            self.saveAFile()
            return
        #select directory
        fileName = QFileDialog.getSaveFileName(
            self.w,
            "Select a name for your text files",
            "",
            "Text file (*.txt);; All files (*.*)"
        )
        if fileName:
            #finish the file that the user got to view
            fileOut = self.binfile.next_write(fileName[0], True)
            fileOut.write(self.outText.toPlainText())
            #save the rest of the files
            while(True):
                file = self.binfile.next_read()
                if(file == -1):
                    break
                data = file.read()
                stringFromData = ' '.join('{:02X}'.format(c) for c in data)
                fileOut = self.binfile.next_write(fileName[0], True)
                fileOut.write(stringFromData)
            #reset the file manager
            self.binfile.reset()
            self.step1Buttons()




app = QApplication([])
app.setStyle('Fusion')
win = Window()
win.show()
app.exec_()
