
import arche

log = arche.debug.log("menuScreens")

class MainScreen(arche.Application):
    def __init__(self):
        super().__init__()

        self.backgroundColor = (200,200,255)

        self._createInterface()

    def _createInterface(self):
        self.buttonQuitX = arche.interface.SolidButton(
            width = 40, height = 25,
            colorReset = (100,100,100),
            colorHover = (255,50,50),
            colorPress = (255,150,150),
            command = self.game.quit,
            textObject = arche.Text(
                value = "X",
                x = 0, y = 0,
                color = (255,255,255),
                size = 25,
                font = "font/consola.ttf"),
            )
        self.buttonQuitX.right = self.game.width + 1
        self.buttonQuitX.top = -1
        self.buttonQuitX.name = "x button"
        self.addSprite(self.buttonQuitX)

        def _createMainButton(command, xprop, caption):
            return arche.interface.SolidButton(
                width = self.xprop(.20),
                height= self.yprop(.10),
                x = self.xprop(xprop),
                y = self.yprop(.85),
                colorReset = (80,80,255),
                colorHover = (120,120,255),
                colorPress = (220,220,255),
                command = command,
                textObject = arche.Text(
                    value = caption,
                    x = 0, y = 0,
                    color = (255,255,255),
                    size = self.xprop(.04),
                    font = "font/consola.ttf"))

        self.buttonQuit = _createMainButton(
            command = self.game.quit,
            xprop = .75, caption = "Quit")
        self.buttonQuit.name = "quit button"
        self.addSprite(self.buttonQuit)

        self.buttonSettings = _createMainButton(
            command = None,
            xprop = .50, caption = "Settings")
        self.buttonSettings.name = "settings button"
        self.addSprite(self.buttonSettings)
