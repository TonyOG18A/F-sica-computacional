import matplotlib.pyplot as plt
import numpy as np
import pygame

def Grafica(tierra_x, tierra_y, jupiter_x, jupiter_y):
	plt.plot(tierra_x, tierra_y, label = "Tierra", color = "blue")
	plt.plot(jupiter_x, jupiter_y, label = "Júpiter", color = "goldenrod")
	plt.plot(0, 0, 'o', color = "yellow", label = "Sol")
	plt.title("Órbitas")
	plt.ylabel("y (UA)")
	plt.xlabel("x (UA)")
	plt.legend(loc = 1)
	plt.grid()
	plt.show()

# Producto de la constante gravitacional con la masa del Sol en unidades astronomicas
GM_S = 4*(np.pi**2) # UA³/Años²
# Posiciones iniciales de los planetas
xy_J, xy_T = np.array([5.20, 0]), np.array([1, 0])
# Velocidades de los planetas
v_J, v_T = np.array([0, 2.75]), np.array([0, 6.28])
# Masas de los 3 cuerpos  en relación a la masa terrestre
M_J, M_T, M_S = 1000*317.83, 1, 333000
# Variables que se utilizaran en la simulacion
t, Δt, plot_Tx, plot_Jx, plot_Ty, plot_Jy = 0, 0.001, [], [], [], []
# Configuraciones de pygame
negro, azul, amarillo, blanco, cremita = (0, 0, 0), (0, 0, 255), (255, 255, 0), (255, 255, 255), (245, 181, 89)
dimensiones = np.array([800, 800])

# Abrir ventana en pygame
pygame.init()

ventana = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Movimiento planetario.")
clock = pygame.time.Clock()

# Consideré una escala de 200 pixeles = 1 UA
def dibujar(pos_Tierra, pos_Jupiter):
	# Tierra
	pygame.draw.circle(ventana, azul , pos_Tierra, 5 , 0)
	# Sol
	pygame.draw.circle(ventana, amarillo, np.array(dimensiones)/2, 20, 0)
	# Jupiter
	pygame.draw.circle(ventana, cremita, pos_Jupiter, 15, 0)
	# Mostrar en pantalla datos
	fuente = pygame.font.SysFont("calibri", 25)
	tiempo = "t = " + str(round(t, 1)) + " años" 
	etiqueta = fuente.render(tiempo, 1, blanco)
	ventana.blit(etiqueta, [600, 100])


run = True
while run:
	clock.tick(600)
	ventana.fill(negro)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Grafica(plot_Tx, plot_Ty, plot_Jx, plot_Jy)
			run = False
			
	# Calular las distancias entre cada cuerpo
	r_T = np.linalg.norm(xy_T)
	r_J = np.linalg.norm(xy_J)
	r_TJ = np.linalg.norm(xy_J - xy_T)
	# Calcular la nueva velocidad de los planetas
	# Tierra
	v_T = v_T + GM_S*(((M_J/M_S)*(xy_J - xy_T))/(r_TJ**3) - xy_T/(r_T**3))*Δt
	# Jupiter
	v_J = v_J - GM_S*(((M_T/M_S)*(xy_J- xy_T))/(r_TJ**3) + xy_J/(r_J**3))*Δt
	
	# Calcular la nueva posición de los planetas
	# Tierra
	xy_T = xy_T + v_T*Δt
	# Jupiter
	xy_J = xy_J + v_J*Δt
	# Datos a graficar
	
	plot_Tx.append(xy_T[0])
	plot_Ty.append(xy_T[1])
	plot_Jx.append(xy_J[0])
	plot_Jy.append(xy_J[1])
	dibujar(xy_T*55 + dimensiones/2, xy_J*55 + dimensiones/2)
	t += Δt
	pygame.display.update()
