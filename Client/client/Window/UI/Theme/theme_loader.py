from client.Window.UI.Theme.stylesheet import StyleSheet
from client.Window.UI.Theme.properties import *
import json


class ThemeLoader:
    def __init__(self, theme):
        with open(f"./res/themes/{theme}") as f:
            self._theme = json.load(f)
            f.close()

        self._setupTheme()


    def _load(self, path):
        path = path
        data = self._theme

        if "/" in path:
            path = path.split("/")

        if type(path) is list:
            for currentPath in path:
                data = data[currentPath]
        
        else:
            data = data[path]

        return data


    def _setupTheme(self):
        self.recentChat = RecentChat(self._load("recent-chat/main"))
        self.recentChat.setDefault(padding="7px 5px 7px 5px")
        self.recentChat.replaceStateStyleSheet("hover", "normal")
        self.recentChat.replaceStateStyleSheet("pressed", "normal")

        self.recentChat.userNameNPhotoFrame = StyleSheet(self._load("recent-chat/username-frame"))
        self.recentChat.userNameNPhotoFrame.setDefault(padding="0px", border="none")
        self.recentChat.userNameNPhotoFrame.replaceStateStyleSheet("hover", "normal")
        self.recentChat.userNameNPhotoFrame.replaceStateStyleSheet("pressed", "normal")
 
        self.recentChat.buttonFrame = StyleSheet(self._load("recent-chat/button-frame"))
        self.recentChat.buttonFrame.setDefault(padding="0px", border="none")
        self.recentChat.buttonFrame.replaceStateStyleSheet("hover", "normal")
        self.recentChat.buttonFrame.replaceStateStyleSheet("pressed", "normal")

        








if __name__ == "__main__":
    TL = ThemeLoader("default.json")
    print(TL.recentChat.pressed.stylesheet)