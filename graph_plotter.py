import pygame as pg
from math import *
width,height,C_BWRGBYCM=400,400,((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
window=pg.display.set_mode((width, height))
def event_check():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
line = lambda a,b,color,width:pg.draw.line(window,C_BWRGBYCM[color],(int(a[0]),int(a[1])),(int(b[0]),int(b[1])),width)
maper = lambda vari,minV,maxV,minO,maxO:(vari-minV)/(maxV-minV)*(maxO-minO)+minO
val_bet=40
c=0
lis = []
for i in range(-200,200):
	lis.append([i+200,200])
while 1:
	event_check()
	window.fill(C_BWRGBYCM[0])
	line((200,0), (200,400), 2, 1)
	line((0,200), (400,200), 2, 1)
	line((100,0), (100,400), 4, 1)
	line((300,0), (300,400), 4, 1)
	for i in range(len(lis)):
		x=maper(lis[i][0],0,400,-val_bet,val_bet)
		try:lis[i][1]=log(int(maper(pg.mouse.get_pos()[0],0,400,0,10)),pg.mouse.get_pos()[1]+x) # enter your equation hear...
		except:pass
	for i in lis:
		i[1]=int(maper(i[1], -val_bet, val_bet, 400, 0))
	for no,i in enumerate(lis):
		try:
			if no!=0:line(i, lis[no-1], 3, 1)
		except:pass