import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Funciones
def Grafica():
	datos = pd.read_csv('Datos.dat', header = 0, delim_whitespace  = True)
	plt.plot(datos.iloc[:,0], datos.iloc[:,1]*180/np.pi, label = "Desplazamiento angular", 		color = "blue")
	plt.ylabel("Desplazamiento angular (°)")
	plt.xlabel("Tiempo (s)")
	plt.title("Desplazamiento angular vs Tiempo")
	plt.legend(loc = 1)
	plt.grid()
	plt.show()
	
#Programa principal
ω, ω_aux, θ, θ_aux, t, t_f, g, l, Δt = 0, 0, 0, 15*np.pi/180, 0, 10, 9.81, 1, 0.05
file_plot = open("Datos.dat","w")
while t <= t_f:
	file_plot.write(str(round(t, 2)) + "\t" + str(θ_aux) + "\n")
	ω = ω_aux -(g/l)*θ_aux*Δt
	θ = θ_aux + Δt*ω
	θ_aux, ω_aux = θ, ω
	t += Δt
file_plot.close()
Grafica()
