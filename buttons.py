
from PySide6.QtWidgets import QPushButton, QWidget, QGridLayout

from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpity


class Button (QPushButton):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')


class ButtonsGrid(QGridLayout):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._gridMask = [
            ['C', '+/-', '%', '÷'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', ',', '='],
        ]

        self._makeGrid()

    def _makeGrid(self):
        for rowNum, rowData in enumerate(self._gridMask):
            for collumnNum, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpity(buttonText):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, rowNum, collumnNum)
