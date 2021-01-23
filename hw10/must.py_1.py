from vpython import*
import numpy as np

R ,r = 0.1 , 0.06
u0 = 4*pi*10**(-7)
m , n = 200 , 200
rz = 0.1

ring_R = list()
ring_r = list()
for i in range(n+1):
    ring_R.append(vec(R*cos(i/n*2*pi) ,R*sin(i/n*2*pi) ,0))
ring_R = np.array(ring_R)
for i in range(n+1):
    ring_r.append(vec(r*cos(i/n*2*pi) ,r*sin(i/n*2*pi) ,rz))
ring_r = np.array(ring_r)

aaa = 0
for i in range(m):
    distance = list()
    for j in range(n):
        distance.append(vec(r*i/m, 0, rz))
    distance = np.array(distance) - ring_R[:-1]
    lines = vec(0,0,0)
    for t in range(n):
        ds = ring_R[t+1] - ring_R[t]
        absolute_r = sqrt(dot(distance[t],distance[t]))
        ds_cross_r = cross(ds,distance[t])
        lines += u0/(4*pi)*(ds_cross_r/absolute_r**3)
    aaa += lines.z*2*pi*r*i/m*r/m

bbb = 0
for i in range(m):
    distance = list()
    for j in range(n):
        distance.append(vec(R*i/m, 0, 0))
    distance = np.array(distance) - ring_r[:-1]
    lines = vec(0,0,0)
    for t in range(n):
        ds = ring_r[t+1] - ring_r[t]
        absolute_R = sqrt(dot(distance[t],distance[t]))
        ds_cross_R = cross(ds,distance[t])
        lines += u0/(4*pi)*(ds_cross_R/absolute_R**3)
    bbb += lines.z*2*pi*R*i/m*R/m
print(aaa,bbb)



