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

# Dimensions
base_height = 60
middle_height =  base_height / 2
top_height = base_height / 4

# Define the block type
block_type = 4 # cobblestone

# Build the base
mc.setBlocks(x, y, z, x + 9 - 1, y + base_height - 1, z + 9 - 1, block_type)
# Build the middle part
mc.setBlocks(x + 2, y + base_height , z + 2, x + 2 + 5 - 1, y + base_height + middle_height - 1, z + 2 + 5 - 1, block_type)
# Build the top
mc.setBlocks(x + 4, y + base_height + middle_height, z + 4, x + 4 + 1 - 1, y + base_height + middle_height + top_height - 1, z + 4 + 1 - 1, block_type)

