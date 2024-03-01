from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from utils import isEmpty


class Display(QLineEdit):
    enterPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()

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
        text = event.text().strip()
        key = event.key()
        keyValue = Qt.Key

        isEnter = key in [keyValue.Key_Enter,
                          keyValue.Key_Return, keyValue.Key_Equal]
        isDelete = key in [keyValue.Key_Backspace,
                           keyValue.Key_Delete, keyValue.Key_D]
        isEsc = key in [keyValue.Key_Escape, keyValue.Key_C]

        if isEnter:
            self.enterPressed.emit()
            print(f'Pressed enter or {text} and signal emitted', type(
                self).__name__)
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            print(f'Pressed delete or {text} and signal emitted', type(
                self).__name__)
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            print('Pressed esc and signal emitted', type(self).__name__)
            return event.ignore()

        # return super().keyPressEvent(event)

        # Não passar daqui se não tiver texto

        if isEmpty(text):
            return event.ignore()

        print('Texto', text)
