import mcpi.minecraft as minecraft #imports mcpi.minecraft and calls it minecraft
import time #imports time
import random #imports random
mc = minecraft.Minecraft.create() #gives minecraft.Minecraft.create() the name mc

while True: #creates an infinite loop
    pos = mc.player.getPos() #gets player's position
    x = int(pos.x)
    print x
    y = pos.y
    print y
    z = int(pos.z)
    print z

    Block = 13 #gives 13 (the block ID) the name Block

    x = random.randint(x-10,x+10)
    z = random.randint(z-10,z+10)
    mc.setBlock(x, y+50, z, Block) #places a block of gravel above the player
    time.sleep(0.2) #pauses for 2/10 of a second
                
