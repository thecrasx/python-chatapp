################### PySide6 ###################
from PySide6.QtCore import QThread, QEvent, Qt
from PySide6.QtGui import QKeySequence, QShortcut


################### ChatApp ###################
from client.Window.UI.Elements.custom_signals import CustomSignal


#################### Other ####################
from time import sleep


################################################



class LineCountTrack(QThread):
    def __init__(self, target: object, chatInputInFocus: CustomSignal) -> None:
        super().__init__()

        # Custom signals
        self.__customSignal = CustomSignal()
        self.lineCountChanged = self.__customSignal.lineCountChanged # Signal: On line count change

        self.chatInputInFocus = chatInputInFocus # Signal: On focus change  
        self.chatInputInFocus.connect(self.__changeFocus)  
        
        self.__inFocus = False
        self.chatInput = target

        
         
    def __changeFocus(self, focus: bool) -> None:
        self.__inFocus = focus

        
         
    def __getLineCount(self):
        return self.chatInput.document().lineCount()

        
        
    def run(self):
        lineCount = -1
        
        while True:
            sleep(0.001)
            
            if self.__inFocus:
                newLineCount = self.__getLineCount()
                
                if newLineCount != lineCount:
                    lineCount = newLineCount
                    self.lineCountChanged.emit()

                          
            



class ChatInput:
    def __init__(self, chatInputBox, chatInput) -> None:
        self.chatInputBox = chatInputBox
        self.chatInput = chatInput

    
        # Shortcut to insert new line
        self.shortCut = QShortcut(QKeySequence("Alt+Return"), self.chatInput)
        self.shortCut.activated.connect(self.__insertNewLine)


        # Custom signals
        self.__customSignal = CustomSignal()
        self.keyEnterPressed = self.__customSignal.keyEnterPressed
        self.chatInputInFocus = self.__customSignal.chatInputInFocus


        # Line count tracker
        self.lineCountTrack = LineCountTrack(self.chatInput, self.chatInputInFocus)
        self.lineCountTrack.lineCountChanged.connect(self._resizeEvent)
        self.lineCountTrack.start()
        

        ### Events
        self.chatInput.installEventFilter(self.chatInput)
        self.chatInput.eventFilter = self.eventFilter
        
        self.chatInput.focusInEvent = self._focusInEvent
        self.chatInput.focusOutEvent = self._focusOutEvent
        


    

    def __insertNewLine(self):
        self.chatInput.insertPlainText("\n")
    
    
    ################## Events ##################
    
    def _focusInEvent(self, event):
        self.chatInputInFocus.emit(True)



    def _focusOutEvent(self, event):
        self.chatInputInFocus.emit(False)
        


    def eventFilter(self, obj, event):
        if obj == self.chatInput:
            if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
                    
                    text = self.chatInput.toPlainText()
                    if text != "":
                        self.keyEnterPressed.emit(text)
                    return True
            else:
                return False

        else:
            return True



    def _resizeEvent(self):
        lineCount = self.chatInput.document().lineCount()
        height = 35 ## Default value
            
        if lineCount != 1:
            height = height + ( lineCount - 1 ) * 17.4            

        self.chatInputBox.setMinimumHeight(height)  
        self.chatInputBox.setMaximumHeight(height)
        self.chatInput.setMinimumHeight(height - 7)