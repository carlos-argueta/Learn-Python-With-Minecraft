# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

# Coordinates to teleport to
x = -885
y = 106
z = 197

location = "Snowy Bridge"
message = "This is a very cool natural bridge"

# Teleport the player
mc.player.setTilePos(x, y, z)
mc.postToChat(location)
mc.postToChat(message)

time.sleep(10)


# Coordinates to teleport to
x = -150
y = 63
z = 240

location = "Green Grass Lake"
message = "The water looks so fresh"

# Teleport the player
mc.player.setTilePos(x, y, z)
mc.postToChat(location)
mc.postToChat(message)

time.sleep(10)

# Coordinates to teleport to
x = -101
y = 69
z = 62

location = "Lava Waterfall"
message = "Don't get too close, it is very hot."

# Teleport the player
mc.player.setTilePos(x, y, z)
mc.postToChat(location)
mc.postToChat(message)


