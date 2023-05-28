import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from Namefinder import *
from design import Ui_MainWindow


class NameFinder(QMainWindow):
    def __init__(self):
        super(NameFinder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Button_File.clicked.connect(self.open_file)


    def open_file(self):
        directory = QFileDialog.getOpenFileNames(self, 'OpenFile', 'C://', 'DOCX File (*.docx);; TXT File (*.txt)')
        text_all = get_text(*directory[0])
        self.ui.Name_List.setText("\n".join(name_finder(text_all)))
        return text_all


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NameFinder()
    window.show()
    sys.exit(app.exec())

