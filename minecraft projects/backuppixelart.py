import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

red = 14
orange = 1
blue = 3
lime = 5
cyan = 9

mc.setBlocks(-30,-5,-30,30,60,30,0)

while True: #creates infinite loop

    #creates red space invader.
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

    time.sleep(2)

    #creates same as above, but in orange.
    for location in (4,5,7,8):
        mc.setBlock(location,0,0,35,orange)
    for location in (1,3,9,11):
        mc.setBlock(location,+1,0,35,orange)
    for location in (1,3,4,5,6,7,8,9,11):
        mc.setBlock(location,+2,0,35,orange)
    for location in (1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(location,+3,0,35,orange)
    for location in (2,3,5,6,7,9,10):
        mc.setBlock(location,+4,0,35,orange)
    for location in (3,4,5,6,7,8,9):
        mc.setBlock(location,+5,0,35,orange)
    for location in (4,8):
        mc.setBlock(location,+6,0,35,orange)
    for location in (3,9):
        mc.setBlock(location,+7,0,35,orange)

    time.sleep(2)

    #blue space invader
    for location in (4,5,7,8):
        mc.setBlock(location,0,0,35,blue)
    for location in (1,3,9,11):
        mc.setBlock(location,+1,0,35,blue)
    for location in (1,3,4,5,6,7,8,9,11):
        mc.setBlock(location,+2,0,35,blue)
    for location in (1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(location,+3,0,35,blue)
    for location in (2,3,5,6,7,9,10):
        mc.setBlock(location,+4,0,35,blue)
    for location in (3,4,5,6,7,8,9):
        mc.setBlock(location,+5,0,35,blue)
    for location in (4,8):
        mc.setBlock(location,+6,0,35,blue)
    for location in (3,9):
        mc.setBlock(location,+7,0,35,blue)

    time.sleep(2)
    
    #green/lime space invader
    for location in (4,5,7,8):
        mc.setBlock(location,0,0,35,lime)
    for location in (1,3,9,11):
        mc.setBlock(location,+1,0,35,lime)
    for location in (1,3,4,5,6,7,8,9,11):
        mc.setBlock(location,+2,0,35,lime)
    for location in (1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(location,+3,0,35,lime)
    for location in (2,3,5,6,7,9,10):
        mc.setBlock(location,+4,0,35,lime)
    for location in (3,4,5,6,7,8,9):
        mc.setBlock(location,+5,0,35,lime)
    for location in (4,8):
        mc.setBlock(location,+6,0,35,lime)
    for location in (3,9):
        mc.setBlock(location,+7,0,35,lime)
        
    time.sleep(2)

    #cyan space invader
    for location in (4,5,7,8):
        mc.setBlock(location,0,0,35,cyan)
    for location in (1,3,9,11):
        mc.setBlock(location,+1,0,35,cyan)
    for location in (1,3,4,5,6,7,8,9,11):
        mc.setBlock(location,+2,0,35,cyan)
    for location in (1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(location,+3,0,35,cyan)
    for location in (2,3,5,6,7,9,10):
        mc.setBlock(location,+4,0,35,cyan)
    for location in (3,4,5,6,7,8,9):
        mc.setBlock(location,+5,0,35,cyan)
    for location in (4,8):
        mc.setBlock(location,+6,0,35,cyan)
    for location in (3,9):
        mc.setBlock(location,+7,0,35,cyan)

    time.sleep(2)
