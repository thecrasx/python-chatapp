

from client.image_loader import ImageLoader
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt



class ProfileUI:
    def __init__(self, mainWindow):
        self.window = mainWindow
        self.ui = self.window.ui
        



    
    
    
    def changeProfilePhoto(self):
        img = QFileDialog.getOpenFileName(self.window, "Select a image", 
                                    filter=("JPEG (*.jpg *.jpeg);;PNG (*.png)"))

        if img[0]:
            imgByteArray = ImageLoader.getImageByteArray(img[0], 100)


            ImageLoader.setPixmap(self.ui.userPhotoLMLabel, imgByteArray, 70)
            ImageLoader.setPixmap(self.ui.userPhotoSettingsLabel, imgByteArray, 60)

            imgHex = ImageLoader.getHexFromBytes(imgByteArray)

            if len(imgHex) <= 15000:
                self.window.connectionUI.request.changeProfilePhoto(imgHex)
            else:
                print("Image too big")



        
        

