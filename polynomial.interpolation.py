import numpy as np
import matplotlib.pyplot as plt
 
     
xs = np.array([1981,1984,1989,1993,1997,2000,2001,2003,2004,2010],dtype=np.float64)
ys = np.array([0.5,8.2,15,22.9,36.6,51,56.3,61.8,65,76.7],dtype=np.float64)

# simply exactly fit a poly nomial of degree |datapoints|-1 
# (generally not a good idea, just for showcase)
deg = len(xs)-1

# fit poly
coeffs = np.polyfit(xs,ys,deg)

# ATTENTION! we recognize a python warning _Polyfit may be poorly conditioned_
# python automatically resorts to a lower degree polynomial

# extrapolate for bigger range
x = np.arange(1975,2020,step=0.1)
y = np.polyval(coeffs,x)


# fit poly now with normalized data points
coeffs = np.polyfit(xs-xs.mean(),ys,deg)
y_ = np.polyval(coeffs,x-xs.mean())

# PLOTTING
 
fig,ax = plt.subplots()
ax.set_xlabel('year')
ax.set_ylabel('households with personal computers[%]')
 
ax.set_ylim (-100, 250)
ax.grid()
 
# plot given points
ax.scatter(xs,ys,marker='.',color='red',label='data points')
 
# plot using non-adjusted polynom
ax.plot(x, y, label='polynomial fit')
 
# plot using adjusted polynom
ax.plot(x, y_, color='green', label='poly fit to normalized data' )
plt.legend()
plt.show()


print("2020 estimate:", np.polyval(coeffs,2020-xs.mean()))