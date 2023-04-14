import neopixel
import time
from machine import Pin

p = Pin(0,Pin.OUT)
n = neopixel.NeoPixel(p, 5)


# Draw a red gradient.
for i in range(5):
    n[i] = (12, 0, 0)
    time.sleep(.5)
    n.write()
    
    n[i] = (0,12,0)
    time.sleep(.5)
    n.write()
    
    n[i] = (0,0,12)
    time.sleep(.5)
    n.write()
    
# Update the strip.
#n.write()

for i in range(4,-1,-1):
    n[i] = (0,0,0)
    time.sleep(.5)
    n.write()