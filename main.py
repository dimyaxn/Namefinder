import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow

class NameFinder(QMainWindow):
    def __init__(self):
        super(NameFinder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NameFinder()
    window.show()
    sys.exit(app.exec())

