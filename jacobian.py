import sympy as sp
from sympy import pprint

import numpy as np

# jacobian matricies for multivariate functions

# 2d example
def a1():
    x1, x2 = sp.symbols('x1 x2')
    f1 = 5*x1*x2
    f2 = x1**2 * x2**2 + x1 + 2*x2
    f = sp.Matrix([f1, f2])
    X = sp.Matrix([x1, x2])
    Df = f.jacobian(X)
    Df0 = Df.subs([(x1, 1), (x2, 2)])
    pprint(Df)
    pprint(Df0)
# a1()

# 3d example
def a2():
    x1, x2, x3 = sp.symbols('x1 x2 x3')

    # assemble vectors f and x
    f1 = sp.log(x1**2+x2**2)+x3**2
    f2 = sp.exp(x2**2+x3**2)+x1**2
    f3 = 1/(x3**2+x1**2)+x2**2
    f = sp.Matrix([f1, f2, f3])
    X = sp.Matrix([x1, x2, x3])

    Df = f.jacobian(X)

    # compute for actual values
    Df0 = Df.subs([(x1, 1), (x2, 2), (x3, 3)])
    pprint(Df)
    pprint(Df0)
# a2()


# example linearization of a multivariable function via tangent plane
def a3():
    x1, x2, x3 = sp.symbols('x1 x2 x3')

    # define vectors
    f1 = x1+x2**2-x3**2-13
    f2 = sp.log(x2/4)+sp.exp(x3/2-1)
    f3 = (x2-3)**2-x3**3+7
    f = sp.Matrix([f1,f2,f3])
    X = sp.Matrix([x1,x2,x3])

    Df = f.jacobian(X)

    # lambdify for use with numpy values
    func = sp.lambdify([(x1,x2,x3)], f, "numpy")
    jac = sp.lambdify([(x1,x2,x3)], Df, "numpy")

    # get jacobian at point v for slopes in all dimensions
    v = np.array([1.5,3,2.5])
    DF = jac(v)

    # tangent plane equation for linearization
    # around neighbourhood of point v 
    def g(x): func(v)+jac(v)*(x-v)

    pprint(func(v))
    # g(v+delta) is close to func(v+delta) in vicinity of v
    pprint(DF)
a3()