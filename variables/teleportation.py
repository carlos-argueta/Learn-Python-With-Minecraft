# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Coordinates to teleport to
x = 1090
y = 110
z = -456

# Teleport the player
mc.player.setTilePos(x, y, z)