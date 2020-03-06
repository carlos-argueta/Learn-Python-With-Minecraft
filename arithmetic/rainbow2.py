# wool 35
# red 14
# orange 1
# yellow 4
# green 13
# blue 11
# purple 10

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Define the starting position
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

wool = 35
# Place the purple wool at original x
mc.setBlock(x, y - 1, z, wool,10)
mc.setBlock(x + 1, y, z, wool,10)
mc.setBlock(x + 2, y - 1, z, wool,10)

# Increase y to place next block above
y = y + 1

# Place the blue wool
mc.setBlock(x, y - 1, z, wool,11)
mc.setBlock(x + 1, y, z, wool,11)
mc.setBlock(x + 2, y - 1, z, wool,11)

# Increase y to place next block above
y = y + 1

# Place the green wool
mc.setBlock(x, y - 1, z, wool,13)
mc.setBlock(x + 1, y, z, wool,13)
mc.setBlock(x + 2, y - 1, z, wool,13)

# Increase y to place next block above
y = y + 1

# Place the yellow wool
mc.setBlock(x, y - 1, z, wool,4)
mc.setBlock(x + 1, y, z, wool,4)
mc.setBlock(x + 2, y - 1, z, wool,4)

# Increase y to place next block above
y = y + 1

# Place the orange wool
mc.setBlock(x, y - 1, z, wool,1)
mc.setBlock(x + 1, y, z, wool,1)
mc.setBlock(x + 2, y - 1, z, wool,1)

# Increase y to place next block above
y = y + 1

# Place the red wool block
mc.setBlock(x, y - 1, z, wool,14)
mc.setBlock(x + 1, y, z, wool,14)
mc.setBlock(x + 2, y - 1, z, wool,14)










