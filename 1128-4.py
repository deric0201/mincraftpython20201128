from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

long = 100 #
width =20 #寬
length =100 #高
blockid = 7
air = 0

mc.setBlocks(x,y,z,x+long,y+length,z+width,blockid)#外圍

mc.setBlocks(x+1,y+1,z+1,x+long-1,y+length-1,z+width-1,air) #裡面放空氣

mc.setBlocks(x,y+1,z+1,x,y+2,z+1,air)

mc.setBlocks(x+1,y+length-1,z+1,x+long-1,y+length-1,z+width+1,169)

mc.setBlocks(x+1,y+length/2,z+1,x+long-1,y+length/2,z+width-1,169)

mc.setBlocks(x+2,y+length/2,z+2,x+long-2,y+length/2,z+width-2,air)