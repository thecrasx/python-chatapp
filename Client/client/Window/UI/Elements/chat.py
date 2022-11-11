from client.Window.UI.Elements.UI.message_ui import MessageUI
from client.Window.UI.Elements.UI.chat_ui import ChatUI

from datetime import datetime



class Chat(ChatUI):
    def __init__(self, mainWindow, *args, **kwargs):
        super().__init__(mainWindow, *args, **kwargs)

        self.window = mainWindow
        self.ui = self.window.ui

        self.messageList = []
        self.messageCount = 0


    
    
    
    def addMessage(self, text, chatFrame, chatLayout, width):
        self.messageCount += 1
        
        dt = datetime.now()
        date = f"{dt.day}/{dt.month}/{dt.year}"
        time = f"{dt.hour}:{dt.minute}"
        
        # date = datetime[0]
        # time = datetime[1].split(":") ## Splits HH:MM:SS
        # time = f"{time[0]}:{time[1]}" ## Time format: HH:MM


        message = MessageUI( text, self.userName, self.userPhoto, 
                                        date, time, chatFrame, chatLayout, 
                                        self.messageCount, width )

        self.messageList.append(message)


    

    def resizeMessages(self):   
        if self.messageList != []:
            width = self.ui.chatSA.width() - 100
            for message in self.messageList:
                if message.messageFrame.visibleRegion():
                    message.setMinimumSize(width)

    
    def hideMessages(self):
        if self.messageList != []:
            for message in self.messageList:
                message.hide()

    
    def showMessages(self):
        if self.messageList != []:   
            for message in self.messageList:
                message.show()




