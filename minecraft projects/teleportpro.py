import time , mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

time.sleep(3)
mc.postToChat("Teleporting in 3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1, commencing teleportation")
time.sleep(1)

while True:

    mc.player.setPos(0,10,60)

    time.sleep(2)

    mc.player.setPos(10,20,40)

    time.sleep(2)

    mc.player.setPos(50,10,50)

    time.sleep(2)


