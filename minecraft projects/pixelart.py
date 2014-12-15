#imports all needed
import mcpi.minecraft as minecraft
import time
#renames minecraft.Minecraft.create() as mc
mc = minecraft.Minecraft.create()

#giving the item ID the name of the colour
red = 14
black = 15

#clears out an area for the space invader to be built
mc.setBlocks(-30,-5,-30,30,60,30,0)

#makes a black background
mc.setBlocks(0,-1,0,12,9,0,35,black)

#builds the space invader
for location in (4,5,7,8):
    mc.setBlock(location,0,0,35,red)
for location in (1,3,9,11):
    mc.setBlock(location,+1,0,35,red)    
for location in (1,3,4,5,6,7,8,9,11):
    mc.setBlock(location,+2,0,35,red)
for location in (1,2,3,4,5,6,7,8,9,10,11):
    mc.setBlock(location,+3,0,35,red)
for location in (2,3,5,6,7,9,10):
    mc.setBlock (location,+4,0,35,red)
for location in (3,4,5,6,7,8,9):
    mc.setBlock(location,+5,0,35,red)
for location in (4,8):
    mc.setBlock(location,+6,0,35,red)
for location in (3,9):
    mc.setBlock(location,+7,0,35,red)
