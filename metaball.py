import pygame as pg
from math import *
from random import *
width,height,C_BWRGBYCM=400,400,((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
window=pg.display.set_mode((width, height))
def event_check():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
max_vel=5
cir = lambda pos,color,radi:pg.draw.circle(window,C_BWRGBYCM[color],(int(pos[0]),int(pos[1])),radi,0)
objec=[[randint(0,width),randint(0,height),randint(-max_vel,max_vel),randint(-max_vel,max_vel)] for i in range(2000)]
maper = lambda vari,minV,maxV,minO,maxO:(vari-minV)/(maxV-minV)*(maxO-minO)+minO
pixel=tuple(pg.PixelArray(window))
while 1:
	event_check()
	window.fill(C_BWRGBYCM[0])
	schem=[[0 for y in range(0,width)] for x in range(0,width)]
	for point in objec:
		for x in range(0,width):
			for y in range(0,height):
				dis=dist((point[0],point[1]),(x,y))
				if dis<=55:col=int(maper(dis,0,55,55,0))
				else:col=0
				schem[x][y]+=col
				# pixel[x][y]=(col,col,col)
		point[0]+=point[2]
		point[1]+=point[3]
		if point[0]<=0:point[2]*=-1
		elif point[0]>=width:point[2]*=-1
		elif point[1]<=0:point[3]*=-1
		elif point[1]>=height:point[3]*=-1
	for x in range(0,width):
		for y in range(0,height):
			if schem[x][y]<=255:pixel[x][y]=(schem[x][y],schem[x][y],schem[x][y],)
		else:pixel[x][y]=C_BWRGBYCM[1]

# while 1:
# 	event_check()
# 	q,w=pg.mouse.get_pos()
# 	window.fill(C_BWRGBYCM[0])
# 	for x in range(0,width):
# 		for y in range(0,height):
# 			dis=dist((q,w),(x,y))
# 			if dis<=50:col=int(maper(dis,0,50,150,0))
# 			else:col=0
# 			pixel[x][y]=(col,col,col)