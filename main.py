import sys

from main_window import MainWindow
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # CREATION APLICATTION
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # DEFINING THE ICON
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 2.0 = 4.0')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Button
    button = Button('Text 1')
    window.addToVLayout(button)

    # Execution
    window.adjustFixedSize()
    window.show()
    app.exec()
