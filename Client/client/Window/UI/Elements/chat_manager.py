# ipsum = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
# when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, 
# but also the leap into electronic typesetting, remaining essentially unchanged. 
# It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with 
# desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""


from PySide6.QtCore import QThread
from time import sleep

################### ChatApp ###################
from client.Window.UI.Elements.custom_signals import CustomSignal
from client.Window.UI.Elements.UI.ui_elements import UIElements
from client.Window.UI.Elements.UI.message_ui import MessageUI
from client.Window.UI.Elements.UI.chat_ui import ChatUI
from client.Window.UI.Elements.chat_input import ChatInput
from client.Window.UI.Elements.chat import Chat


################################################




class ChatManager:
    def __init__(self, mainWindow):
        self.window = mainWindow
        self.ui = self.window.ui
        
        self.chatCount = 0
        self.chatList = []

        self.currentChat = None
        self.chatInput = ChatInput(chatInputBox=self.ui.chatInputBox,
                                    chatInput=self.ui.chatInput)

        
        # Custom signals
        self.__customSignal = CustomSignal()
        self.currentChatChanged = self.__customSignal.currentChatChanged
        self.currentChatChanged.connect(self._onCurrentChatChanged)
        self.chatInput.keyEnterPressed.connect(self.addMessage)

    
    
    def _onCurrentChatChanged(self, Chat: Chat):     
        # Updates previous chat
        if self.currentChat is not None:
            self.currentChat.setNormal()
            self.currentChat.hideMessages()

        self.currentChat = Chat
        self.currentChat.resizeMessages()
        self.currentChat.showMessages()

        if not self.ui.mainFrame.isHidden():
            self.ui.mainFrame.hide()
        
        if not self.ui.chatInput.isEnabled():
            self.ui.chatInput.setEnabled(True)

        if self.ui.chatContainer.isHidden():
            self.ui.chatContainer.show()


    
    
    def addMessage(self, text):
        self.ui.chatInput.clear()
        self.currentChat.addMessage(text=text, 
                                        chatFrame=self.ui.chatBox,
                                        chatLayout=self.ui.chatBoxLayout,
                                        width=self.ui.chatSAWC.width() - 50)

    
    
    def addChat(self, userName, userPhoto):
        self.chatCount += 1
        
        chat = Chat(self.window, userName, userPhoto, self.chatCount, self.currentChatChanged)
        chat.closeChatBtnPressed.connect(self.removeChat)

        self.chatList.append(chat)

    
    def removeChat(self, Chat: Chat):
        if self.currentChat == Chat:
            self.ui.chatInput.setDisabled(True)
            self.ui.chatContainer.hide()
            self.ui.mainFrame.show()

            
            
            
            self.currentChat = None
            Chat.hideMessages()


        Chat.close()
        self.chatList.remove(Chat)
        