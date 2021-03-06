# Stochastic-Process-and-Random-Walk

A popular random walk model is that of a random walk on a regular lattice, where at each step the location jumps to another site according to some probability distribution. In a simple random walk, the location can only jump to neighboring sites of the lattice, forming a lattice path. 

Let's start with an simple example of a discrete-time random walk in which the length of each step is one unit. The walker is initially at the coordinates (0, 0) which is the center of the circle. The stochastic process stops once the walker escape from the circle with a radius of 10. 

At each position, the walker can move one unit towards four directions with uniformly distributed probability. Turn North, turn South, turn East and turn West. The probability of each direction is shown below: 

``` Python
# Probability of each direction
West = 0.3
East = 0.25
North = 0.35
South = 0.1
initial = (0, 0)

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
```

The animation tool ```matplotlib``` is used to better visualize the random walk process. ```FuncAnimation``` built in ```matplotlib.animation.Animation``` provides a clear step by step walking process. 

For one simulation, we get the coordinates of each position and saved in ```animate(s)``` function where ```s``` means the ```nth``` step of the simulation. 

``` Python
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
circ = plt.Circle((0, 0), radius=10, fill=False, color='brown', linewidth=2)  # Draw a circle centered in (0, 0) with a radius of 10. 
ax.add_patch(circ)


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(Points), interval=500, blit=True)

anim.save('RandomWalk.mp4',fps=1.0 ,dpi=200)
```
In ```animation.FuncAnimation``` function, it accepts an argument ```frame``` which control the number of frames desplayed. We've chosen the number of steps as the frame number with a 500ms delay between frames. The default delay is 200ms if not specified. After animation is generated, we can either display the plot or save it into a MP4 file.

For the display animation, the duration is going to be frames * interval / 1000 (in seconds). 
To display animation clock to click every second, set ```interval=1000```.

For the saved animation, the duration is going to be frames * (1 / fps) (in seconds). 
To save animation clock to tick every second, set ```fps=1```. (The number I use in the example).

![](https://github.com/jqsheng94/Stochastic-Process-and-Random-Walk/blob/master/RandomWalk.gif)

At each coordinate, the probability of the next move is independent of the previous one. 

For each time the walker escape from the circle, we count it as one event and record the number of steps it used to exit. Repeat the same process 100,000 times, and then get the average number of steps that walker need to stop the process.


Here is the hisgram plot of the number of steps for 100,000 iterations.

![](https://github.com/jqsheng94/Stochastic-Process-and-Random-Walk/blob/master/2d%20hist%20plot.png)

```
E(X) = 36.38841
```

After run the simulation ```100,000``` times, we get the stable results of ```36.38841``` which is also known as the expected value of the number of steps. 

We can apply the same theory to study three dimensional random walk. The walker starts at the coordinate (0, 0, 0) and at each step he will move to one of six directions based on different probabilities. 

``` Python
# Probability of each direction
West = 0.1
East = 0.2
North = 0.35
South = 0.05
Up = 0.15
Down = 0.15
initial = (0, 0, 0)
radius = 10
```

Here is the simulation animation for 3-dimensional random walk. 

![](https://github.com/jqsheng94/Stochastic-Process-and-Random-Walk/blob/master/3DRandomWalk2.gif)

We count each time that walker escapes from the sphere as one event and record the numbers of steps for each event. Repeat the same process 100,000 times and finally approaches to a constant number ```25.70093```.

Here is the hisgram plot of the number of steps for 100,000 iterations.

![](https://github.com/jqsheng94/Stochastic-Process-and-Random-Walk/blob/master/3d%20hist%20plot.png)

```
E(X) = 25.70093
```
After run the simulation ```100,000``` times, we get the expectation of  ```25.70093``` as the average number of steps to get out of the sphere. 


