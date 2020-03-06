#connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# get the current location
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

# subtract 1 from y
y = y - 1

# place a grass block below the player
grass = 2
time.sleep(3)
mc.setBlock(x,y,z,grass)




