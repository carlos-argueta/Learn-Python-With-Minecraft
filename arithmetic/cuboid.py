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
width = 2 # this is in x
height = 15 # this is in y
length = 2 # this is in z

# Define the block type
block_type = 4 # cobblestoneÐ

# Build the cuboid with setBlocks
mc.setBlocks(x, y, z, x + width - 1, y + height - 1, z + length - 1, block_type)





