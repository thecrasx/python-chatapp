from client.Window.UI.Theme.theme_loader import ThemeLoader


class Theme:
    def __init__(self, theme):
        self.theme = ThemeLoader(theme)