import spline as myspline
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],dtype=np.float64)
y = np.array([75.995,91.972,105.711,123.203,131.669,150.697,179.323,203.212,226.505,249.633,281.422,308.745],dtype=np.float64)

x_int = np.arange(1900,2010+1,1,np.float64)

my_y_int = myspline.cubicSpline(x,y,x_int)
ref_y_int = CubicSpline(x,y,bc_type='natural')(x_int)

p = np.polyfit(x-1900,y,11)
poly_y_fit = np.polyval(p,x_int-1900)

#region plots
 
fig,ax = plt.subplots()
ax.set_xlabel('Year')
ax.set_ylabel(f'USA Population [in Millions]')

ax.grid()
 
# plot given points
ax.scatter(x,y,marker='o',color='red',label='data points')
 
ax.plot(x_int, my_y_int, marker='.', color='orange', label='my spline')
 
ax.plot(x_int, ref_y_int, marker=',', color='green', label='scypy spline' )

ax.plot(x_int, poly_y_fit, color='blue', label='polyfit deg 11' )
ax.legend()
plt.show()

#endregion