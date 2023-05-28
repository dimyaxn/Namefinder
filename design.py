# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(506, 702)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/buttons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: #eceff1;\n"
"    background-color: #2B2B2B;\n"
"    font-family: Jost;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"    }\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Button_File = QPushButton(self.centralwidget)
        self.Button_File.setObjectName(u"Button_File")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_File.sizePolicy().hasHeightForWidth())
        self.Button_File.setSizePolicy(sizePolicy2)
        self.Button_File.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_File.setStyleSheet(u"\n"
" QPushButton {\n"
"     border: 2px solid #8AB4F8;\n"
"     border-radius: 29px;\n"
"     min-width: 80px;\n"
"	font-size: 28pt;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     background-color: #8AB4F8;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     border: 2px solid #9AA0A6;\n"
"     background-color: #9AA0A6;\n"
" }\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_File.setIcon(icon1)
        self.Button_File.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.Button_File)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Jost"])
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #9AA0A6;\n"
"font-size: 13pt;\n"
"font-weight: 600;")

        self.verticalLayout_2.addWidget(self.label)

        self.Name_List = QTextEdit(self.centralwidget)
        self.Name_List.setObjectName(u"Name_List")
        self.Name_List.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Name_List.sizePolicy().hasHeightForWidth())
        self.Name_List.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Jost"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.Name_List.setFont(font1)
        self.Name_List.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.Name_List.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Name_List.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Name_List.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Name_List.setUndoRedoEnabled(False)

        self.verticalLayout_2.addWidget(self.Name_List)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0438\u043c\u0435\u043d", None))
        self.Button_File.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u043c\u0451\u043d \u0432 \u0442\u0435\u043a\u0441\u0442\u0435:", None))
        self.Name_List.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Jost'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

