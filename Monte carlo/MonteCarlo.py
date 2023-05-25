# Se trato con más intentos que los que se hicieron en este programa, pero me encontre con el problema de que mi computadora no tenia la suficiente potencia para simular tantos datos.

import matplotlib.pyplot as plt
import numpy as np
import random

x_ad, y_ad, x_af, y_af = [], [], [], []
p = 2000000
for i in range(9, p):
	x_r, y_r = random.uniform(0, 1), random.uniform(0, 1)
	if x_r**2 + y_r**2 < 1:
		x_ad.append(x_r)
		y_ad.append(y_r)
	else:
		x_af.append(x_r)
		y_af.append(y_r)		
	
π = 4*(len(x_ad)/p)
print("Area = " + str(len(x_ad)/p))
print("π = " + str(π))

#Grafica
def y(x):
	return np.sqrt(1 - x**2)
x = np.linspace(0, 1, 1000)
plt.plot(x, y(x), '-', color = 'black')
plt.plot(x_ad, y_ad, ',', color = 'blue')
plt.plot(x_af, y_af, ',', color = 'chocolate')
plt.ylabel("y")
plt.xlabel("x")
plt.title("Método de Montecarlo.")
plt.show()


