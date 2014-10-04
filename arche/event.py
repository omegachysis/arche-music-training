from pygame.locals import *

import logging

from . import control

log = logging.getLogger("R.Event")

class Handler(object):
    def __init__(self, command=None):
        if command:
            self.run = command
            self._commands = [command]

    def run(self, event, engine):
        pass

class KeyHandler(Handler):
    def __init__(self):
        super().__init__()

        # NAME : [KEY, COMMAND, ARGS]
        self.commands = {}
        # KEY : [NAME, NAME, ..]
        self._commandKeys = {}

    def addCommand(self, name, key, command, args=[]):
        if name in self.commands:
            # already added this command
            pass
        else:
            self.commands[name] = [key, command, args]
            if key not in self._commandKeys:
                self._commandKeys[key] = [name]
            else:
                self._commandKeys[key].append(name)

    def removeCommand(self, name):
        if name in self.commands:
            key, command, args = self.commands[name]
            if name in self._commandKeys[key]:
                self._commandKeys[key].remove(name)
            del self.commands[name]

    def run(self, event, game):
        if event.type == KEYDOWN:
            if event.key in self._commandKeys:
                for name in self._commandKeys[event.key]:
                    key, command, args = self.commands[name]
                    command(*args)

class GameEngineHandler(Handler):
    def __init__(self):
        super().__init__()
        log.debug("game engine handler initialized")
        
    def run(self, event, game):
        if event.type == QUIT:
            game.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game.postEvent(QUIT)
            elif event.key == K_BACKQUOTE:
                if game.autoPause:
                    if game.paused == False:
                        game.paused = True
                    else:
                        game.paused = False
                game.gameConsole.toggleHidden()
            elif event.key == K_RETURN:
                if not game.gameConsole.hidden:
                    game.gameConsole.executeEntry()
            elif event.key == K_BACKSPACE:
                if not game.gameConsole.hidden:
                    game.gameConsole.entryBackspace()
            else:
                if not game.gameConsole.hidden:
                    game.gameConsole.entryAdd(event.unicode)
        elif event.type == MOUSEBUTTONDOWN:
            if not game.gameConsole.hidden:
                if event.button == 2:
                    game.gameConsole.pickSprite()
                elif event.button == 4:
                    game.gameConsole.scrollUp()
                elif event.button == 5:
                    game.gameConsole.scrollDown()
        elif event.type == KEYUP:
            if event.key == K_BACKSPACE:
                game.gameConsole.backspaceHoldingReset()