from PySide6.QtGui     import QPixmap, QPainter, QPainterPath, QImage
from PySide6.QtWidgets import QLabel
from PySide6.QtCore    import Qt, QSize

from client.image_loader import ImageLoader




class PhotoLabel(QLabel):
    def __init__(self, parent, size, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.antialiasing = True
        
        self.__size = size
        self.setMinimumSize(size, size)
        self.setMaximumSize(size, size)
        self.radius = round(size / 2)


        self.target = QPixmap(self.size())
        self.target.fill(Qt.transparent)

        self.setStyleSheet(f"background: gray; border: 1px solid transparent; border-radius: {self.radius}px")
        


    def __paint(self, image):
        img = QImage()
        img.loadFromData(image)
        p = QPixmap(img).scaled(QSize(self.__size, self.__size), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        painter = QPainter(self.target)

        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.radius, self.radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.setPixmap(self.target)

    
    def loadImage(self, image):
        image = ImageLoader.getImageByteArray(image)
        self.__paint(image)
        self.setStyleSheet("")


    def loadImageFromHex(self, _hex):
        image = ImageLoader.getBytesFromHex(_hex)
        self.__paint(image)
        self.setStyleSheet("")


