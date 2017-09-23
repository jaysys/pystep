#Numpy
import numpy as np

num_puntos = 100
conjunto_puntos = []

for i in xrange(num_puntos):
	x1= np.random.normal(0.0, 0.9)
	y1= x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.05)
	conjunto_puntos.append([x1, y1])

x_data = [v[0] for v in conjunto_puntos]
y_data = [v[1] for v in conjunto_puntos]

#Graphic display
import matplotlib.pyplot as plt

plt.plot(x_data, y_data, 'ro')
plt.legend()
plt.show()
print("done~@!!!")


