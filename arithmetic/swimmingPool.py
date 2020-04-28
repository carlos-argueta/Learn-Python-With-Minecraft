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

# Define the dimensions of the pool
d = 3
# The width is twice the depth
w = d * 2
# The length to be three times to depth
l = d * 4

# Define the block types
block_type = 4
water = 9

# Build the outer walls of the pool
mc.setBlocks(x , y - 1 , z, x + w - 1, y - 1 - d + 1, z + l - 1, block_type)

# Replace part of the solid cuboid (pool walls) with a water cuboid
mc.setBlocks(x + 1 , y - 1 , z + 1, x + w - 1 - 1, y - 1 - d + 1 + 1, z + l - 1 - 1, water)
