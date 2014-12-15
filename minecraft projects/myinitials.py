import mcpi.minecraft as minecraft #imports mcpi.minecraft and calls it minecraft
import time #imports time
import random #imports random
mc = minecraft.Minecraft.create() #gives minecraft.Minecraft.create() the name mc

mc.setBlocks(-30,-5,-30,30,30,30,0) #clears an area to build on

orange = 1 #gets the block with the item ID of 1 and gives it the name "orangeW
lime = 5 #gets the block with the item ID of 5 and gives it the name "lime"


mc.setBlocks(3,3,-1,14,10,-1,35,orange #creates an orange background

#creates letter L
mc.setBlocks(4,4,0,4,9,0,35,lime)
mc.setBlocks(4,4,0,7,4,0,35,lime)

#creates letter G
mc.setBlocks(9,5,0,9,8,0,35,lime)
mc.setBlocks(10,4,0,12,4,0,35,lime)
mc.setBlocks(10,9,0,12,9,0,35,lime)
mc.setBlocks(13,8,0,13,8,0,35,lime)
mc.setBlocks(13,5,0,13,6,0,35,lime)
mc.setBlocks(12,6,0,12,6,0,35,lime)
