# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Coordinates to teleport to
 y = 110
z = -892

# Teleport the player
mc.postToChat(Ready to teleport)
mc.player.setTilePos(x, y, z)
message = "Player teleported to (x,y,z) = ("+x+","+y+","+z+")"
mc.postToChat(message)



