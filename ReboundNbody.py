import rebound # Import the Rebound module
from IPython.display import clear_output
from tqdm import tqdm # Visulization of integration process
import matplotlib.pyplot as plt
import numpy as np

# Initial Configuration
sim = rebound.Simulation()
sim.gravity = 'tree' # Tree code
sim.integrator = 'leapfrog' # Leap frog integration
sim.configure_box(150.)   
sim.boundary = 'open'
sim.dt = 0.001
sim.softening = 0.01
# sim.status()

# Generate a galaxy in the x-y plane
def generate_galaxy(N,Na,M,ptm,r_max,r_min,z_s,cx,cy,cz,cvx,cvy,cvz):
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
# Generate a vertical Galaxy
def generate_vertical_galaxy(N,Na,M,ptm,r_max,r_min,z_s,cx,cy,cz,cvx,cvy,cvz):
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
        #print(i)
        sim.add(m = ptm, x = x_pos[i],y = y_pos[i],z = z_pos[i],vx = x_vel[i],vy = y_vel[i],vz = z_vel[i])


# Parameters 1
Nr1 = 30
Na1 = 50
N1 = Nr1 * Na1 +1 
M1 = 8000
ptm1 = 1
r_max1 = 20
r_min1 = 3
z_s1 = 0.3
cx1 = 20
cy1 = 20
cz1 = 0
cvx1 = -10
cvy1 = 0
cvz1 = 0
# Parameters 2
Nr2 = 30
Na2 = 50
N2 = Nr2 * Na2 +1 
M2 = 8000
ptm2 = 1
r_max2 = 20
r_min2 = 3
z_s2 = 0.3
cx2 = -20
cy2 = -20
cz2 = 0
cvx2 = 10
cvy2 = 0
cvz2 = 0
# Generate Galaxy
generate_galaxy(Nr1,Na1,M1,ptm1,r_max1,r_min1,z_s1,cx1,cy1,cz1,cvx1,cvy1,cvz1)
generate_vertical_galaxy(Nr2,Na2,M2,ptm2,r_max2,r_min2,z_s2,cx2,cy2,cz2,cvx2,cvy2,cvz2)
N = N1 + N2

# Stores position for future plot/animation analysis
# saving the integration series for later plots (e.g. 3D)

t_series = np.arange(0,10,0.005)
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
        pass
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
            pass
        x_pos.append(x_p)
        y_pos.append(y_p)
        z_pos.append(z_p)
    x_record.append(x_pos)
    y_record.append(y_pos)
    z_record.append(z_pos)    