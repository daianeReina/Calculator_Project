from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent


class Display(QLineEdit):
    eqRequested = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size:{BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2.5)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        keyValue = Qt.Key

        isEnter = key in [keyValue.Key_Enter, keyValue.Key_Return]

        if isEnter:
            self.eqRequested.emit()
            print('Pressed enter and signal emitted', type(self).__name__)

            return event.ignore()

        # return super().keyPressEvent(event)
