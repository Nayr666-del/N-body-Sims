# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:18:37 2024

@author: Ryan Xiong
"""

from Galaxies import generate_galaxy, generate_clockwise_galaxy, temp_generate_galaxy, reverse_temp_generate_galaxy
import rebound
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial Configuration. Units are set as G = 1
sim = rebound.Simulation()
sim.gravity = 'tree'
sim.integrator = 'leapfrog'
sim.configure_box(800.)   # confine the simulation to a box of size 10
sim.boundary = 'open'
sim.dt = 0.001
sim.softening = 0.01
#sim.status()

# Parameters 1 - Modify
Nr1 = 80
Na1 = 80
N1 = Nr1 * Na1 +1 
M1 = 8000
ptm1 = 1
r_max1 = 80
r_min1 = 10
z_s1 = 3
cx1 = 0
cy1 = 0
cz1 = 0
cvx1 = 0
cvy1 = 0
cvz1 = 0

# Parameters 2 - Modify
Nr2 = 30
Na2 = 50
N2 = Nr2 * Na2 +1 
M2 = 800
ptm2 = 2
r_max2 = 16
r_min2 = 1
z_s2 = 0.3
cx2 = 120
cy2 = 120
cz2 = 0
cvx2 = -10
cvy2 = 0
cvz2 = 0

# Generate Galaxy
temp_generate_galaxy(3000,M1,ptm1,r_max1,r_min1,z_s1,cx1,cy1,cz1,cvx1,cvy1,cvz1,sim)
temp_generate_galaxy(600,M2,ptm2,r_max2,r_min2,z_s2,cx2,cy2,cz2,cvx2,cvy2,cvz2,sim)

N = 3602 # Total Number of particles

# saving the integration series for later plots (e.g. 3D)
t_series = np.arange(0,30,0.005)
x_pos = []
y_pos = []
z_pos = []
x_record = []
y_record = []
z_record = []
for i in range(N):
    try:
        x_p = sim.particles[i].x
        y_p = sim.particles[i].y
        z_p = sim.particles[i].z
    except AttributeError:
        continue
    x_pos.append(x_p)
    y_pos.append(y_p)
    z_pos.append(z_p)
x_record.append(x_pos)
y_record.append(y_pos)
z_record.append(z_pos)
for t in tqdm(t_series):
    sim.integrate(t)
    x_pos = []
    y_pos = []
    z_pos = []
    for i in range(N):
        try:
            x_p = sim.particles[i].x
            y_p = sim.particles[i].y
            z_p = sim.particles[i].z
        except AttributeError:
            continue
        x_pos.append(x_p)
        y_pos.append(y_p)
        z_pos.append(z_p)
    x_record.append(x_pos)
    y_record.append(y_pos)
    z_record.append(z_pos)


# Generate Animation

fig = plt.figure(figsize = (6,6))
ax = plt.axes()

scat = ax.scatter(x_record[0], y_record[0], c="b",alpha = 0.2, s=3)
ax.set(xlim=[-200, 200], ylim=[-200, 200])
char = ax.annotate('t='+str(0),(150,150))
ax.grid()

def update(frame):
    # for each frame, update the data stored on each artist.
    x = x_record[frame*10]
    y = y_record[frame*10]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    char.set_text('t='+str(round(frame*0.05,2)))
    return (scat)


ani = animation.FuncAnimation(fig=fig, func=update, frames=600, interval=20)
plt.show()
ani.save(filename="ExampleAnimation.gif", writer="pillow")