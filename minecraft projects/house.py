import mcpi.minecraft as minecraft #imports mcpi.minecraft and calls it minecraft
import time #imports time
import random #imports random
mc = minecraft.Minecraft.create() #gives minecraft.Minecraft.create() the name mc

spruce = 1 #gets the block with the item ID of 1 and calls it spruce

mc.setBlocks(-30,-5,-30,30,30,30,0) #clears an area to build a house

mc.setBlocks(1,0,1,5,6,7,5,spruce) #creates a solid block of spruce planks
mc.setBlocks(2,1,2,4,5,6,0) #hollows out the block
mc.setBlocks(3,1,1,3,2,2,0) #creates a doorway

mc.setBlocks(2,6,2,4,6,6,20) #creates a window




