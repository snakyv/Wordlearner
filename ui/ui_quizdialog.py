# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quizdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(441, 323)
        self.wordLabel = QLabel(Dialog)
        self.wordLabel.setObjectName(u"wordLabel")
        self.wordLabel.setGeometry(QRect(50, 20, 101, 21))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.wordLabel.setFont(font)
        self.wordLabel.setLayoutDirection(Qt.LeftToRight)
        self.answerEdit = QLineEdit(Dialog)
        self.answerEdit.setObjectName(u"answerEdit")
        self.answerEdit.setGeometry(QRect(20, 60, 161, 51))
        self.checkButton = QPushButton(Dialog)
        self.checkButton.setObjectName(u"checkButton")
        self.checkButton.setGeometry(QRect(250, 40, 151, 51))
        self.nextButton = QPushButton(Dialog)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(240, 100, 171, 51))
        self.resultLabel = QLabel(Dialog)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setGeometry(QRect(30, 230, 381, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.resultLabel.setFont(font1)
        self.resultLabel.setLayoutDirection(Qt.RightToLeft)
        self.resultLabel.setMidLineWidth(0)
        self.soundButton = QPushButton(Dialog)
        self.soundButton.setObjectName(u"soundButton")
        self.soundButton.setGeometry(QRect(280, 160, 91, 41))
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 130, 191, 41))
        self.progressBar.setValue(24)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.wordLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.answerEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043f\u0435\u0440\u0435\u043a\u043b\u0430\u0434", None))
        self.checkButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0432\u0456\u0440\u0438\u0442\u0438", None))
        self.nextButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0443\u043f\u043d\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.resultLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.soundButton.setText("")
    # retranslateUi

