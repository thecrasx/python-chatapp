################### PySide6 ###################
from turtle import delay
from PySide6.QtCore import QThread, QEvent
from PySide6.QtWidgets import QLineEdit


################### ChatApp ###################
from client.Window.UI.Elements.custom_signals import CustomSignal
from client.Window.UI.Elements.UI.friends_ui import FriendUI
from time import time, sleep





class SearchMode:
    friends = 0
    addFriends = 1
    friendRequests = 2
    blockList = 3


class FriendsSearch:
    def __init__(self, mainWindow):
        self.window = mainWindow
        self.ui = self.window.ui
        self.signals = self.window.signals
        self.connectionUI = self.window.connectionUI
        
        self.ui.searchInput.focusInEvent = self.__focusInEvent
        self.ui.searchInput.focusOutEvent = self.__focusOutEvent

        self.ui.searchInput.textChanged.connect(self.__onNewInput)
        self.signals.friendsSignal.searchInputDelayed.connect(self.__onInputDelayed)



        self.mode = SearchMode()

        self.__previousInput = None
        self.__searchInputDelayThread = SearchInputDelayThread(self.signals)

        self.__noInputEmited = False





    def updateCurrentMode(self):
        if self.ui.friendsPage.isVisible():
            self.mode = SearchMode.friends

        elif self.ui.addFriendsPage.isVisible():
            self.mode = SearchMode.addFriends

        elif self.ui.friendRequestPage.isVisible():
            self.mode =  SearchMode.friendRequests

        elif self.ui.blockListPage.isVisible():
            self.mode = SearchMode.blockList


    def search(self):
        self.updateCurrentMode()

        text = self.ui.searchInput.text()

        if text.replace(" ", "") == "":
            if not self.__noInputEmited:
                self.__noInputEmited = True
                self.__previousInput = ""
                self.signals.friendsSignal.searchNoInput.emit()
                return
        
        if text != self.__previousInput:
            self.__previousInput = text

            if self.mode == SearchMode.friends:
                pass

            elif self.mode == SearchMode.addFriends:
                self.addFriends(text)


    def addFriends(self, name):
        self.connectionUI.request.findNewFriends(name, 7)


    def __onNewInput(self):
        self.__noInputEmited = False
        self.signals.friendsSignal.searchInputChanged.emit()

    
    def __onInputDelayed(self):
        self.search()


    def __focusInEvent(self, event):
        self.__searchInputDelayThread.start()
        
        QLineEdit.focusInEvent(self.ui.searchInput, event)

    def __focusOutEvent(self, event):
        self.__searchInputDelayThread.stop()

        QLineEdit.focusOutEvent(self.ui.searchInput, event)





class SearchInputDelayThread(QThread):
    def __init__(self, signals):
        super().__init__()

        self.delay = False
        self.__delayTime = time()
        self.signals = signals
        self.signals.friendsSignal.searchInputChanged.connect(self.__onNewInput)

        
    def __onNewInput(self):
        self.__delayTime = time()
        self.delay = False


    def stop(self):
        self.__running = False


    def run(self):
        self.__running = True
        self.__delayTime = time()

        while self.__running:

            if not self.delay:
                if time() - self.__delayTime >= 0.75:
                    self.signals.friendsSignal.searchInputDelayed.emit()
                    self.delay = True

            sleep(0.1)

