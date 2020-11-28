from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
username = input("請輸入姓名:")
message = input("請輸入發言: ")
mc.postToChat("<"+username + "> "+message)

