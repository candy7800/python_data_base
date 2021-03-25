import pygame as pg
import math
width,height = 1000, 500
window = pg.display.set_mode((width, height))
# colors...
C_BWRGBYCM = [(0,0,0),(255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(255, 0, 255)]
def cir(pos,color):pg.draw.circle(window,C_BWRGBYCM[color],(int(pos[0]),int(pos[1])),1,0)
def line(a,b,c):pg.draw.line(window,C_BWRGBYCM[c],a,b)
def line2(a,b,c):pg.draw.line(window,c,a,b)
def wave(angle,length):return math.sin(angle)*length+height/2
def wave2(angle,length):return math.cos(angle)*length+height/2
def wave3(angle,length):return math.tan(angle)*length+height/2
def wave4(angle,length):return -math.sin(angle)*length+height/2
def wave5(angle,length):return -math.cos(angle)*length+height/2
def wave6(angle,length):return -math.tan(angle)*length+height/2
def wave7(angle,length):return 1/math.sin(angle)*length+height/2
def wave8(angle,length):return 1/math.cos(angle)*length+height/2
def wave9(angle,length):return 1/math.tan(angle)*length+height/2
# game_variables...
clock = pg.time.Clock()
fps = 40
points = []
points2 = []
points3 = []
points4 = []
points5 = []
points6 = []
points7 = []
points8 = []
points9 = []
numbers_of_point = 800
x = 5
a = 0
for i in range(numbers_of_point):
    points.append([int(x),int(height/2)])
    x+=width/numbers_of_point
x = 5
for i in range(numbers_of_point):
    points2.append([int(x),int(height/2)])
    x+=width/numbers_of_point
x = 5
for i in range(numbers_of_point):
    points3.append([int(x),int(height/2)])
    x+=width/numbers_of_point
x = 5
for i in range(numbers_of_point):
    points4.append([int(x),int(height/2)])
    x+=width/numbers_of_point
x = 5
for i in range(numbers_of_point):
    points5.append([int(x),int(height/2)])
    x+=width/numbers_of_point
x = 5
for i in range(numbers_of_point):
    points6.append([int(x),int(height/2)])
    x+=width/numbers_of_point
x = 5
for i in range(numbers_of_point):
    points7.append([int(x),int(height/2)])
    x+=width/numbers_of_point
x = 5
for i in range(numbers_of_point):
    points8.append([int(x),int(height/2)])
    x+=width/numbers_of_point
x = 5
for i in range(numbers_of_point):
    points9.append([int(x),int(height/2)])
    x+=width/numbers_of_point
x = 5
s=c=t=d=v=y=z=x=r=1
p=int((height/2)-10)
# game main loop...
while 1:
    window.fill(C_BWRGBYCM[0])
    q,w=pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                s+=1
            if event.key == pg.K_c:
                c+=1
            if event.key == pg.K_t:
                t+=1
            if event.key == pg.K_d:
                d+=1
            if event.key == pg.K_v:
                v+=1
            if event.key == pg.K_y:
                y+=1
            if event.key == pg.K_z:
                z+=1
            if event.key == pg.K_x:
                x+=1
            if event.key == pg.K_r:
                r+=1
            if event.key == pg.K_RIGHT:
                p-=10
            if event.key == pg.K_LEFT:
                p+=10
            if event.key == pg.K_ESCAPE:
                quit()

# enter your code hear...
    if s%2==0:
        for no,point in enumerate(points):
            # cir(point,5)
            point[1]=wave(a+no/(q/10),p)
            if no!=0:
                line(point,points[no-1],3)
    if c%2==0:
        for no,point in enumerate(points2):
            # cir(point,5)
            point[1]=wave2(a+no/(q/10),p)
            if no!=0:
                line(point,points2[no-1],2)
    if t%2==0:
        for no,point in enumerate(points3):
            # cir(point,5)
            point[1]=wave3(a+no/(q/10),p)
            if no!=0:
                line(point,points3[no-1],1)
    if d%2==0:
        for no,point in enumerate(points4):
            # cir(point,5)
            point[1]=wave4(a+no/(q/10),p)
            if no!=0:
                line(point,points4[no-1],5)
    if v%2==0:
        for no,point in enumerate(points5):
            # cir(point,5)
            point[1]=wave5(a+no/(q/10),p)
            if no!=0:
                line(point,points5[no-1],6)
    if y%2==0:
        for no,point in enumerate(points6):
            # cir(point,5)
            point[1]=wave6(a+no/(q/10),p)
            if no!=0:
                line(point,points6[no-1],7)
    if z%2==0:
        for no,point in enumerate(points7):
            # cir(point,5)
            point[1]=wave7(a+no/(q/10),p)
            if no!=0:
                line(point,points7[no-1],4)
    if x%2==0:
        for no,point in enumerate(points8):
            # cir(point,5)
            point[1]=wave8(a+no/(q/10),p)
            if no!=0:
                line2(point,points8[no-1],(150,150,255))
    if r%2==0:
        for no,point in enumerate(points9):
            # cir(point,5)
            point[1]=wave9(a+no/(q/10),p)
            if no!=0:
                line2(point,points9[no-1],(150,255,150))
    pg.display.update()
    clock.tick(fps)
    a+=w/1000
# end_of_the_code...
pg.quit()
quit()