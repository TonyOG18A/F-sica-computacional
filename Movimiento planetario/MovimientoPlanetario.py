import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def Grafica():
	planetas = ["Saturno", "Jupiter", "Marte", "Tierra", "Venus"]
	colores = ["orange", "darkgoldenrod", "red", "blue", "darkorange"]
	datos = pd.read_csv('Datos.dat', header = 0, delim_whitespace = True)
	for i in range(0, 5):
		plt.plot(datos.iloc[:, 2*i + 1], datos.iloc[:, 2*(i + 1)], label = planetas[i], color = 			colores[i])
	plt.plot(0, 0, 'o', color = "yellow", label = "Sol")
	plt.title("Órbitas")
	plt.ylabel("y (UA)")
	plt.xlabel("x (UA)")
	plt.legend(loc = 1)
	plt.grid()
	plt.show()

# Producto de la constante gravitacional con la masa del Sol en unidades astronomicas
GM_S = 4*(np.pi**2) # UA³/Años²
# Radio de la orbita terrestre en unidades astronomicas
R = np.array([9.58, 5.20, 1.52, 1, 0.72]) # UA
# Variables que se utilizaran en la simulacion
t, Δt, v_aux = 0, 0.01, 2
planetas = ["Saturno", "Jupiter", "Marte", "Tierra", "Venus"]
V_f = []
Grafica()
print("Estimando valores de las velocidades orbitales")
for i in range(0, 5):
	Conf = True
	v = v_aux
	if i < 2:
		Δt = 0.01
		redondeo = 2
	else:
		Δt = 0.001
		redondeo = 3
	while Conf == True:
		ω = v/R[i]
		x = R[i]*np.cos(ω*round(t, redondeo))
		y = R[i]*np.sin(ω*round(t, redondeo))
		t += Δt
		if round(ω*round(t, redondeo), 2) == round(2*np.pi, 2):
			if round((t**2)/((x**2+y**2)**1.5), 2) == 1:
				V_f.append(v)
				v_aux = v
				Conf = False
				if i == 0:
					t_f = t
				t = 0
			else:
				t = 0
				v += 0.01
t = 0
Δt = 0.01
file_plot = open('Datos.dat', 'w')
while t <= t_f:
	file_plot.write(str(round(t, 2)))
	for i in range(0, 5):
		ω = V_f[i]/R[i]
		x = R[i]*np.cos(ω*t)
		y = R[i]*np.sin(ω*t)
		file_plot.write("\t" + str(x) + "\t" + str(y))
	file_plot.write("\n")
	t += Δt
file_plot.close()

