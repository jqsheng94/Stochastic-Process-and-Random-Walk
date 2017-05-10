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
