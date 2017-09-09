#!/usr/bin/env python

'''Unicorn HAT HD: GIF Displayer

This piece of software was made for the fantastic Unicorn Hat HD by Pimoroni: https://shop.pimoroni.com/products/unicorn-hat-hd

This script is based of: https://github.com/pimoroni/unicorn-hat-hd/blob/1dda39a1074d7676fc0c5f9a44037748d32219db/examples/show-png.py which was made by the Pimoroni Team

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License. (https://creativecommons.org/licenses/by-nc-sa/3.0/)

Press Ctrl+C to exit!

'''

import signal
import time
from sys import exit

try:
    from PIL import Image, ImageSequence
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhathd as unicorn

print("""
  _    _       _                        _    _       _     _    _ _____
 | |  | |     (_)                      | |  | |     | |   | |  | |  __ \\
 | |  | |_ __  _  ___ ___  _ __ _ __   | |__| | __ _| |_  | |__| | |  | |
 | |  | | '_ \\| |/ __/ _ \\| '__| '_ \\  |  __  |/ _` | __| |  __  | |  | |
 | |__| | | | | | (_| (_) | |  | | | | | |  | | (_| | |_  | |  | | |__| |
  \\____/|_|_|_|_|\\___\\___/|_|  |_| |_| |_| _|_|\\__,_|\\__| |_|  |_|_____/
   _____ _____ ______   _____
  / ____|_   _|  ____| |  __ \\(_)         | |
 | |  __  | | | |__    | |  | |_ ___ _ __ | | __ _ _   _  ___ _ __
 | | |_ | | | |  __|   | |  | | / __| '_ \\| |/ _` | | | |/ _ \\ '__|
 | |__| |_| |_| |      | |__| | \\__ \\ |_) | | (_| | |_| |  __/ |
  \\_____|_____|_|      |_____/|_|___/ .__/|_|\\__,_|\\__, |\\___|_|
                                    | |             __/ |
                                    |_|            |___/
""")

unicorn.rotation(0)
unicorn.brightness(0.2)

width, height = unicorn.get_shape()

print("Reading and processing frames...")

img = Image.open("bow.gif")

frames = [frame.copy().convert("RGBA") for frame in ImageSequence.Iterator(img)]

print("Playing animation...\nPress Ctrl+C to stop.")

try:
    while True:
        for im in frames:
            valid = False
            for x in range(width):
                for y in range(height):
                    pixel = im.getpixel((y, x))
                    r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                    if r or g or b:
                        valid = True
                    unicorn.set_pixel(x, y, r, g, b)
            if valid:
                unicorn.show()
                time.sleep((im.info["duration"] / 1000) - 0.02)
except KeyboardInterrupt:
    unicorn.off()
    print("\nStopped.")
