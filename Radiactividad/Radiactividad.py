import matplotlib.pyplot as plt
import numpy as np
import random
import os

p, Δt, t_f, rep = 0.01, 1, 100, 100
nucleos = [0]*10000
N = np.array([0]*t_f)
beep = lambda x: os.system("echo -n '\a';sleep 0.01;" * x)
x = np.array([0]*100)
N_log = [0]*100
x_log = [0]*100
for e in range(0, rep):
	nucleos = [0]*10000
	con = 0
	for t in range(1, t_f):
		x[t] = t
		for n in range(0, 10000):
			r = random.uniform(0, 1)
			if r <= p and nucleos[n] == 0:
				nucleos[n] = 1
				con += 1
		N[t] = N[t] + 10000 - round(con)

N = N/100
N[0] = 10000
for t in range(0, 100):
	N_log[t] = np.log(N[t])
m, b = np.polyfit(x, N_log, 1)
print("λ = " + str(-m))
plt.plot(x, N, 'o', color = 'red', label = 'Datos')
plt.plot(x, np.exp(m*x+b), '-', color = 'black', label = 'Regresion')
plt.ylabel("N")
plt.xlabel("t")
plt.title("Decaimento radiactivo.")
plt.legend(loc = 1)
plt.grid()
plt.show()
