    
    

    
class _Data:
    def __init__(self, stylesheet=None, properties=None):
        self.stylesheet = stylesheet
        self.properties = properties
    
    

    
class StyleSheet:
    def __init__(self, data):
        self._data = data

        self.default = ""
        self.className = self._data["class-name"]

        self.load()
    
    

    
    # Default means it will go in every category ( normal, hover, pressed, etc. )
    def setDefault(self, **kwargs):
        self.default = self._format(kwargs, default=True)
        self.load()
    
    

    
    def load(self):
        self.normal = self._loadNormal()
        self.hover = self._loadHover()
        self.pressed = self._loadPressed()
        self.extended = self._loadExtended()
        self.stylesheet = self._connectAll()
    
    

    
    def replaceStateStyleSheet(self, state, newState):
        newState = self._formatState(newState)

        if state == "hover":
            self.hover.stylesheet = self.hover.stylesheet.replace("::hover", newState)
        
        elif state == "pressed":
            self.pressed.stylesheet = self.pressed.stylesheet.replace("::pressed", newState)
    
    

      
    def _format(self, data, default=False, returnSet=False):
        output = ""
        dataSet = {}

        for key in data:
            if key != "extend":
                output += f"    {key}: {data[key]};\n"

            if returnSet:
                dataSet[key] = data[key]


        if default:
            if "_" in output:
                output = output.replace("_", "-")


        if returnSet:
            return output, dataSet

        else:
            return output
    
    

    
    def _formatState(self, state):
        if state == "normal":
            return ""       
        else:  
            return f"::{state}"
    
    

    
    def _extend(self, data):
        extended = ""

        if "extend" in data:
            extendedData = data["extend"]

            for className in extendedData:
                properties = self._format(extendedData[className])
                extended += f"{className} {{\n{properties}}}\n\n"

        if extended:
            return extended[:-2]
        else:
            return extended
    
    

    
    def _makeStyleSheet(self, state, data, extend):
        state = self._formatState(state)
        
        if extend:
            return f"{self.className}{state} {{\n{self.default}{data}}}\n\n{extend}"
        else:
            return f"{self.className}{state} {{\n{self.default}{data}}}"
    
    

     
    def _loadNormal(self):
        if "normal" in self._data:
            data = self._data["normal"]
            normal = self._format(data, returnSet=True)
            extend = self._extend(data)

            return _Data(self._makeStyleSheet("normal", normal[0], extend), normal[1])
        else:
            return None
    
    

    
    def _loadHover(self):
        if "hover" in self._data:
            data = self._data["hover"]
            hover = self._format(data, returnSet=True)
            extend = self._extend(data)

            return _Data(self._makeStyleSheet("hover", hover[0], extend), hover[1])
        else:
            return None
    
    

    
    def _loadPressed(self):
        if "pressed" in self._data:
            data = self._data["pressed"]
            pressed = self._format(data, returnSet=True)
            extend = self._extend(data)

            return _Data(self._makeStyleSheet("pressed", pressed[0], extend), pressed[1])
        else:
            return None
    
    

    
    def _loadExtended(self):
        data = self._extend(self._data)

        if data:
            return data
        else:
            return None
    
    

    
    def _connectAll(self):
        stylesheet = ""

        if self.normal:
            stylesheet += self.normal.stylesheet + "\n\n"

        if self.hover:
            stylesheet += self.hover.stylesheet + "\n\n"

        if self.pressed:
            stylesheet += self.pressed.stylesheet + "\n\n"

        if self.extended:
            stylesheet += self.extended + "\n\n"

        return stylesheet[:-2]