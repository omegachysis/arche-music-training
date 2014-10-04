
import arche

log = arche.debug.log("menuScreens")

class MainScreen(arche.Application):
    def __init__(self):
        super().__init__()

        self.backgroundColor = (200,200,255)