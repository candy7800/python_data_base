import pygame as pg
import random,pyautogui as pag
init = pg.init()
width = 600
height = 600
window = pg.display.set_mode((width, height))
pg.display.set_caption('my_game')
# colors...
C_BWRGBYCM = [(0,0,0),(255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(255, 0, 255)]

# game_variables...
exit_game = False
clock = pg.time.Clock()
fps = 1000
points = []
for i in range(100):
    points.append([int(random.randint(0,width))-200,int(random.randint(0,height))-100,int(random.randint(0,height)),C_BWRGBYCM[random.randint(0,7)]])
    # points.append([int(300)-200,int(200)-100,int(350),C_BWRGBYCM[4]])
    # points.append([int(301)-200,int(200)-100,int(350),C_BWRGBYCM[1]])
dt = 0.000001
update = 0
dx = dy = dz = 0
size = 0.5

a_ = 10*size
p_ = 28*size
b_ = 9/8*size
def cir(v):
    # print(v)
    pg.draw.circle(window, v[3], (int(v[2]),int(v[1])), 1, 1)
def val(l,a_,p_,b_):
    x,y,z,c = l
    dx = (a_*(y-x))*dt
    dy = (x*(p_-z)-y)*dt
    dz = (x*y-b_*z)*dt
    
    # dy = (-y*(1-x**2))*dt
    # dx = (x*(4-y)+3*z)*dt
    
    # dz = (-x*(5-1*z)-5*z)*dt
    # dz = (p_ + a_*z-(z**3/3)-(x**2+y**2)*(1+0*z))*dt

    l[0] += dx
    l[1] -= dy
    l[2] += dz
    return l
# game main loop...
while 1:
    # if update > 2000:
    #     update = 0
        # window.fill(C_BWRGBYCM[0])
    # window.fill(C_BWRGBYCM[0])
    for event in pg.event.get():
        if event.type==pg.QUIT:
            exit_game = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                loop()
            if event.key == pg.K_ESCAPE:
                quit()
    for i in range(len(points)):
        points[i] = val(points[i],a_,p_,b_)
        cir(points[i])
# enter your code hear...
    pg.display.update()
    clock.tick(fps)
    # update += 1
# end_of_the_code...
pg.quit()
quit()