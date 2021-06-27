import sympy as sp
import numpy as np

# https://en.wikipedia.org/wiki/Newton's_method#Nonlinear_systems_of_equations
# not to be confused with the non-generalized version

sp.init_printing()

x1, x2 = sp.symbols('x1 x2')
f1 = 20-18*x1-2*x2**2
f2 = -4*x2*(x1-x2**2)
f = sp.Matrix([f1,f2])
X = sp.Matrix([x1,x2])
Df = f.jacobian(X)

# either subs or ..
Df0 = Df.subs([(x1,1.1),(x2,0.9)])
sp.pprint(Df0)

# .. evaluate as numpy function
jac = sp.lambdify([[(x1,x2)]], Df, "numpy")
F = sp.lambdify([[(x1,x2)]],f,"numpy")

print("jacobian")
sp.pprint(Df)

print("1st iteration")
x0 = np.array([[1.1,0.9]])
delta0 = np.linalg.solve(jac(x0), -F(x0))
x1 = np.add(x0,delta0.T)
print(delta0)
print(x1)

print("2nd iteration")
delta1 = np.linalg.solve(jac(x1), -F(x1))
x2 = np.add(x1,delta1.T)
print(delta1)
print(x2)


def newtonIteration(x_0,Df,stop):
    """
    this function will continue Newton Iterations until a
    stopping criterion is met.
    :param x_0: start vector
    :param Df: Jacobian
    :param stop: (x) -> Bool. Stop when True. x[i] equals x_i
    :return: (x[])
    """
    x = [x_0]
    i = 0
    while(not stop(x)):
        delta_i = np.linalg.solve(Df(x[-1]), -F(x[-1]))
        x.append(x[-1]+delta_i.T)
        i+=1
    
    
    return x


# run for 3 iterations
x = newtonIteration(x0,jac,lambda x:len(x)==3)


# run until really close to root
tol = 1e-10
def closeToRoot(x):
    # iterate until error is less than tolerance
    return np.linalg.norm(F(x[-1]))<tol

x = newtonIteration(x0,jac,closeToRoot)
sp.pprint(x)


# find roots for different starting points:
x01 = np.array([[-1200,1600]])
x02 = np.array([[-220,100]])
x03 = np.array([[750,950]])
x04 = np.array([[250,250]])

roots = []

for x_0 in [x01,x02,x03,x04]:
    root = newtonIteration(x_0,Df,f,closeToRoot)[-1]
    print(root)
    roots.append(root)
