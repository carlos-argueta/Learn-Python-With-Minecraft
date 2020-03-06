# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set the player's location
x = -39
y = 84
z = 79

# Set the first block
mc.setBlock(x, y, z, 45)

# Increase y
y = y + 1

# Set the second block
mc.setBlock(x, y, z, 45)

# Increase y
y = y + 1

# Set the third block
mc.setBlock(x, y, z, 45)

# Increase y
y = y + 1

# Set the fourth block
mc.setBlock(x, y, z, 45)


