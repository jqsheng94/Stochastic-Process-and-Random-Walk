# Stochastic-Process-and-Random-Walk


Let's start with an simple exmple of a discrete-time ramdom walk in which the length of each step is 1. The walker is initially at an coordinates (0, 0) which is the center of the circle. The stochastic process stops once the walker escape from the circle with redius of 10. 

At each position, the walker can move toward four directions with uniformly distributed probability. Turn North, turn South, turn East and turn West. The probability of each direction is shown below: 

```
Prob (West) = 0.3
Prob (East) = 0.25
Prob (North) =  0.35
Prob (South) = 0.1
```



![](https://github.com/jqsheng94/Stochastic-Process-and-Random-Walk/blob/master/RandomWalk.gif)

At each coordinate, the probability of the next move is independent of the previous one. 

For each time the walker escape from the circle, we count it as one even and record the number of steps it use to exit. Repeat the same process 10000 times, and then get the average of steps that walker need to stop the process.

```
E(X) = 36.38841
```

After execute the simulation 10000 times, we get the stable results of 36.38841 which is also known as the expected value of the number of steps. 




