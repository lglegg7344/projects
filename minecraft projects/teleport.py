### Basic Teleporter in minecraft-pi


import mcpi.minecraft as mc, time #adds mcpi module and the option of time
mc = mc.Minecraft.create() #connects to a minecraft game and calls it game

time.sleep(10)
mc.postToChat("hello world") #adds option to chat in-game

time.sleep(2)

mc.postToChat("I hope you enjoy your world")

mc.player.setPos(5,10,20)
