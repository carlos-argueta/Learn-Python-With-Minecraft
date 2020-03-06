# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Coordinates to teleport to
x = -345
y = 110
z = -892

# Teleport the player
mc.player.setTilePos(x, y, z)
message = "Player teleported to (x,y,z) = ("+str(x)+","+str(y)+","+str(z)+")"
mc.postToChat(message)



