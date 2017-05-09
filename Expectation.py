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
        Points = []
        initial = (0, 0)
        for i in range(self.NumberOfSteps):
            if i == 0:
                Points.append(initial)
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
                if (initial[0]) ** 2 + (initial[1]) ** 2 > self.radius ** 2:
                    break
                Points.append(initial)
        return len(Points)

    def MultipleInteration(self):
        Steps = []
        for i in range(self.NumberOfInteration):
            Result = self.OneIeteration()
            Steps.append(Result)
        return mean(Steps)


ExpectedNumberOfSteps = RandomWalk(NumberOfSteps = 10000, NumberOfInteration = 100000).MultipleInteration()
print(ExpectedNumberOfSteps)