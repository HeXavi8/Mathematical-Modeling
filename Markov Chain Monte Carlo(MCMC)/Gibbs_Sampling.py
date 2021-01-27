# A simple Gibbs sampler

from pylab import *
from numpy import *

def pXgivenY(y,m1,m2,s1,s2):
    return random.normal(m1 + (y-m2)/s2,s1)

def pYgivenX(x,m1,m2,s1,s2):
    return random.normal(m2 + (x-m1)/s1,s2)

def gibbs(N=5000):
    k=20
    x0 = zeros(N,dtype=float)
    m1 = 10
    m2 = 20
    s1 = 2
    s2 = 3
    for i in range(N):
        y = random.rand(1)
        # Each sample is iterated k times
        for j in range(k):
            x = pXgivenY(y,m1,m2,s1,s2)
            y = pYgivenX(x,m1,m2,s1,s2)
        x0[i] = x
    
    return x0

def f(x):
    return exp(-(x-10)**2/10)

# Draw the picture
N=10000
s=gibbs(N)
x1 = arange(0,17,1)
hist(s,bins=x1,fc='k')
x1 = arange(0,17, 0.1)
px1 = zeros(len(x1))
for i in range(len(x1)):
    px1[i] = f(x1[i])
plot(x1, px1*N*10/sum(px1), color='k',linewidth=3)

show()
