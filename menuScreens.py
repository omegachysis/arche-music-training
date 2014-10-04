
import arche

log = arche.debug.log("menuScreens")

class MainScreen(arche.Application):
    def __init__(self):
        super().__init__()

        self.backgroundColor = (200,200,255)

        self._createInterface()

    def _createInterface(self):
        self.buttonQuit = arche.interface.SolidButton(
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
        self.buttonQuit.right = self.game.width + 1
        self.buttonQuit.top = -1
        self.buttonQuit.name = "quit button"
        self.addSprite(self.buttonQuit)