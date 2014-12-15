# Basic Teleporter in minecraft-pi


import mcpi.minecraft as mc, time #adds mcpi module and the option of time
mc = mc.Minecraft.create() #connects to a minecraft game and calls it game

time.sleep(10) #pauses for 10 seconds
mc.postToChat("hello world") #adds option to chat in-game

time.sleep(2) #pauses for 2 seconds

mc.postToChat("I hope you enjoy your world") #posts "I hope you enjoy your world" onto your game

mc.player.setPos(5,10,20) #moves the player to the coordinates of 5,10,20
