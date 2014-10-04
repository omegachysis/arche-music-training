#!/usr/bin/env python3

import arche

# Create a logging object for this program
log = arche.debug.log("main")

def main():
    # Log the successful loading of the main program
    log.info("starting music-training")

    game = arche.Game(width = 1280, height = 800,
                      fullscreen = True,
                      titleName = "Arche Music Training")

    game.run()

if __name__ == "__main__":
    arche.debug.test(main)