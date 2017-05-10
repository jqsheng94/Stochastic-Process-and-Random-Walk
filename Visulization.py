import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
import matplotlib.style
import random
from matplotlib import animation


West = 0.3
East = 0.25
North = 0.35
South = 0.1
radius = 10
initial = (0, 0)


Points = []

for i in range(10000):
    if i == 0:
        x = [initial[0]]
        y = [initial[1]]
        Points.append((x, y))
    else:
        p = random.uniform(0, 1)
        if p <= West:
            initial = (initial[0] - 1, initial[1])
        elif p > West and p <= West + East:
            initial = (initial[0] + 1, initial[1])
        elif p > West + East and p <= West + East + North:
            initial = (initial[0], initial[1] + 1)
        else:
            initial = (initial[0], initial[1] - 1)
        x = [initial[0]]
        y = [initial[1]]
        Points.append((x, y))
        if (initial[0]) ** 2 + (initial[1]) ** 2 > radius ** 2:
            break
    

def init():
    line.set_data([], [])
    return line,

def animate(s):
    A = Points[s]
    xs = np.array(A[0])
    ys = np.array(A[1])
    line.set_data(xs, ys)
    return line,


matplotlib.style.use('ggplot')
fig = plt.figure()
ax = plt.axes(xlim=(-12, 12), ylim=(-12, 12))
line, = ax.plot([], [], lw=2, marker='o')
circ = plt.Circle((0, 0), radius=10, fill=False, color='brown', linewidth=2)
ax.add_patch(circ)


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(Points), interval=500, blit=True)

anim.save('RandomWalk.mp4',fps=1.0 ,dpi=200)

plt.show()


