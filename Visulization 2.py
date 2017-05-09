
import matplotlib.pyplot as plt
import matplotlib.style
from matplotlib import animation
from statistics import mean
import random


class RandomWalk():
    def __init__(self, **kwargs):
        self.NumberOfSteps = kwargs.get("NumberOfSteps")
        self.NumberOfInteration = kwargs.get("NumberOfInteration")
        self.Left = 0.3
        self.Right = 0.25
        self.Up = 0.35
        self.Down = 0.1
        self.radius = 10

    def OneIeteration(self):
        matplotlib.style.use('ggplot')
        fig, ax = plt.subplots()
        ax.set_xlim(-12, 12)
        ax.set_ylim(-12, 12)
        circ = plt.Circle((0, 0), radius=10, fill=False, color='brown', linewidth=2)
        ax.add_patch(circ)
        Points = []
        initial = (0, 0)
        for i in range(self.NumberOfSteps):
            if i == 0:
                new_x = [initial[0]]
                new_y = [initial[1]]
                points, = ax.plot(new_x, new_y, marker='o')
            else:
                p = random.uniform(0, 1)
                if p <= self.Left:
                    initial = (initial[0] - 1, initial[1])
                elif p > self.Left and p <= self.Left + self.Right:
                    initial = (initial[0] + 1, initial[1])
                elif p > self.Left + self.Right and p <= self.Left + self.Right + self.Up:
                    initial = (initial[0], initial[1] + 1)
                else:
                    initial = (initial[0], initial[1] - 1)
                new_x = [initial[0]]
                new_y = [initial[1]]
                points.set_data(new_x, new_y)
                if (initial[0]) ** 2 + (initial[1]) ** 2 > self.radius ** 2:
                    break
            Points.append((new_x, new_y))
            plt.pause(0.5)
        return len(Points)



Animation = RandomWalk(NumberOfSteps = 10000, NumberOfInteration = 10000).OneIeteration()
print(Animation)



