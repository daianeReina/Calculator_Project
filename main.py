import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label_1 = QLabel('My Text')
    label_1.setStyleSheet('font-size:50px')
    window.v_layout.addWidget(label_1)
    window.adjustFixedSize()

    window.show()
    app.exec()
