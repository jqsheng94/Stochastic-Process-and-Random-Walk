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


class RandomWalk():
    def __init__(self, **kwargs):
        self.NumberOfSteps = kwargs.get("NumberOfSteps")
        self.West = 0.1
        self.East = 0.2
        self.North = 0.35
        self.South = 0.05
        self.Up = 0.15
        self.down = 0.15
        self.radius = 10

    def OneIeteration(self):
        matplotlib.style.use('ggplot')
        fig = plt.figure(figsize=(15,15))
        ax1 = fig.add_subplot(111, projection='3d')
        u, v = np.mgrid[0:2*np.pi:200j, 0:np.pi:200j]
        x=np.cos(u)*np.sin(v)*10
        y=np.sin(u)*np.sin(v)*10
        z=np.cos(v)*10
        ax1.plot_wireframe(x, y, z, rstride = 10, cstride = 15, linewidth = 0.5, color = 'brown')
        ax1.set_xlim(-12, 12)
        ax1.set_ylim(-12, 12)
        ax1.set_zlim(-12, 12)
        plt.show()
        Points = []
        initial = (0, 0, 0)
        for i in range(self.NumberOfSteps):
            if i == 0:
                new_x = [initial[0]]
                new_y = [initial[1]]
                new_z = [initial[2]]
                points, = ax1.plot(new_x, new_y, new_z, marker='o')
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
                new_x = [initial[0]]
                new_y = [initial[1]]
                new_z = [initial[2]]
                points.set_data(new_x, new_y)            
                if (initial[0]) ** 2 + (initial[1]) ** 2 +(initial[2])**2 > self.radius ** 2:
                    break
                Points.append(initial)
                plt.pause(0.5)
        return len(Points)



ExpectedNumberOfSteps = RandomWalk(NumberOfSteps = 10000).OneIeteration()
print(ExpectedNumberOfSteps)