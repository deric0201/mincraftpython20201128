from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

try:
    block = int(input('請問你要什麼方塊:'))
    mc.setBlock(x+1,y,z,block)
