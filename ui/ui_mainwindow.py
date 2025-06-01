# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(895, 739)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.wordList = QListWidget(self.centralwidget)
        self.wordList.setObjectName(u"wordList")
        self.wordList.setGeometry(QRect(50, 110, 451, 311))
        self.importButton = QPushButton(self.centralwidget)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setGeometry(QRect(170, 430, 191, 61))
        self.quizButton = QPushButton(self.centralwidget)
        self.quizButton.setObjectName(u"quizButton")
        self.quizButton.setGeometry(QRect(170, 500, 191, 61))
        font = QFont()
        font.setBold(True)
        self.quizButton.setFont(font)
        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(530, 400, 271, 71))
        self.toggleThemeButton = QPushButton(self.centralwidget)
        self.toggleThemeButton.setObjectName(u"toggleThemeButton")
        self.toggleThemeButton.setGeometry(QRect(530, 560, 271, 71))
        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setGeometry(QRect(530, 480, 271, 71))
        self.showGraphButton = QPushButton(self.centralwidget)
        self.showGraphButton.setObjectName(u"showGraphButton")
        self.showGraphButton.setGeometry(QRect(170, 570, 191, 61))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 30, 491, 61))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color rgb(0, 0, 127)")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(520, 110, 301, 261))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.NoAntialias)
        self.groupBox.setFont(font2)
        self.addWordButton = QPushButton(self.groupBox)
        self.addWordButton.setObjectName(u"addWordButton")
        self.addWordButton.setGeometry(QRect(50, 40, 201, 51))
        self.editWordButton = QPushButton(self.groupBox)
        self.editWordButton.setObjectName(u"editWordButton")
        self.editWordButton.setGeometry(QRect(50, 110, 201, 51))
        self.deleteWordButton = QPushButton(self.groupBox)
        self.deleteWordButton.setObjectName(u"deleteWordButton")
        self.deleteWordButton.setGeometry(QRect(50, 180, 201, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 895, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.importButton.setText(QCoreApplication.translate("MainWindow", u"\u0406\u043c\u043f\u043e\u0440\u0442\u0443\u0432\u0430\u0442\u0438", None))
        self.quizButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442 \u0442\u0435\u0441\u0442\u0443", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0438\u043d\u0443\u0442\u0438 \u0441\u043b\u043e\u0432\u0430", None))
        self.toggleThemeButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438 \u0442\u0435\u043c\u0443", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 \u0441\u043b\u043e\u0432\u043d\u0438\u043a", None))
        self.showGraphButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u0438 \u0433\u0440\u0430\u0444\u0456\u043a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0432\u0447\u0435\u043d\u043d\u044f \u0441\u043b\u0456\u0432 \u2014 WordLearner\n"
"", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0435\u0440\u0443\u0432\u0430\u043d\u043d\u044f \u0441\u043b\u043e\u0432\u0430\u043c\u0438", None))
        self.addWordButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0441\u043b\u043e\u0432\u043e", None))
        self.editWordButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u0441\u043b\u043e\u0432\u043e", None))
        self.deleteWordButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0441\u043b\u043e\u0432\u043e", None))
    # retranslateUi

