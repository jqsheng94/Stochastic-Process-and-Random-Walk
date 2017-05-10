# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:32:21 2017

@author: jiaqi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May  10 13:07:26 2017

@author: jiaqi
"""
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.style
import random
import numpy as np
from matplotlib import animation



class ScatterAnimation(object):
    def __init__(self):
        self.West = 0.1
        self.East = 0.2
        self.North = 0.35
        self.South = 0.05
        self.Up = 0.15
        self.down = 0.15
        self.radius = 10
        self.initial = (0,0,0)
        self.numberOfSteps = 10000
        self.Points = self.OneInteration()


    def OneInteration(self):
        Points = []
        initial = self.initial
        for i in range(self.numberOfSteps):
            if i == 0:
                x = [initial[0]]
                y = [initial[1]]
                z = [initial[2]]
                Points.append((x, y, z))
            else:
                p = random.uniform(0, 1)
                if p <= self.West:
                    initial = (initial[0] - 1, initial[1], initial[2])
                elif p > self.West and p <= self.West + self.East:
                    initial = (initial[0] + 1, initial[1], initial[2])
                elif p > self.West + self.East and p <= self.West + self.East + self.North:
                    initial = (initial[0], initial[1] + 1, initial[2])
                elif p > self.West + self.East + self.North and p < self.West + self.East + self.North + self.Up:
                    initial = (initial[0], initial[1], initial[2] + 1)
                else:
                    initial = (initial[0], initial[1], initial[2] - 1)
                x = [initial[0]]
                y = [initial[1]]
                z = [initial[2]]
                Points.append((x, y, z))
                if (initial[0]) ** 2 + (initial[1]) ** 2 + (initial[2]) ** 2 > self.radius ** 2:
                    break
        return Points

    def animate(self,i):
        A = self.Points[i]
        xs = np.array(A[0])
        ys = np.array(A[1])
        zs = np.array(A[2])
        self.graph.set_data(xs, ys)
        self.graph.set_3d_properties(zs)
        self.title.set_text('3D Random Walk: Step='+ format(i) + ',Coordinates: ' + format(A))
        return self.graph, self.title


    def fig(self):
        matplotlib.style.use('ggplot')
        fig = plt.figure(figsize=(15, 15))
        ax1 = fig.add_subplot(111, projection='3d')
        u, v = np.mgrid[0:2 * np.pi:200j, 0:np.pi:200j]
        x = np.cos(u) * np.sin(v) * self.radius
        y = np.sin(u) * np.sin(v) * self.radius
        z = np.cos(v) * self.radius
        ax1.plot_wireframe(x, y, z, rstride=10, cstride=15, linewidth=0.5, color='brown')
        ax1.set_xlim(-15, 15)
        ax1.set_ylim(-15, 15)
        ax1.set_zlim(-15, 15)
        self.graph, = ax1.plot([self.initial[0]], [self.initial[1]], [self.initial[2]], linestyle="", marker="o")
        self.title = ax1.set_title('3D Random Walk')
        ani = animation.FuncAnimation(fig, self.animate, frames=len(self.Points), interval=500, blit=True)
        ani.save('3DRandomWalk2.mp4', fps=1.0, dpi=200)
        plt.show()

Animation = ScatterAnimation().fig()


