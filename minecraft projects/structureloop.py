import mcpi.minecraft as minecraft #imports mcpi.minecraft and calls it minecraft
import time #imports time
mc = minecraft.Minecraft.create() #gives minecraft.Minecraft.create() the name mc

time.sleep(5) #pauses for 5 seconds

for location in (0,2,4,6,8,10):
    mc.setBlock(location,0,0,22)
    time.sleep(2)

time.sleep(5)

for height in (-1,15,12,40,65,0):
    mc.setBlock(10,height,10,22)
    time.sleep(2)

time.sleep(5)

for step in (0,1,2,3,4,5,6,7,8,9,10):
    mc.setBlock(0,step,step,22)
    time.sleep(2)

time.sleep(5)

for step in range(11):
    mc.setBlock(30,step,step,22)
    time.sleep(2)

time.sleep(5)

for step in range(5,11):
    mc.setBlock(40,step,step,22)
    time.sleep(2)
