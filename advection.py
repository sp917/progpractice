import numpy as np
import matplotlib.pyplot as plt

# we shall solve the advection equation using FTBS

# dy/dt + u dy/dx = 0

# initial condition: y(x,0) = f(x) where we define f below

X = 2 

def f(x):
    return 1 - (x%X>0.5) - (x%X<0.25)
    


N = 100
M = 100
δx = X/N 
T = 10
δt = T/M
c = 0.9 # c = uδt/δx
C = c*δx/δt

x = np.zeros(N)
for n in range(0,N):
    x[n] = n*δx

y = np.zeros(shape=(M,N))

#initialize:

y[0] = f(x)


A = np.zeros(shape=(N,N))
for n in range(1,M):
    for k in range(0,M):
        A[n][k] = (1-c)*(n==k) + c*(n==((k+1)%M))

A[0][N-1] = 1

#iterate
for m in range(1,M):
    y[m] = np.dot(A,y[m-1]) 


#now plot exact solution
ytrue = np.copy(y)
for m in range(0,M):
    for n in range(0,N):
        ytrue[m][n] = f(x[n]-C*m*δt)

t = 9.99
m = int(M*t/T)
plt.axis([0,X,0,1.2])
plt.plot(x,y[m])
plt.plot(x,ytrue[m])
plt.show()

