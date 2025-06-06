from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer

def show_splash(app, main_window):
    pixmap = QPixmap("icons/splash_logo.png")  # вставь свой логотип
    splash = QSplashScreen(pixmap)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.show()
    splash.showMessage("Завантаження...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)

    QTimer.singleShot(2000, splash.close)  # 2 секунды
    QTimer.singleShot(2000, main_window.show)
