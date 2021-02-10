import numpy as np
import scipy as sp
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
%matplotlib inline

# Objective function
def real_func(x):
    return np.sin(2*np.pi*x)

# Polynomial
# ps: numpy.poly1d([1,2,3])  -->  $1x^2+2x^1+3x^0$*
def fit_func(p, x):
    f = np.poly1d(p)
    return f(x)

# Residual
def residuals_func(p, x, y):
    ret = fit_func(p, x) - y
    return ret


# Ten points
x = np.linspace(0, 1, 10)
x_points = np.linspace(0, 1, 1000)
# The value of the objective function plus the normal distribution noise
y_ = real_func(x)
y = [np.random.normal(0, 0.1)+y1 for y1 in y_]

def fitting(M=0):
    """
    n is the degree of the polynomial
    """
    # Randomly initialize polynomial parameters
    p_init = np.random.rand(M+1)
    # Least squares
    p_lsq = leastsq(residuals_func, p_init, args=(x, y))
    print('Fitting Parameters:', p_lsq[0])

    # Visualization
    plt.plot(x_points, real_func(x_points), label='real')
    plt.plot(x_points, fit_func(p_lsq[0], x_points), label='fitted curve')
    plt.plot(x, y, 'bo', label='noise')
    plt.legend()
    return p_lsq


# M=0
p_lsq_0 = fitting(M=0)

# M=1
p_lsq_1 = fitting(M=1)
