# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:32:21 2017

@author: jiaqi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May  10 14:02:17 2017

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
        self.West = 0.3
        self.East = 0.25
        self.North = 0.35
        self.South = 0.1
        self.radius = 10
        self.initial = (0,0)
        self.numberOfSteps = 10000
        self.Points = self.OneInteration()


    def OneInteration(self):
        Points = []
        initial = self.initial
        for i in range(self.numberOfSteps):
            if i == 0:
                x = [initial[0]]
                y = [initial[1]]
                Points.append((x, y))
            else:
                p = random.uniform(0, 1)
                if p <= self.West:
                    initial = (initial[0] - 1, initial[1])
                elif p > self.West and p <= self.West + self.East:
                    initial = (initial[0] + 1, initial[1])
                elif p > self.West + self.East and p <= self.West + self.East + self.North:
                    initial = (initial[0], initial[1] + 1)
                else:
                    initial = (initial[0], initial[1] - 1)
                x = [initial[0]]
                y = [initial[1]]
                Points.append((x, y))
                if (initial[0]) ** 2 + (initial[1]) ** 2 > self.radius ** 2:
                    break
        return Points

    def init(self):
        self.line.set_data([], [])
        return self.line,

    def animate(self,i):
        A = self.Points[i]
        xs = np.array(A[0])
        ys = np.array(A[1])
        self.line.set_data(xs, ys)
        self.title.set_text('Random Walk: Step='+ format(i) + ',Coordinates: ' + format(A))
        return self.line, self.title


    def fig(self):
        matplotlib.style.use('ggplot')
        fig = plt.figure()
        ax = plt.axes(xlim=(-12, 12), ylim=(-12, 12))
        circ = plt.Circle((0, 0), radius=10, fill=False, color='brown', linewidth=2)
        ax.add_patch(circ)
        self.line, = ax.plot([], [], lw=2, marker='o')
        self.title = ax.set_title('3D Random Walk')
        ani = animation.FuncAnimation(fig, self.animate, init_func=self.init, frames=len(self.Points), interval=500, blit=True)
        ani.save('RandomWalk2.mp4', fps=1.0, dpi=200)
        plt.show()

Animation = ScatterAnimation().fig()


