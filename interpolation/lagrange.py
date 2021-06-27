import numpy as np
 
# data points
xs = np.array([0,2500,5000,10000],dtype=np.float64)
ys = np.array([1013,747,540,226],dtype=np.float64)


# returns lagrange coefficients i for interpolating only a single point x, given data points xs and ys.
def lagrangeCoeffs(x,xs,ys): 
    # saves data points and (x,_?) in closure. returns i-th lagrange coefficioent for the interpolant.
    def i_th(i):
        # i != j  drops xs[i] data point
        xs_ = np.delete(xs,i)
        return np.multiply.reduce((x-xs_)/(xs[i]-xs_))
    return i_th

# interpolates a 
def lagrangePolynomial(xs,ys,x):
    P_x = 0
    
    lagrangecoef_ = lagrangeCoeffs(x,xs,ys)
    # for all datapoints
    for i in range(len(xs)):
        
        # add  l_i * y_i  to the polynomial
        P_x += lagrangecoef_(i) * ys[i]
        
    return P_x


y = lagrangePolynomial(xs, ys, 3750)

print("my lagrange: ", y)


from scipy.interpolate import lagrange
y_ = lagrange(xs,ys)(3750)
print("reference implementation: ", y_)