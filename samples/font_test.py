import gaugette.ssd1306
import time
import sys

fonts = []

from gaugette.fonts import arial_16
from gaugette.fonts import arial_24
from gaugette.fonts import arial_32
fonts += [arial_16,
          arial_24,
          arial_32]

from gaugette.fonts import tahoma_16
from gaugette.fonts import tahoma_24
from gaugette.fonts import tahoma_32
fonts += [tahoma_16,
          tahoma_24,
          tahoma_32]

from gaugette.fonts import verdana_15
from gaugette.fonts import verdana_24
from gaugette.fonts import verdana_32

fonts += [verdana_15,
          verdana_24,
          verdana_32,
          ]

from gaugette.fonts import stencil_16
from gaugette.fonts import stencil_24
from gaugette.fonts import stencil_33
fonts += [stencil_16,
          stencil_24,
          stencil_33]

from gaugette.fonts import old_english_30
fonts += [old_english_30]

from gaugette.fonts import magneto_16
from gaugette.fonts import magneto_24
from gaugette.fonts import magneto_32
fonts += [magneto_16,
          magneto_24,
          magneto_32]

from gaugette.fonts import curlz_22
from gaugette.fonts import curlz_32
fonts += [curlz_22,
          curlz_32]

RESET_PIN = 15
DC_PIN    = 16

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN, buffer_cols=256)
led.begin()
led.clear_display()

offset = 0
while True:
    for font in fonts:
        row = (offset+32) % 64
        y = (32-font.char_height)/2
        led.clear_block(0,row,256,32)
        textSize = led.draw_text3(0,row+y,font.name,font)
        if textSize > 256:
            textSize = 256
            
        led.display()

        for scroll in range(0,32):
            offset = (offset+1) % 64
            led.command(led.SET_START_LINE | offset)
            time.sleep(0.01)

        if (textSize > 128):
            for scroll in range(0,textSize-128):
                led.col_offset = scroll
                led.display()
            time.sleep(0.5)
            for scroll in range(0,textSize-128):
                led.col_offset = textSize-128-1-scroll
                led.display()
        else:
            time.sleep(1.0)
