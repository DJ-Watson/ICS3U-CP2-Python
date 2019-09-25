#!/usr/bin/env python3

# Created by DJ Watson
# Created on September 2019
# This program draws a background on PyBadge

import ugame
import stage

# image bank
bank_1 = stage.Bank.from_bmp16("ball.bmp")

def main():
    # set background to image 0 in bank
    background = stage.Grid(bank_1, 10, 8)
    # changes image to third image
    background.tile(4, 3, 3)

    # creates stage for background to show up on
    # sets game to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = [background]
    # render
    game.render_block()

    while True:

        pass

if __name__ == "__main__":
    main()