import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()


while True:
        pPos = mc.player.getPos()

        x = pPos.x
        y = pPos.y
        z = pPos.z

        Block = 0
        mc.setBlocks(x+1,y,z+1,x-1,y+1,z-1,Block)
        time.sleep(0.2)
