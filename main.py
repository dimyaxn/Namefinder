import sys
# from docx import *
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from Namefinder import name_finder, file_name_finder
from design import Ui_MainWindow

text_all = ''

class NameFinder(QMainWindow):
    def __init__(self):
        super(NameFinder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Button_File.clicked.connect(self.open_file)
        self.ui.Button_Find.clicked.connect(self.print_result)


    def open_file(self):
        directory = QFileDialog.getOpenFileNames(self, 'OpenFile', '/Users/stari/OneDrive/Desktop', 'TXT File (*.txt);; DOC File (*.doc);; DOCX File (*.docx)')
        # doc = docx.Document(*directory[0])
        # text_all = '\n\n'.join(paragraph.text for paragraph in doc.paragraphs)
        # full_text = []
        file = open(*directory[0], encoding="utf8")
        text_all = file.read()

        self.ui.Label_File_name.setText(file_name_finder(*directory[0]))
        self.ui.Name_List.setText(text_all)
        return text_all

    def print_result(self):
        result = name_finder(text_all)
        print(result)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NameFinder()
    window.show()
    sys.exit(app.exec())

