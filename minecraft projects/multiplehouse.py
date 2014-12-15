import mcpi.minecraft as minecraft #imports mcpi.minecraft and calls it minecraft
import time #imports time
import random #imports random
mc = minecraft.Minecraft.create() #gives minecraft.Minecraft.create() the name mc

def house(x,y,z): #defines house
    
    spruce = 1 #gets the block with the item ID of 1 and calls it spruce

    mc.setBlocks(x+1,y+0,z+1,x+5,y+6,z+7,5,spruce) #creates a solid block of spruce planks
    mc.setBlocks(x+2,y+1,z+2,x+4,y+5,z+6,0) #hollows out the block
    mc.setBlocks(3,1,1,3,2,2,0) #creates a doorway

    mc.setBlocks(x+2,y+6,z+2,x+4,y+6,z+6,20) #creates a window

    time.sleep(5) #pauses for 5 seconds

house(20,0,20) #builds a house at the coordinates of 20,0,20
house(30,0,30) #builds another house 10 blocks away
house(40,0,40) #builds another house 20 blocks away from the first



