import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#setting up plot
ax = plt.figure().add_subplot(111, aspect='equal')

#defining points
P = np.array([4.0,1.0])

#defining lines
n = np.array([1,-1])
c = 0
m = omat@n

n=n.reshape((2,1))
m=m.reshape((2,1))

R1 = ((m@m.T-n@n.T)/(m.T@m+n.T@n))@P
R2 = c*n/np.linalg.norm(n)
R2=R2.reshape((1,2))
R = 2*(R1+R2)
R = np.array(R)[0]

#printing points
print("P=\n",P)
print("R=\n",R)

A = np.array((c,0))
m = np.array(m.T)[0]

print(A)
print(m)
#Generating the line
x_AB = line_gen(A,(P+R)/2)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$L$')

plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 - 0.05), R[1] * (1) , 'R')
ax.plot()

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
plt.savefig('../figs/reflection.pdf')
plt.savefig('../figs/reflection.eps')
subprocess.run(shlex.split("termux-open ../figs/reflection.pdf"))
#else
#plt.show()