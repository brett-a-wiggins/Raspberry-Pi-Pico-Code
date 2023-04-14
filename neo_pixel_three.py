import neopixel
import time
from machine import Pin
import random
import sys

p = Pin(0,Pin.OUT)
n = neopixel.NeoPixel(p, 5)

for i in range(5):
    n[i] = (0,100,0)
    n.write()
    time.sleep(.5)


class Player(object):
    def __init__(self, player_name):
        self.player_name  = player_name
        self.inventory = []
        self.direction = "North"
        self.health = 4
        
    def fight(self, monster):
        print(f"You are about to fight {monster}")
        
        
        print(f"{monster} attacks and inflicts 1 damage")
        damage_function(self.health)
        self.health = self.health -1
        
        if(self.health < 0):
            print("You died.")
            sys.exit()
        
    def move(self, direction, distance):
        print(f"You have moved {distance} in a {direction} direction")
        direction = direction
    
    def pick_up_item(self,item):
        print(f"You picked up {item}")
        self.inventory.append(item)
        print(f"{item} has been placed in your inventory")
        
    def drop_item(self,item):
        inventory.remove(item)
        print(f"You have dropped {item}")
        
    def use_item(self, item):
        print(f"You are about to use {item}")
        if item == "health_potion":
            self.health = self.health + 1
            heal_function(self.health)
            

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

def heal_function(health_points):
    
    n[health_points] = (0,100,0)
    n.write()
    time.sleep(.5)
    n[health_points] = (0,0,0)
    n.write()
    time.sleep(.5)
    n[health_points] = (0,100,0)
    n.write()

name = input("Please enter your name: ")
player_one = Player(name)
print(f"Welcome to the game {player_one.player_name}")
print(f"""
You find yourself in a dark hallway facing {player_one.direction}. There are
walls to your left or right. In front of you is the dark abyss. What direction
do you want to go in?
""")
direction = input("Which direction do you want to go in? ")
distance = input("How far do you want to walk? ")

player_one.move(direction,distance)

choice = input("You come face to face with a Monster. Do you want to fight or run?")

if choice.lower() == "fight":
    player_one.fight("Gerry")
else:
    print("You run away!")
    
print("""
In the darkness you stumble on an item. It's a health potion! Do you want
to pick it up?
""")
choice = input()

if choice.lower() == "y" or choice.lower() == "yes":
    player_one.pick_up_item("health_potion")
else:
    print(f"You walk past the health potion without a thought.")
    
if player_one.health < 4:
    print("You notice your health is low. Do you want to use the health potion?")
    choice = input()
    if choice.lower() == "y" or choice.lower == "yes":
        player_one.use_item("health_potion")
    else:
        print("You stash the potion in your backpack for future use.")




