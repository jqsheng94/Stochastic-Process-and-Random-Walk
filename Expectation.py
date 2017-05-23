from statistics import mean
import random
import matplotlib.pyplot as plt
import matplotlib.style

class RandomWalk():
    def __init__(self, **kwargs):
        self.NumberOfSteps = kwargs.get("NumberOfSteps")
        self.NumberOfInteration = kwargs.get("NumberOfInteration")
        self.West = 0.3
        self.East = 0.25
        self.North = 0.35
        self.South = 0.1
        self.radius = 10

    def OneIeteration(self):
        Points = []
        initial = (0, 0)
        for i in range(self.NumberOfSteps):
            if i == 0:
                Points.append(initial)
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
                if (initial[0]) ** 2 + (initial[1]) ** 2 > self.radius ** 2:
                    break
                Points.append(initial)
        return len(Points)

    def MultipleInteration(self):
        Steps = []
        for i in range(self.NumberOfInteration):
            Result = self.OneIeteration()
            Steps.append(Result)
        matplotlib.style.use('ggplot')
        n, bins, patches = plt.hist(Steps)
        plt.title("2D - Distribution plot of Number of steps")
        plt.xlabel("Number of Steps")
        plt.ylabel("Number of Iterations")
        plt.axvline(mean(Steps), linewidth=2, color = 'b')
        plt.show()
        return mean(Steps)


ExpectedNumberOfSteps = RandomWalk(NumberOfSteps = 10000, NumberOfInteration = 100000).MultipleInteration()
print(ExpectedNumberOfSteps)