import mcpi.minecraft as minecraft
import time
import random
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getPos()
    x = int(pos.x)
    print x
    y = pos.y
    print y
    z = int(pos.z)
    print z

    Block = 13

    x = random.randint(x-10,x+10)
    z = random.randint(z-10,z+10)
    mc.setBlock(x, y+50, z, Block)
    time.sleep(0.2)
                
