import mcpi.minecraft as minecraft #imports mcpi.minecraft and calls it minecraft
import time #imports time
mc = minecraft.Minecraft.create() #gives minecraft.Minecraft.create() the name mc

while True: #creates an infinite loop
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    Block = 41 #gives 41 (the item ID) the name Block

    mc.setBlock(x,y-1,z,Block) # places a block of gold (Block) underneath your feet
    time.sleep(0.2) #pauses for 2/10 of a second
