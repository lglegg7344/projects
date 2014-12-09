import mcpi.minecraft as minecraft
import time
import random
mc = minecraft.Minecraft.create()

def house(x,y,z):
    
    spruce = 1

    mc.setBlocks(x+1,y+0,z+1,x+5,y+6,z+7,5,spruce)
    mc.setBlocks(x+2,y+1,z+2,x+4,y+5,z+6,0)
    mc.setBlocks(3,1,1,3,2,2,0)

    mc.setBlocks(x+2,y+6,z+2,x+4,y+6,z+6,20)

    time.sleep(5)

house(20,0,20)
house(30,0,30)
house(40,0,40)



