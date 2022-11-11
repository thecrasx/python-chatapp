from PySide6.QtWidgets import QFrame, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QSize



class OverlayUI(QFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setOverlayOpacity(0)
        self.move(0, 0)

        self.titleBarHeight = 0

        self.frameLayout = QVBoxLayout(self)

    def setOffset(self, titleBar):
        self.titleBarHeight = titleBar.height() - 2

        self.move(0, self.titleBarHeight)

    def updateSize(self, width, height):     
        self.resize(QSize(width, height - self.titleBarHeight))
    
    def addWidget(self, widget):
        self.frameLayout.addWidget(widget, 0, Qt.AlignCenter|Qt.AlignCenter)


    def setOverlayOpacity(self, opacity):
        self.setStyleSheet(f"background: rgba(0, 0, 0, {opacity});")