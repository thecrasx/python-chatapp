from tkinter import W
from PIL import Image, ImageCms, ImageDraw
import io
import numpy as np

from PySide6.QtGui     import QPixmap, QPainter, QPainterPath, QImage
from PySide6.QtWidgets import QLabel
from PySide6.QtCore    import Qt, QSize



class ImageLoader:
    def __cropImage(image, size):
        w, h = image.size
        cropWidth = size
        cropHeight = size
        
        
        return image.crop(((w - cropWidth) // 2,
                         (h - cropHeight) // 2,
                         (w + cropWidth) // 2,
                         (h + cropHeight) // 2))


    def __cropToCenter(image, fraction=0.7):
        frac = fraction
        left = image.size[0]*((1-frac)/2)
        upper = image.size[1]*((1-frac)/2)
        right = image.size[0]-((1-frac)/2)*image.size[0]
        bottom = image.size[1]-((1-frac)/2)*image.size[1]  

        return image.crop((left, upper, right, bottom))


    def __cropToSquare(img):
        w, h = img.size

        if h > w:
            h = w
        else:
            w = h

        return img.resize((w, h), Image.Resampling.LANCZOS)



    def __processImage(img, fraction=0.7):
        # CONVERT TO sRGB IF POSSIBLE
        icc = img.info.get("icc_profile", "")
        

        if icc:
            ioHandle = io.BytesIO(icc)
            srcProfile = ImageCms.ImageCmsProfile(ioHandle)
            dstProfile = ImageCms.createProfile('sRGB')

            convertedImg = ImageCms.profileToProfile(img, srcProfile, dstProfile)
            convertedIcc = convertedImg.info.get("icc_profile", "")

            if icc != convertedIcc:
                img = convertedImg
        

        # CROP IMAGE
        if fraction:
            img = ImageLoader.__cropToCenter(img, fraction)

        else:
            img = ImageLoader.__cropToSquare(img)
            img = ImageLoader.__cropImage(img, 500)


        # DRAW CIRCULAR IMAGE     
        arrImg = np.array(img)
        alpha = Image.new("L", img.size, 0)

        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0, 0, img.size[0], img.size[1]], 0, 360, fill = 255)

        arrAlpha = np.array(alpha)
        arrImg = np.dstack((arrImg, arrAlpha))

        img = Image.fromarray(arrImg)

        return img


    def getImageByteArray(path, size=0):
        # LOAD IMAGE
        img = Image.open(path)
        imgFormat = img.format

        # PROCESS IMAGE
        img = ImageLoader.__processImage(img, 0)

        # RESIZE IMAGE
        if size > 0:
            img = img.resize((size, size), Image.Resampling.LANCZOS)

        
        # SAVE IMAGE
        imgByteArray = io.BytesIO()
        img = img.convert("RGB")
        img.save(imgByteArray, format="JPEG", optimize=True)
        img.save("E:/Programming/Projects/Python/ChatApp/test.png", format="JPEG", optimize=True)

        imgByteArray = imgByteArray.getvalue()

        return imgByteArray


    def getHexFromBytes( _bytes):
        return _bytes.hex()


    def getBytesFromHex(_hex):
        return bytes.fromhex(_hex)


    def setPixmap(parent, image, size):
        target = QPixmap(QSize(size, size))
        target.fill(Qt.transparent)
        radius = round(size / 2)

        img = QImage()
        img.loadFromData(image)
        p = QPixmap(img).scaled(QSize(size, size), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        painter = QPainter(target)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(0, 0, size, size,  radius, radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)

        painter.end()
        
        parent.setPixmap(target)




if __name__ == "__main__":
    img = ImageLoader.getImageByteArray("E:/Other/1/21706548_154953608419573_594140024_o.jpg", 100)
    img = ImageLoader.getHexFromBytes(img)
    print(len(img))