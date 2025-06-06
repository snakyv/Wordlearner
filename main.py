import sys
from PySide6.QtWidgets import QApplication
from controllers import MainWindow
from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pixmap = QPixmap("icons/splash_logo.png")
    splash = QSplashScreen(pixmap)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.show()
    splash.showMessage("Завантаження...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)

    window = MainWindow()

    QTimer.singleShot(2000, splash.close)
    QTimer.singleShot(2000, window.show)

    sys.exit(app.exec())
