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

#region plots
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x,y,z,rstride=5, cstride=5)

plt.title('throwing distance as wireframe')
ax.set_xlabel(r'initial speed $v_0 [\frac{m}{s^2}]$')
ax.set_ylabel(r'angle $\alpha$')
ax.set_zlabel('throwing distance [m]')

plt.show()
#endregion