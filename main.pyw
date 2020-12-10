from PyQt5.QtWidgets import QApplication
from gui import Window

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    win = Window()
    win.show()
    app.exec_()
