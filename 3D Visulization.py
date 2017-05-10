# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:32:21 2017

@author: jiaqi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:57:06 2017

@author: jiaqi
"""
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.style
import random
import numpy as np
from matplotlib import animation


West = 0.1
East = 0.2
North = 0.35
South = 0.05
Up = 0.15
down = 0.15
radius = 10

Points = []
initial = (0, 0, 0)

for i in range(10000):
    if i == 0:
        x = [initial[0]]
        y = [initial[1]]
        z = [initial[2]]
        Points.append((x, y, z))
    else:
        p = random.uniform(0, 1)
        if p <= West:
            initial = (initial[0] - 1, initial[1], initial[2])
        elif p > West and p <= West + East:
            initial = (initial[0] + 1, initial[1], initial[2])
        elif p > West + East and p <= West + East + North:
            initial = (initial[0], initial[1] + 1, initial[2])
        elif p > West + East + North and p < West + East + North + Up:
            initial = (initial[0], initial[1], initial[2] + 1)
        else:
            initial = (initial[0], initial[1], initial[2] - 1)
        x = [initial[0]]
        y = [initial[1]]
        z = [initial[2]]    
        Points.append((x, y, z))       
        if (initial[0]) ** 2 + (initial[1]) ** 2 +(initial[2])**2 > radius ** 2:
            break

def animate(i):
    A = Points[i]
    xs = np.array(A[0])
    ys = np.array(A[1])
    zs = np.array(A[2])
    graph.set_data(xs, ys)
    graph.set_3d_properties(zs)
    return graph,


matplotlib.style.use('ggplot')
fig = plt.figure(figsize=(5,5))
ax1 = fig.add_subplot(111, projection='3d')
u, v = np.mgrid[0:2 * np.pi:200j, 0:np.pi:200j]
x = np.cos(u) * np.sin(v) * 10
y = np.sin(u) * np.sin(v) * 10
z = np.cos(v) * 10
ax1.plot_wireframe(x, y, z, rstride=10, cstride=15, linewidth=0.5, color='brown')
ax1.set_xlim(-15, 15)
ax1.set_ylim(-15, 15)
ax1.set_zlim(-15, 15)


graph, = ax1.plot([0], [0], [0], linestyle="", marker="o")
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=len(Points), interval=500, blit=True)
nim.save('3DRandomWalk.mp4',fps=1.0 ,dpi=200)
plt.show()