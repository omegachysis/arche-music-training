
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

        self.buttonQuit = arche.interface.SolidButton(
            width = self.xprop(.2),
            height= self.yprop(.1),
            colorReset = (80,80,255),
            colorHover = (120,120,255),
            colorPress = (220,220,255),
            command = self.game.quit,
            textObject = arche.Text(
                value = "Quit",
                x = 0, y = 0,
                color = (255,255,255),
                size = self.xprop(.04),
                font = "font/consola.ttf"),
            )
        self.buttonQuit.x = self.xprop(.75)
        self.buttonQuit.y = self.yprop(.85)
        self.buttonQuit.name = "quit button"
        self.addSprite(self.buttonQuit)