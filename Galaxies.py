# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:16:56 2024

@author: Ryan Xiong
"""
import numpy as np

# Generate a galaxy in the x-y plane
def generate_galaxy(N,Na,M,ptm,r_max,r_min,z_s,cx,cy,cz,cvx,cvy,cvz,sim):
    r = np.linspace(r_min,r_max,N)
    angle = np.linspace(0,2*np.pi*(Na-1)/Na,Na)
    x_pos = []
    y_pos = []
    z_pos = []
    for i in range(N):
        for j in range(Na):
            x_pos.append(r[i]*np.cos(angle[j]))
            y_pos.append(r[i]*np.sin(angle[j]))
            z_pos.append(z_s*np.random.randn())
    x_pos = np.array(x_pos)
    y_pos = np.array(y_pos)
    z_pos = np.array(z_pos)
    N_total = N*Na
    radius = np.sqrt(x_pos**2+y_pos**2)
    mu = M + (radius-r_min)/(r_max-r_min) * N_total * ptm
    vrot = np.sqrt(mu/radius)
    x_vel = -y_pos/radius * vrot + cvx
    y_vel = x_pos/radius * vrot + cvy
    z_vel = vrot*0 + cvz
    x_pos += cx
    y_pos += cy
    z_pos += cz
    sim.add(m = M, x = cx, y = cy, z = cz, vx = cvx, vy = cvy, vz = cvz)
    for i in range(N_total):
        #print(i)
        sim.add(m = ptm, x = x_pos[i],y = y_pos[i],z = z_pos[i],vx = x_vel[i],vy = y_vel[i],vz = z_vel[i])
# Generate a Galaxy with a 1/r sampling
def temp_generate_galaxy(N,M,ptm,r_max,r_min,z_s,cx,cy,cz,cvx,cvy,cvz,sim):
    r_temp = np.random.uniform(size=(N))
    r = (r_max-r_min)*r_temp + r_min
    theta = np.random.uniform(size=(N))*2*np.pi
    x_pos = r*np.cos(theta)
    y_pos = r*np.sin(theta)
    z_pos = z_s*np.random.randn(N)
    x_pos = np.array(x_pos)
    y_pos = np.array(y_pos)
    z_pos = np.array(z_pos)
    N_total = N
    radius = np.sqrt(x_pos**2+y_pos**2)
    mu = M + (radius-r_min)/(r_max-r_min) * N_total * ptm
    vrot = np.sqrt(mu/radius)
    x_vel = -y_pos/radius * vrot + cvx 
    y_vel = x_pos/radius * vrot + cvy 
    z_vel = vrot*0 + cvz 
    x_pos += cx
    y_pos += cy
    z_pos += cz
    sim.add(m = M, x = cx, y = cy, z = cz, vx = cvx, vy = cvy, vz = cvz)
    for i in range(N_total):
        #print(i)
        sim.add(m = ptm, x = x_pos[i],y = y_pos[i],z = z_pos[i],vx = x_vel[i],vy = y_vel[i],vz = z_vel[i])

#Generate a 1/r galaxy rotating in the other direction
def reverse_temp_generate_galaxy(N,M,ptm,r_max,r_min,z_s,cx,cy,cz,cvx,cvy,cvz,sim):
    r_temp = np.random.uniform(size=(N))
    r = (r_max-r_min)*r_temp + r_min
    theta = np.random.uniform(size=(N))*2*np.pi
    x_pos = r*np.cos(theta)
    y_pos = r*np.sin(theta)
    z_pos = z_s*np.random.randn(N)
    x_pos = np.array(x_pos)
    y_pos = np.array(y_pos)
    z_pos = np.array(z_pos)
    N_total = N
    radius = np.sqrt(x_pos**2+y_pos**2)
    mu = M + (radius-r_min)/(r_max-r_min) * N_total * ptm
    vrot = np.sqrt(mu/radius)
    x_vel = y_pos/radius * vrot + cvx 
    y_vel = -x_pos/radius * vrot + cvy 
    z_vel = vrot*0 + cvz 
    x_pos += cx
    y_pos += cy
    z_pos += cz
    sim.add(m = M, x = cx, y = cy, z = cz, vx = cvx, vy = cvy, vz = cvz)
    for i in range(N_total):
        #print(i)
        sim.add(m = ptm, x = x_pos[i],y = y_pos[i],z = z_pos[i],vx = x_vel[i],vy = y_vel[i],vz = z_vel[i])

# Generate a vertical Galaxy perpendicular to xy
def generate_vertical_galaxy(N,Na,M,ptm,r_max,r_min,z_s,cx,cy,cz,cvx,cvy,cvz,sim):
    r = np.linspace(r_min,r_max,N)
    angle = np.linspace(0,2*np.pi*(Na-1)/Na,Na)
    x_pos = []
    y_pos = []
    z_pos = []
    for i in range(N):
        for j in range(Na):
            x_pos.append(r[i]*np.cos(angle[j]))
            z_pos.append(r[i]*np.sin(angle[j]))
            y_pos.append(z_s*np.random.randn())
    x_pos = np.array(x_pos)
    y_pos = np.array(y_pos)
    z_pos = np.array(z_pos)
    N_total = N*Na
    radius = np.sqrt(x_pos**2+z_pos**2)
    mu = M + (radius**2-r_min**2)/(r_max**2-r_min**2) * N_total * ptm
    vrot = np.sqrt(mu/radius)
    x_vel = -z_pos/radius * vrot + cvx
    z_vel = x_pos/radius * vrot + cvz
    y_vel = vrot*0 + cvy
    x_pos += cx
    y_pos += cy
    z_pos += cz
    sim.add(m = M, x = cx, y = cy, z = cz, vx = cvx, vy = cvy, vz = cvz)
    for i in range(N_total):
        sim.add(m = ptm, x = x_pos[i],y = y_pos[i],z = z_pos[i],vx = x_vel[i],vy = y_vel[i],vz = z_vel[i])

# Generate a normal galaxy rotating the other direction
def generate_clockwise_galaxy(N,Na,M,ptm,r_max,r_min,z_s,cx,cy,cz,cvx,cvy,cvz,sim):
    r = np.linspace(r_min,r_max,N)
    angle = np.linspace(0,2*np.pi*(Na-1)/Na,Na)
    x_pos = []
    y_pos = []
    z_pos = []
    for i in range(N):
        for j in range(Na):
            x_pos.append(r[i]*np.cos(angle[j]))
            y_pos.append(r[i]*np.sin(angle[j]))
            z_pos.append(z_s*np.random.randn())
    x_pos = np.array(x_pos)
    y_pos = np.array(y_pos)
    z_pos = np.array(z_pos)
    N_total = N*Na
    radius = np.sqrt(x_pos**2+y_pos**2)
    mu = M + (radius**2-r_min**2)/(r_max**2-r_min**2) * N_total * ptm
    vrot = np.sqrt(mu/radius)
    x_vel = y_pos/radius * vrot + cvx
    y_vel = -x_pos/radius * vrot + cvy
    z_vel = vrot*0 + cvz
    x_pos += cx
    y_pos += cy
    z_pos += cz
    sim.add(m = M, x = cx, y = cy, z = cz, vx = cvx, vy = cvy, vz = cvz)
    for i in range(N_total):
        #print(i)
        sim.add(m = ptm, x = x_pos[i],y = y_pos[i],z = z_pos[i],vx = x_vel[i],vy = y_vel[i],vz = z_vel[i])
# Generate a Plummer Sphere
def Plummer_Sphere(N,M,a,cx,cy,cz,cxv,cyv,czv,sim):
    ptm = M/N
    theta_temp = np.random.uniform(size=(N))
    r_temp = np.random.uniform(size = (N))
    phi = 2*np.pi*np.random.uniform(size = (N))
    r = a*np.tan(np.arcsin(r_temp**(1/3)))
    theta = np.arccos(1-2*theta_temp)
    x_pos = r*np.sin(theta)*np.cos(phi) + cx
    y_pos = r*np.sin(theta)*np.sin(phi) + cy
    z_pos = r*np.cos(theta) + cz
    x_vel = []
    y_vel = []
    z_vel = []
    v_disp = np.sqrt(M/(6*np.sqrt(r**2+a**2)))
    for i in range(N):
        v = np.random.normal([0,0,0],[v_disp[i],v_disp[i],v_disp[i]])
        x_vel.append(v[0])
        y_vel.append(v[1])
        z_vel.append(v[2])
    x_vel = np.array(x_vel)*0 + cxv
    y_vel = np.array(y_vel)*0 + cyv
    z_vel = np.array(z_vel)*0 + czv
    Number = 0
    for i in range(N):
        try:
            sim.add(m = ptm, x = x_pos[i],y = y_pos[i],z = z_pos[i],vx = x_vel[i],vy = y_vel[i],vz = z_vel[i])
            Number +=1
        except RuntimeError:
            pass
    return Number