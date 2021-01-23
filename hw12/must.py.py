#這次有錄影片!!!
###https://youtu.be/4aweOb8k31o
from vpython import*

f_d = 120  
w = 2*pi*f_d
R = 30 
C = 20*10**(-6) 
L = 0.2 
T = 1/f_d
t = 0
dt = 1/(f_d*5000) 
Q = 0 
i = 0
imax = 0
vmax = 0
vt, it, imin, iamp = 0, 0, 0, 0
Z = complex(R, (w*L-1/(w*C)))
I = 36/Z
flag = False
time = 0
E_decay = 0
r = 36/((Z.real**2 + Z.imag**2)**0.5)
phi = 180/pi*atan(Z.imag/Z.real)

scene1 = graph(align='left', xtitle='t', ytitle='i(A):blue, v(100V):red', background=vector(0.2, 0.6, 0.2))
scene2 = graph(align='left', xtitle='t', ytitle='Energy(J)', background=vector(0.2, 0.6, 0.2))

i_t = gcurve(color=color.blue, graph=scene1)
v_t = gcurve(color=color.red, graph=scene1)
E_t = gcurve(color=color.red, graph=scene2)



while t <= 20*T:
    rate(5000)
    t += dt
    if 0 <= t <= 12*T: v = 36*sin(w*t)
    else: v = 0
    v_c = Q/C
    v_r = i*R
    di = (v - v_c - v_r)*dt/L
    i += di
    Q += i*dt
    E_t.plot(pos=(t/T, (1/2)*(C*v_c**2+L*i**2)))
    v_t.plot(pos=(t/T, v/100))
    i_t.plot(pos=(t/T, i))
    if 9*T <= t and t <= 10*T:
        if i > imax:
            imax = i
            it = t
        if i < imin:
            imin = i
        if v > vmax:
            vmax = v
            vt = t
        iamp = (imax - imin)/2
    if t >= 12*T:
        time += dt
        if E_decay == 0:
            E_decay = (1/2)*(C*v_c**2+L*i**2)
        if flag == False and (1/2)*(C*v_c**2+L*i**2) <= 0.1*E_decay:
            print('phi = %s'%(phi))
            print('decay_time = %s'%(time))
            print('real_amp = %s'%(iamp))
            print('real_phi = %s'%((it-vt)/T*360))
            print('theoretical_amp = %s'%(r))
            flag = True
