import random
import pygame as pg
import perlin
import matplotlib.pyplot as plt
# class perlin:
#     def __init__(self, fre):
#         if fre<2:
#             return 0
#         self.fre=fre
#         self.lb=0
#         self.int_size=100
#         self.grad=[random.uniform(-1,1) for _ in range(fre)]
#     def value_at(self,t):
#         if t<self.lb:return print('t<=0')
#         discarded=int(self.lb/self.int_size)
#         while t>=(len(self.grad)-1+discarded)*self.int_size:
#             self.grad.append(random.uniform(-1,1))
#         numOfint=int(t/self.int_size)
#         a1=self.grad[numOfint-discarded]
#         a2=self.grad[numOfint+1-discarded]
#         amt = self.__ease((t-numOfint*self.int_size)/self.int_size)
#         return self.__lerp(a1,a2,amt)
#     def discard(self,amount):
#         toDis=int((amount+self.lb%self.int_size)/self.int_size)
#         self.grad=self.grad[todis:]
#         self.lb+=amt
#     def __ease(self,x): return 6*x**5-15*x**4+10*x**3
#     def __lerp(self,start,stop,amt):
#         return amt*(stop-start)+start
# noise=perlin(15)
noise=perlin.perlin(15)
# values=[noise.value_at(i) for i in range(0,4000,2)]
width,height,C_BWRGBYCM=200,200,((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
window=pg.display.set_mode((width, height))
def event_check():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
maper = lambda vari,minV,maxV,minO,maxO:(vari-minV)/(maxV-minV)*(maxO-minO)+minO
pixel=pg.PixelArray(window)
while 1:
    event_check()
    for i in range(0,width):
        for j in range(0,height):
            col=maper(noise.two(i,j),-40,40,0,255)
            pixel[i][j]=(col,col,col)

        
