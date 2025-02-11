import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

x_real = pd.read_csv('XXOR.csv')
y_real = pd.read_csv('yXOR.csv')
x_real['x1^2'] = x_real['Input 1'] ** 2
x_real['x2^2'] = x_real['Input 2'] ** 2
x_real['z'] = x_real['x1^2'] + x_real['x2^2']

x1 = x_real[y_real['Output'] == 0]
x2 = x_real[y_real['Output'] == 1]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x1['Input 1'], x1['Input 2'], x1['z'])
ax.scatter(x2['Input 1'], x2['Input 2'], x2['z'])

plt.title('Dots Distribution in 3D with $x_1^2$ and $x_2^2$ function')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$z$')

plt.show()