
import matplotlib.pyplot as plt
import matplotlib.style
import random


class RandomWalk():
    def __init__(self, **kwargs):
        self.NumberOfSteps = kwargs.get("NumberOfSteps")
        self.West = 0.3
        self.East = 0.25
        self.North = 0.35
        self.South = 0.1
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
                if p <= self.West:
                    initial = (initial[0] - 1, initial[1])
                elif p > self.West and p <= self.West + self.East:
                    initial = (initial[0] + 1, initial[1])
                elif p > self.West + self.East and p <= self.West + self.East + self.North:
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



Animation = RandomWalk(NumberOfSteps = 10000).OneIeteration()
print(Animation)



