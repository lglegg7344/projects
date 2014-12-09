import mcpi.minecraft as minecraft
import time
import random
mc = minecraft.Minecraft.create()

spruce = 1

mc.setBlocks(-30,-5,-30,30,30,30,0)

mc.setBlocks(1,0,1,5,6,7,5,spruce)
mc.setBlocks(2,1,2,4,5,6,0)
mc.setBlocks(3,1,1,3,2,2,0)

mc.setBlocks(2,6,2,4,6,6,20)




