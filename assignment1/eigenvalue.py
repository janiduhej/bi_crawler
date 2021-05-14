import numpy as np
from numpy import linalg as LA

r = np.array([[ 0.1729, -0.1468 ,0.9739], [ 0.9739, 0.1729 ,0.1468], [ -0.1468, -0.9739 ,0.1729]])

t = np.matrix.trace(r)
print("Spur der Matrix R:")
print (t)

a = np.arccos((t-1)/2)
print(a)
u=(a/2*np.sin(a))
v = u * np.array([[-0.9739+0.1468,0.9739+0.1468,0.9739+0.1468]])
print(v)

x, y = LA.eig(r)
print("Eigenwerte:")
print(x)
print("Eigenvektoren:")
print(y)

print("The numpy.linalg.eig function returns a tuple consisting of a vector "
      "and an array. The vector (here w) contains the eigenvalues. The array "
      "(here v) contains the corresponding eigenvectors, one eigenvector per "
      "column. The eigenvectors are normalized so their Euclidean norms are 1.")