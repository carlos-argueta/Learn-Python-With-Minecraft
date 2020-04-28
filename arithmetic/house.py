# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Get player's position
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

# Pause to give time to return to the game
time.sleep(3)

# Define cuboid dimensions
width = 20 # this is in x
height = 7 # this is in y
length = 10 # this is in z

# Define the block type
block_type = 4 # cobblestoneÐ
air = 0

# Build the cuboid with setBlocks
mc.setBlocks(x, y, z, x + width - 1, y + height - 1, z + length - 1, block_type)

# Build an air cuboid to empty the inside of the house
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1 - 1, y + height - 1 - 1, z + length - 1 - 1, air)

# Build the door
dw = 2
dh = 3
dl = 1
mc.setBlocks(x + width/2 - dw/2, y, z, x + width/2 + dw/2 - 1, y + dh - 1, z + dl - 1, air)

# Build the right window
ww = 2
wh = 2
wl = 1
mc.setBlocks(x + 1 , y + 4, z, x + 1 + ww - 1 , y + 4 + wh - 1 , z - wl - 1 , air)

# Build the left window
mc.setBlocks(x + width - 1 - ww , y + 4, z, x + width - 1 - 1 , y + 4 + wh - 1 , z - wl - 1 , air)



