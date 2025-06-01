# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'importdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-40, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.importLabel = QLabel(Dialog)
        self.importLabel.setObjectName(u"importLabel")
        self.importLabel.setGeometry(QRect(120, 30, 191, 71))
        self.chooseFileButton = QPushButton(Dialog)
        self.chooseFileButton.setObjectName(u"chooseFileButton")
        self.chooseFileButton.setGeometry(QRect(120, 120, 171, 41))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.importLabel.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u0444\u0430\u0439\u043b \u0434\u043b\u044f \u0456\u043c\u043f\u043e\u0440\u0442\u0443", None))
        self.chooseFileButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0444\u0430\u0439\u043b", None))
    # retranslateUi

