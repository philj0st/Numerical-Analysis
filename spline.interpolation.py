import numpy as np
from scipy.interpolate import CubicSpline

def cubicSpline(x,y,x_int):
    """! Harmonic cubic spline interpolation. Determines coefficients a,b,c,d and 
    interpolates x_int in appropriate intervals.
    @param x  Vector of datapoints x.
    @param y  Vector of datapoints y.
    @param x_int x value of the point to be interpolated.
    @return y_int interpolated y values
    """

    #region "learn" the coefficients of the cubic polynomials that interpolate intervals in x.
    # amount of intervals/splines
    n = len(x)-1

    # a_i = y_i
    a = y[:-1]

    # h_i = x_{i+1} - x_i for i in 0..n-1
    h = x[1:]-x[:-1]

    # 2 * h_i + h_{i+1}
    diagA = 2*(h[1:]+h[:-1])
    
    # h_1..h_n-2
    hInA = h[1:-1]

    A = np.eye(n-1)*diagA
    # distribute h_1..h_n-2 above and underneath the diagonal
    A += np.diag(hInA,1)
    A += np.diag(hInA,-1)

    # construct RHS
    z = 3/h[1:] * (y[2:] - y[1:-1]) - 3/h[:-1] * (y[1:-1] - y[:-2])

    # c_0 = c_{n} = 0
    c = np.zeros(n+1)

    c[1:-1] = np.linalg.solve(A,z)
    
    b = (y[1:]-y[:-1])/h - h/3*(c[1:] + 2*c[:-1])

    d = 1/(3*h)*(c[1:]-c[:-1])
    #endregion

    #region interpolate all points in x_int
    y_int = x_int.copy()
    # for all intervals
    for i in range(len(x)-1):
        # find points to interpolate within given interval
        idx = np.where(np.logical_and(x[i]<= x_int,x_int < x[i+1]))[0]
        xx = x_int[idx]
        yy = np.polyval(np.array([d[i],c[i],b[i],a[i]]), xx-x[i])
        y_int[idx] = yy
        print(f'interpolating in interval [{x[i]},{x[i+1]}[')
        print(xx)
        print(yy)
        print('\n')

    # edgecase where x_int contains exactly last interval border
    #find indicies if x_int contains dupes
    idx = np.where(x_int == x[len(x)-1])[0] 
    # interpolate with last interval polynomial
    i = len(a)-1
    y_int[idx] = np.polyval(np.array([d[i],c[i],b[i],a[i]]), x_int[idx]-x[i])
    #endregion
    return y_int




xi = np.array([4,6,8,10],dtype=np.float64)
yi = np.array([6,3,9,0],dtype=np.float64)

x_int = np.array([4.1,5,5.5,5.6,7,8,10,10])
y_int = cubicSpline(xi,yi,x_int)
print(x_int)
print(y_int)


# reference implementation
cs = CubicSpline(xi,yi,bc_type='natural')
print(cs(x_int))

