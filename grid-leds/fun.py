# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import logging
from random import randrange

import adafruit_dotstar
from adafruit_pixel_framebuf import PixelFramebuffer

from PIL import Image


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
#pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 256 

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

pixel_framebuf = PixelFramebuffer(
    pixels,
    16,
    16,
#    orientation="VERTICAL",
    reverse_x=True,
    rotation=1
#    top=0,
#    bottom=239
)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def color_cycle(color):
    for i in range(num_pixels):
        logging.warning("Setting pixel %s to %s", i, color)
        pixels[i] = color
    pixels.show()

def one_pixel_cycle(color):
    for j in range(num_pixels):
        for i in range(num_pixels):
            if i == j:
                k = num_pixels - 1 - i;
                #pixels[i] = (0,255,0)
                pixels[k] = (0,255,0)
                #logging.warning("Setting pixels %s and %s to %s", i, k, "floater")
                logging.warning("Setting pixel %s to %s", k, "floater")
            else:
                if i%2:
                    pixels[i] = (99,99,99)
                else:
                    pixels[i] = (99,99,99)
                logging.warning("Setting pixel %s to %s", i, "green")
        pixels.show()
        time.sleep(0.5)

def one_pixel_cycle_fill(color):
    for j in range(num_pixels):
        pixels.fill((0,0,255))
        for i in range(num_pixels):
            if i == j:
                k = num_pixels - 1 - i;
                pixels[i] = (255,165,0)
                pixels[k] = (255,165,0)
                logging.warning("Setting pixels %s and %s to %s", i, k, "floater")
                #logging.warning("Setting pixel %s to %s", k, "floater")
        pixels.show()
        time.sleep(0.1)

def kai_kai(evenOrOdd, r, g, b):
#     pixels.fill((255, 140, 0))
     for i in range(num_pixels):     
         if i%2 == evenOrOdd:
             pixels[i] = (r, g, b) 
             pixels.show()
#         time.sleep(1)


while True:
#     pixels.fill((255, 0, 0))
#     pixels.show()
#     time.sleep(1)
#     pixels.fill((0, 255, 0))
#     pixels.show()
#     time.sleep(1)
#     pixels.fill((0, 0, 255))
#     pixels.show()
#     time.sleep(1)
#     kai_kai(0, randrange(255), randrange(255), randrange(255)) #evens
#     time.sleep(1)
#     kai_kai(1, randrange(255), randrange(255), randrange(255)) #evens
#     time.sleep(1)


#     pixel_framebuf.line(0, 0, 7, 9, 0xFF0000)
#     pixel_framebuf.hline(2, 3, 5, 0xFF0000)
#     pixel_framebuf.vline(2, 3, 5, 0xFF0000)
#     pixel_framebuf.display()


#     image = Image.new("RGBA", (16, 16))
#     image = Image.open("egg-kai.jpg")
#     image.alpha_composite(icon)
#     pixel_framebuf.image(image.convert("RGB"))
#     pixel_framebuf.display()

     a = 16;
     b = 0;
     pixel_framebuf.text("Kai", b, 6, 0x00FF00)
     pixel_framebuf.display()
     pixel_framebuf.fill_rect(0, 12, 16, 4, 0xFF0000)
     pixel_framebuf.circle(3, 3, 2, 0x00008F)
     pixel_framebuf.circle(8, 3, 3, 0x0000FF)
     pixel_framebuf.circle(13, 3, 2, 0x0000AA)
     pixel_framebuf.display()
     time.sleep(1)
     while True:
         if a == 16:
             pixel_framebuf.circle(3, 3, 2, 0x00008F)
             pixel_framebuf.circle(8, 3, 3, 0x0000FF)
             pixel_framebuf.circle(13, 3, 2, 0x0000AA)
             pixel_framebuf.text("Kai", b, 6, 0x00FF00)
             pixel_framebuf.display()
             time.sleep(0.25)
             a = 0
         pixel_framebuf.scroll(0,-1)
         pixel_framebuf.display()
         time.sleep(0.25)
         a = a + 1


     break;
#     one_pixel_cycle_fill((255,0,0))
#    color_cycle((255,0,0))
#    time.sleep(2)

#    color_cycle((0,255,0))
#    time.sleep(2)

#    color_cycle((0,0,255))
#    time.sleep(2)
