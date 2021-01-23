###https://youtu.be/yoiG6-1uHx4
###這次有錄影片
from vpython import *
import numpy as np
from random import *
prob = 0.008
N, L = 400, 10e-9/2.0
E = 1500000
q, m, size = 1.6e-19, 1e-6/6e23, 0.1e-9
t, dt, vrms = 0, 1E-16, 100000.0
atoms, atoms_v = [], []

# Initialization
scene = canvas(width=600, height=600, align='left', background=vector(0.2,0.2,0))
scenev = canvas(width=600, height=600, align='left', fov=0.01, background=vector(0.2,0.2,0))
g = graph(align = 'right',width = 500)
p = gcurve(color = color.blue, graph = g) 

container = box(canvas=scene, length=2*L, height=2*L, width=2*L, opacity=0.2, color=color.yellow )

pos_array = -L + 2*L*np.random.rand(N,3)
theta = pi*np.random.rand(N,1).flatten()
phi = 2*pi*np.random.rand(N,1).flatten()
v_array = np.transpose(vrms*np.array([np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)]))

def a_to_v(a):
    return vector(a[0], a[1], a[2])

for i in range(N):
    if i== N-1:
        atom = sphere(canvas=scene, pos=a_to_v(pos_array[i]), radius=2*size, color=color.yellow)
    else:
        atom = sphere(canvas=scene, pos=a_to_v(pos_array[i]), radius=size, color=a_to_v(np.random.rand(3,1)))
    atoms.append(atom)
    atoms_v.append(sphere(canvas=scenev, pos=a_to_v(v_array[i]), radius=vrms/70, color=a_to_v(np.random.rand(3,1))))

atoms_v[N-1].radius = vrms/30
atoms_v[N-1].color = color.yellow

vd_ball = sphere(canvas=scenev, pos=vec(0,0,0), radius=vrms/30, color=color.red)
x_axis = curve(canvas=scenev, pos=[vector(-1.4*vrms,0,0), vector(1.4*vrms,0,0)], radius=vrms/200)
y_axis = curve(canvas=scenev, pos=[vector(0,-1.4*vrms,0), vector(0,1.4*vrms,0)], radius=vrms/200)

vv = vector(0, 0, 0)
total_c = 0
while True:
    t += dt
    rate(10000)
    a = q*E/m
    v_array += a*dt*np.array([1,0,0])
    pos_array += v_array*dt
    outside = abs(pos_array) >= L
    pos_array[outside] = -pos_array[outside]
    vv += a_to_v(np.sum(v_array, axis=0) / N)
    
    # Handle collision here
    for i in range(N):
        ttt = np.random.random()
        if ttt <= prob:
            phi_collision =2*np.random.random()*pi
            theta_collision = np.random.random()*pi
            v_array[i] = vrms*np.array([np.sin(theta_collision)*np.cos(phi_collision),np.sin(theta_collision)*np.sin(phi_collision),np.cos(theta_collision)])
            total_c += 1

    vd = mag(vv)/(t/dt)

    if int(t/dt)%2000 == 0:
        tau = t*N/total_c    #find tau
        print(tau, vv/(t/dt), q*E*tau/m)
        print(vd/(q*E*tau/m))
        p.plot(pos = (t,vd/(q*E*tau/m)))

    vd_ball.pos = vv/(t/dt)

    for i in range(N):
        atoms_v[i].pos, atoms[i].pos = a_to_v(v_array[i]), a_to_v(pos_array[i])