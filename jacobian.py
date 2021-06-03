import sympy as sp
from sympy import pprint

# 1.a)


def a1():
    x1, x2 = sp.symbols('x1 x2')
    f1 = 5*x1*x2
    f2 = x1**2 * x2**2 + x1 + 2*x2
    f = sp.Matrix([f1, f2])
    X = sp.Matrix([x1, x2])
    Df = f.jacobian(X)
    Df0 = Df.subs([(x1, 1), (x2, 2)])
    # pprint(Df)
    # pprint(Df0)


a1()


def a2():
    x1, x2, x3 = sp.symbols('x1 x2 x3')
    f1 = sp.log(x1**2+x2**2)+x3**2
    f2 = sp.exp(x2**2+x3**2)+x1**2
    f3 = 1/(x3**2+x1**2)+x2**2
    f = sp.Matrix([f1, f2, f3])
    X = sp.Matrix([x1, x2, x3])
    Df = f.jacobian(X)
    Df0 = Df.subs([(x1, 1), (x2, 2), (x3, 3)])
    pprint(Df)
    # pprint(Df0)


a2()
