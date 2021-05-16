import pygame as pg
from random import *
from math import *
pg.init()
width,height,C_BWRGBYCM=800,400,((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
window=pg.display.set_mode((width, height))
line = lambda a,b,color,width:pg.draw.line(window,C_BWRGBYCM[color],(int(a[0]),int(a[1])),(int(b[0]),int(b[1])),width)
cir = lambda pos,color,radi:pg.draw.circle(window,C_BWRGBYCM[color],(int(pos[0]),int(pos[1])),radi,0)
rect = lambda color,x,y,w,h:pg.draw.rect(window,(color,color,color),[int(x),int(y),int(w),int(h)])
maper = lambda vari,minV,maxV,minO,maxO:(vari-minV)/(maxV-minV)*(maxO-minO)+minO
vel=[0,0]
speed=1
shi=0
point = [200,200]
def check_line_colision(ray,def_line):
	x1,y1,x2,y2=def_line[0][0],def_line[0][1],def_line[1][0],def_line[1][1]
	x3,y3,x4,y4=ray[0][0],ray[0][1],ray[1][0],ray[1][1]
	den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
	if den == 0:return
	t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den
	u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den
	if 0<t<1 and u>0:
		return (int(x1+t*(x2-x1)),int(y1+t*(y2-y1)))
	return
def closest_point(frome,l_to):
	small_dis=1000
	nu=12
	for no,i in enumerate(l_to):
		dis=dist(frome,i)
		if dis<small_dis:
			small_dis=dis
			nu=no
	return l_to[nu]
	return None
def coliton_dot():
	point[0]+=vel[0]
	point[1]+=vel[1]
	if point[0]<0:point[0]=0
	elif point[0]>400:point[0]=400
	elif point[1]<0:point[1]=0
	elif point[1]>height:point[1]=height
	return
def event_check(shi):
	pg.display.update()
	clock.tick(fps)
	for event in pg.event.get():
	    if event.type==pg.QUIT:quit()
	    if event.type==pg.KEYDOWN:
	        if event.key==pg.K_ESCAPE:quit()
	        if event.key==pg.K_UP:vel[1]-=speed
	        if event.key==pg.K_DOWN:vel[1]+=speed
	        if event.key==pg.K_RIGHT:vel[0]+=speed
	        if event.key==pg.K_LEFT:vel[0]-=speed
	        if event.key==pg.K_w:shi+=0.1
	        if event.key==pg.K_s:shi-=0.1
	coliton_dot()
	return shi
clock = pg.time.Clock()
fps=400
lent=200
num_rays=1000
lines = [((randint(0,400),randint(0,height)),(randint(0,400),randint(0,height))) for i in range(2)]
lines.append(((1,1),(399,1)))
lines.append(((399,1),(399,399)))
lines.append(((399,399),(1,399)))
lines.append(((1,399),(1,1)))
values,distan=[],[]
while 1:
	shi = event_check(shi)
	point=list(pg.mouse.get_pos())
	window.fill(C_BWRGBYCM[0])
	gap = 2*pi/num_rays
	india=int(num_rays//pi/3)
	for rays in range(india):
		ang=gap*rays+shi
		nex_x,nex_y=int(sin(ang)*lent+point[0]),int(cos(ang)*lent+point[1])
		values.clear()
		for i in range(len(lines)):
			line(lines[i][0],lines[i][1],2,1)
			for lents in lines:
				temp=check_line_colision((point,(nex_x,nex_y)),lents)
				if temp==None:continue
				values.append(temp)
			if len(lines)>0:
				if len(values)>1:temp = closest_point(point,values)
				try:
					line(point,temp,4,1)
					distan.append(dist(point,temp))
				except:pass
	distan.reverse()
	for no,distances in enumerate(distan):
		width_box = 400/len(distan)
		h=maper(distances,0,566,200,0)
		rect(maper(distances,0,550,255,0),width_box*no+400,200-h,width_box,h*2)
	distan=[]
