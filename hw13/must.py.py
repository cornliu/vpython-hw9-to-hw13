from vpython import *
from numpy import * 
 
N = 100
R, lamda = 1.0, 500E-9
d = 100E-6 
k = 2 * pi / lamda
dx, dy = d/N, d/N
scene1 = canvas(align = 'left', height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene2 = canvas(align = 'right', x=600, height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene1.lights, scene2.lights = [], []
scene1.ambient, scene2.ambient = color.gray(0.99), color.gray(0.99)
side = linspace(-0.01*pi, 0.01*pi, N)
x,y = meshgrid(side,side)
E_field = zeros((N,N))
XY = linspace(-10E-4,10E-4, 1000)
for X in XY:
    for Y in XY:
        if X**2 + Y**2 <= (d/2)**2:
            E_field += cos((X*x+Y*y)*k/R)/R/2 *dx*dy
qqq = abs(E_field) ** 2
maxI = amax(qqq)
for i in range(N):
    for j in range(N):
        box(canvas = scene1, pos=vector(i*dx, j*dy, 0), length = dx,height= dy,width = dx,color=vector(qqq[i,j]/maxI,qqq[i,j]/maxI,qqq[i,j]/maxI) )        
for i in range(50,0,-1):
    if qqq[i,50] <= maxI/100:
        theta = atan((x[50][50]-x[50][i])/R)
        print('theta = ',theta)
        break
print('理論值' , asin(1.22*lamda/d))
qqq = abs(E_field)
maxI = amax(qqq)
for i in range(N):
    for j in range(N):
        box(canvas = scene2, pos=vector(i*dx, j*dy, 0),length = dx,height= dy,width = dx,color=vector(qqq[i,j]/maxI,qqq[i,j]/maxI,qqq[i,j]/maxI) )   



    

