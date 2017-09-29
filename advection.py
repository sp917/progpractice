import math
import numpy
import matplotlib.pyplot as plt

# we shall solve the advection equation using FTBS

# dy/dt + u dy/dx = 0

# initial condition: y(x,0) = f(x) where we define f below

def f(x):
    if x<1 and x>=0:
        return 1
    else:
        return 0
X = 2 
N = 100
M = 100
δx = X/N 
T = 1
δt = T/M
c = 1

x = numpy.zeros(N)
for n in range(0,N):
    x[n] = n*δx

y = numpy.zeros(shape=(M,N))

#initialize:

for n in range(0,N):
    y[0][n] = f(x[n])

#iterate
for m in range(1,M):
    y[m][0] = 1
    for n in range(1,N):
        y[m][n] = y[m-1][n] - c*(y[m-1][n] - y[m-1][n-1])

plt.plot(x,y[80])
plt.show()

