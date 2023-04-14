import neopixel
import time
from machine import Pin

p = Pin(0,Pin.OUT)
n = neopixel.NeoPixel(p, 5)

for i in range(5):
    n[i] = (0,100,0)
    n.write()
    time.sleep(.5)

health = 4

def damage_function(health_points):
    n[health_points] = (100,0,0)
    n.write()
    time.sleep(.5)
    n[health_points] = (0,0,0)
    n.write()
    time.sleep(.5)
    n[health_points] = (100,0,0)
    n.write()
    time.sleep(.5)
    n[health_points] = (0,0,0)
    n.write()


damage_function(health)
health = health - 1
damage_function(health)
