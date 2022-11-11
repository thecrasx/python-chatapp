from client.Window.UI.Animations.animations import Animations





class ButtonFunctions:
    def __init__(self, mainWindow) -> None:
        self.window = mainWindow
        self.ui = self.window.ui

        self.animations = Animations(self.ui.friendsContainer)
        self.windowSize = self.window.size()



    def friendsContainerSlide(self):
        width = self.ui.friendsContainer.width()

        self.animations.friendsContainerAnimation.slide(width, 500)


    def toggleFullScreen(self):
        if self.window.isMaximized():
            self.window.showNormal()
        
        else:
            self.window.showMaximized()


    def setFriendsPage(self, friends=False, add=False, request=False, block=False):
        if friends:
            self.ui.friendsLabel.setText("Friends")
            self.ui.friendsSW.setCurrentWidget(self.ui.friendsPage)

        elif add:
            self.ui.friendsLabel.setText("Add Friends")
            self.ui.friendsSW.setCurrentWidget(self.ui.addFriendsPage)
            
        elif request:
            self.ui.friendsLabel.setText("Friend Requests")
            self.ui.friendsSW.setCurrentWidget(self.ui.friendRequestPage)

        elif block:
            self.ui.friendsLabel.setText("Block List")
            self.ui.friendsSW.setCurrentWidget(self.ui.blockListPage)