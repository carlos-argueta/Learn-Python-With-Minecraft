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
# Perform the jump
mc.player.setTilePos(x, y + 5, z)
# Block id for water
water = 11
# Original x, z
mc.setBlock(x, y - 1, z, water)
# Front of the player
mc.setBlock(x, y - 1, z + 1, water)
# Back of player
mc.setBlock(x, y - 1, z - 1, water)
# Left of the player
mc.setBlock(x + 1, y - 1, z, water)
# Right of the player
mc.setBlock(x - 1, y - 1, z, water)
# Left forward of the player
mc.setBlock(x + 1, y - 1, z + 1, water)
# Left backward of the player
mc.setBlock(x + 1, y - 1, z - 1, water)
# Right forward of the player
mc.setBlock(x - 1, y - 1, z + 1, water)
# Right back of the player
mc.setBlock(x - 1, y - 1, z - 1, water)
