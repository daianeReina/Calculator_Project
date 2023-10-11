from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        # CONFIGURING THE BASIC LAYOUT...
        # Central Widget (cw)
        self.cw = QWidget()

        # Vertical Layout
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # WINDOW TITLE
        self.setWindowTitle('Calculator')

    # FIXING THE WINDOW SIZE

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        # self.adjustFixedSize()
