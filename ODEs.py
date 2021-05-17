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
plt.show()

# %%
# numerically solve some ODEs with different methods

# Euler Method for f with initial value y0
# n steps in the interval [a,b].
# def euler(f,a,b,n,y0):

#     # init x_i's and y_i's
#     xis = np.linspace(a,b,n)
#     yis = np.zeros_like(xis)

#     for xi in np.nditer(xis):
#         print(xi)


# def f(x,y):
#     return x**2 + 0.1 * y
    
# euler(f)