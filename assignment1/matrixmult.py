import numpy as np

a = np.array([[ 1, 0 ,0], [ 0, np.cos(np.pi/3) ,(-1)*np.sin(np.pi/3)], [ 0, np.sin(np.pi/3) ,np.cos(np.pi/3)]])
b = np.array([[np.cos(np.pi/6), (-1)*np.sin(np.pi/6), 0],[np.sin(np.pi/6),np.cos(np.pi/6),0], [0,0,1]])
print("a*b")
print (a*b)
print("b*a=")
print (b*a)
