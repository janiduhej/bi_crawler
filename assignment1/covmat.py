import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

x = []
y = []
#read data
with open("covtest.dat", "r") as file:
    for row in file:
        r1, r2 =(float(val) for val in row.strip().split(" "))
        x.append(r1)
        y.append(r2)

#calculate covmat
data = np.vstack((x, y)).T
mean = np.mean(data, axis=0)
covmat = np.cov(x,y)
print(data)
print("mean:")
print(mean)
print("covmat:")
print(covmat)

#https://stackoverflow.com/questions/20126061/creating-a-confidence-ellipses-in-a-sccatterplot-using-matplotlib
def eigsorted(covmat):
    vals, vecs = np.linalg.eigh(covmat)
    order = vals.argsort()[::-1]
    return vals[order], vecs[:,order]


#https://www.visiondummy.com/2014/04/draw-error-ellipse-representing-covariance-matrix/
w, v = eigsorted(covmat)
alpha = np.arctan2(*v[:,0][::-1])

#angle_degree = alpha*(180/math.pi)
nstd = 2
width, height = 2* nstd * np.sqrt(w)

fig, ax = plt.subplots(nrows=1, ncols=1)
xmin, ymin = np.min(data, axis = 0)
xmax, ymax = np.max(data, axis = 0)
ax.set_xlim(xmin -1, xmax +1)
ax.set_ylim(ymin -1, ymax +1)
plt.scatter(data[:,0], data[:,1])

el = Ellipse(xy = mean, width=width, height=height, angle=np.degrees(alpha), edgecolor='red', fc='r', lw=3, alpha=0.2)

ax.add_patch(el)
plt.savefig("covmat.png")
plt.show
