import matplotlib.pyplot as plt
import numpy as np

#region data
# gravitational acceleration
G = 9.81

# throwing distance given initial speed v0 and angle a
def f(v0,a):
    return v0**2 * np.sin(2*a) / G

# determine throwing distances for combinations of v0 and a
[x,y] = np.meshgrid(np.linspace(0,100), np.linspace(0,np.pi/2))
z = f(x,y)

#endregion

#region plot
fig = plt.figure()
colorbar = plt.contour(x, y, z)
fig.colorbar(colorbar)

# in a sense fix z axis to constants and show lines for different constants i.e intersects with the xy-plane and the graph

plt.title('throwing distance as contour lines')
ax = fig.add_subplot(111)
ax.set_xlabel(r'initial speed $v_0 [\frac{m}{s^2}]$')
ax.set_ylabel(r'angle $\alpha$')
plt.show()
#endregion