from client.Window.UI.Theme.stylesheet import StyleSheet



class RecentChat(StyleSheet):
    def __init__(self, data):
        StyleSheet.__init__(self, data)

        self.photo = None
        self.username = None
        self.closeBtn = None

        self.buttonFrame = None
        self.userNameNPhotoFrame = None
