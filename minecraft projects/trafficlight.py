import mcpi.minecraft as minecraft,time as t
mc = minecraft.Minecraft.create()

#Move player close to origin
mc.player.setPos(10,20,10)

black=7
red=14
orange=1
green=5

while True:

    #Red light
    mc.setBlock(0,20,0,35,black)
    mc.setBlock(0,21,0,35,red)
    mc.setBlock(0,22,0,35,black)
    mc.setBlock(0,23,0,35,black)
    mc.setBlock(0,24,0,35,black)

    t.sleep(10)

    #Red and amber light
    mc.setBlock(0,20,0,35,black)
    mc.setBlock(0,21,0,35,red)
    mc.setBlock(0,22,0,35,orange)
    mc.setBlock(0,23,0,35,black)
    mc.setBlock(0,24,0,35,black)

    t.sleep(3)

    #Green light
    mc.setBlock(0,20,0,35,black)
    mc.setBlock(0,21,0,35,black)
    mc.setBlock(0,22,0,35,black)
    mc.setBlock(0,23,0,35,green)
    mc.setBlock(0,24,0,35,black)

    t.sleep(10)

    #Amber light
    mc.setBlock(0,20,0,35,black)
    mc.setBlock(0,21,0,35,black)
    mc.setBlock(0,22,0,35,orange)
    mc.setBlock(0,23,0,35,black)
    mc.setBlock(0,24,0,35,black)

    t.sleep(3)
