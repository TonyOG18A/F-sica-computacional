import matplotlib.pyplot as plt
import numpy as np
import random
from itertools import zip_longest

def Grafica(y):
	x = np.linspace(0, len(y), len(y), endpoint = False)
	plt.plot(x, y, 'o', color = 'red')
	plt.vlines(x, 0, y, color = 'red', linestyles = '-', lw = 1)
	plt.ylabel("P(n)")
	plt.xlabel("n")
	plt.title("Distribución de probabilidad (Experimental).")
	plt.grid()
	plt.show()
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
N, M, n, rep = 50, 500, 0, 1000
P_n_sum, n_fact = np.array([]), []
n_prom = 0
for k in range(0, rep):
	j = True
	casilla, H_n = [0]*M, []
	n = 0
	for i in range(0, N):
		r = random.randint(0, M-1)
		casilla[r] = casilla[r] + 1
	while j == True:
		cant = 0
		for t in range(0, M):
			if casilla[t] == n:
				cant += 1
		n += 1
		if cant != 0:
			H_n.append(cant)
		else:
			j = False
	P_n = np.array(H_n)/M
	P_n_sum = [x + y for x, y in zip_longest(P_n_sum, P_n, fillvalue = 0)]
for i in range(0, len(P_n_sum)):
	n_prom += i*P_n_sum[i]/rep
	n_fact.append(factorial(n))
print(n_prom)
print(np.array(P_n_sum)/rep)
Grafica(np.array(P_n_sum)/rep)
