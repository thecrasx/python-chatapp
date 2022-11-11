from PIL import Image, ImageColor
import os


class IconColorizer:
    def __init__(self):
        self._icon = None
        self._icon_path = None


    def load(self, path):
        self._icon_path = path
        self._icon = Image.open(self._icon_path)

    def save(self, path=None):
        if path is None:
            self._icon.save(self._icon_path)

        else:
            self._icon.save(path)

    def colorize(self, color):
        if self._icon is not None:
            width, height = self._icon.size
            color = self._getColorCode(color)
            
            for x in range(width):
                for y in range(height):
                    pixel = self._icon.getpixel( (x, y) )
                    
                    if pixel[3] > 0:
                        new_color = ( color[0], color[1], color[2], pixel[3] ) # ( r, g, b, a )
                        self._icon.putpixel( ( x, y ), new_color)



    def _getColorCode(self, color):     
        if color is not None:
            color = color.replace(" ", "") # Remove spaces
                                     
            # Hex color code
            if color[0] == "#":
                return ImageColor.getcolor(color, "RGB")

            
            # RGB / RGBA color code
            elif "rgb" in color.lower() or "rgba" in color.lower():
                # Get values from the string
                color = color.split("(", 1)[1]
                color = color.split(")", 1)[0]

                # Convert to tuple 
                return eval(color)
            
            else:
                print(f"Invalid color code: {color}")
                return None

            




if __name__ == "__main__":
    path = "./client/Window/UI/Icons/"
    icons = os.listdir(path)
    
    ic = IconColorizer()

    color = "#5d0cc4"

    for icon in icons:
        ic.load(f"{path}{icon}")
        ic.colorize("#5d0cc4")
        ic.save()