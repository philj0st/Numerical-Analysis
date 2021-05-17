# %%
import numpy as np
import matplotlib.pyplot as plt

# 1st derivative of f
def f_1(x,y):
    return x**2 + 0.1 * y

xmin = -2
xmax = 2
xstep = .2

ymin = -2
ymax = 2
ystep = .2


# generate a grid of points. (later arrow locations)
xs = np.arange(xmin,xmax + xstep,xstep, dtype=np.float64)
ys = np.arange(ymin,ymax + ystep,ystep, dtype=np.float64)
[xgrid, ygrid] = np.meshgrid(xs,ys)



# evaluate x and y direction components of the arrow vectors
# (if a curve goes through those points it has this slope)
dy = f_1(xgrid,ygrid)
dx = np.ones_like(dy)

# normalize arrows
r = np.power(np.add(np.power(dx,2), np.power(dy,2)),0.5)

quiveropts = dict(color='blue', units='xy', angles='xy', width=0.002)

plt.quiver(xgrid, ygrid, dx/r, dy/r, **quiveropts)


# %%
# numerically integrate ODEs with different methods

# Euler Method for f with initial value y0
# n steps in the interval [a,b].
def euler(f,a,b,n,y0):

    # init x_i's and y_i's
    x = np.linspace(a,b,n)
    y = np.zeros_like(x)
    
    for i in range(0,len(x)-1):
        # distance to the next point to approximate
        d = np.abs(x[i]-[x[i+1]])

        # slope at current point
        slope = f(x[i],y[i])

        # to get the next point follow the slope for distance d
        y[i+1] = y[i] + d * slope

    return y

# Midpoint method for f with initial value y0
# n steps in the interval [a,b].
def midpoint(f,a,b,n,y0):

    # init x_i's and y_i's
    x = np.linspace(a,b,n)
    y = np.zeros_like(x)
    
    for i in range(0,len(x)-1):
        # distance to the next point to approximate
        dnext = np.abs(x[i]-[x[i+1]])

        # use Euler Method to calculate y of midpoint
        ymid = y[i] + dnext/2 * f(x[i],y[i])
        xmid = x[i] + dnext/2

        # slope at midpoint between next and current point
        slope = f(xmid,ymid)

        # to get the next point follow the slope for distance d
        y[i+1] = y[i] + dnext * slope

    return y

# Modified Euler / Heun's method for f with initial value y0
# n steps in the interval [a,b].
def modeuler(f,a,b,n,y0):

    # init x_i's and y_i's
    x = np.linspace(a,b,n)
    y = np.zeros_like(x)
    
    for i in range(0,len(x)-1):
        # distance to the next point to approximate
        d = np.abs(x[i]-[x[i+1]])

        # slope at the current point
        slope_here = f(x[i],y[i])

        # use slope to find a temporary y
        ytemp = y[i] + d * slope_here

        # use ytemp to find slope on the other side of the discretization step
        slope_next = f(x[i+1],ytemp)
        slope_avg = (slope_here + slope_next)/2

        # to get the next point follow the average slope for distance d
        y[i+1] = y[i] + d * slope_avg

    return y

def f(x,y):
    return x**2 + 0.1 * y
    
ys_euler  = euler(f,xmin,xmax,15,2)
xs_euler = np.linspace(xmin,xmax,15)
plt.plot(xs_euler, ys_euler)

ys_midpoint = midpoint(f,xmin,xmax,15,2)
plt.plot(xs_euler, ys_midpoint)

ys_modeuler = modeuler(f,xmin,xmax,15,2)
plt.plot(xs_euler, ys_modeuler)

plt.show()