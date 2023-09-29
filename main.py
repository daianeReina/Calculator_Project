import sys

from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # CREATION APLICATTION
    app = QApplication(sys.argv)
    window = MainWindow()

    # DEFINING THE ICON
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Execution
    window.adjustFixedSize()
    window.show()
    app.exec()
