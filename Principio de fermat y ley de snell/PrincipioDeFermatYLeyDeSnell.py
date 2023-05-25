import numpy as np
import random 
import matplotlib.pyplot as plt
import pygame
import copy

# Configuraciones de ventana Pygame
dimensiones = [800, 600]
Cm1 = (200, 200, 200)
Cm2 = (0, 120, 255)
Cp = (100, 0, 0)
negro = (0, 0, 0)
trayectoria_ini = (0, 35, 254)
trayectoria_sim = (247, 157, 20)
# Abrir ventana en pygame
pygame.init()

ventana = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("LCO")
clock = pygame.time.Clock()

def dibujar(p, col):
	# Puntos y trayectoria
	pygame.draw.circle(ventana, negro, p[0], 5, 0)
	pygame.draw.circle(ventana, negro, p[8], 5, 0)
	for i in range(1, len(p)):
		pygame.draw.line(ventana, col, p[i - 1], p[i], 2)
def CalularLCOi(i, Pi, p):
	if i <= 3:
		LCOI = n2*(np.sqrt((p[0] - Pi[i - 1][0])**2 + (p[1] - Pi[i - 1][1])**2) + 				np.sqrt((p[0] - Pi[i + 1][0])**2 + (p[1] - Pi[i + 1][1])**2))
	elif i == 4:
		LCOI = n1*(np.sqrt((p[0] - Pi[i + 1][0])**2 + (p[1] - Pi[i + 1][1])**2))+ 				n2*np.sqrt((p[0] - Pi[i - 1][0])**2 + (p[1] - Pi[i - 1][1])**2)
	else: 
		LCOI = n1*(np.sqrt((p[0] - Pi[i - 1][0])**2 + (p[1] - Pi[i - 1][1])**2) + 				np.sqrt((p[0] - Pi[i + 1][0])**2 + (p[1] - Pi[i + 1][1])**2))
	return LCOI
# Medios
m1 = pygame.Surface([400, 600])
m1.fill(Cm1)
m2 = pygame.Surface([400, 600])
m2.fill(Cm2)
con = 0
# Variables a utilizar en la simulacion
pi = [[800, 150], [700, random.uniform(150, 300)], [600, random.uniform(150, 300)], [500, random.uniform(150, 300)], [400, random.uniform(150, 300)], [300, random.uniform(150, 300)], [200, random.uniform(150, 300)], [100, random.uniform(150, 300)], [0, 300]]
pi_aux = copy.deepcopy(pi)
n1, n2 = 1, 1.5
d = 2
LCOi = [0]*9

running = True
while running:
	t = 0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			θi = np.arctan((300 - pi[4][1])/400) 
			θf = np.arctan((pi[4][1] - 150)/400)
			print("n_1*sen(θ_i) = " + str(n1*np.sin(θi)) + ".\n")
			print("n_2*sen(θ_f) = " + str(n2*np.sin(θf)) + ".")
	ventana.blit(m1, (0, 0))	
	ventana.blit(m2, (400, 0))
	dibujar(pi_aux, trayectoria_ini)
	dibujar(pi, trayectoria_sim)
	i = random.randint(1, 7)
	P = pi[i]
	P_aux = P
	LCOi_aux = CalularLCOi(i, pi, P)
	Conf = True
	c = 0
	while Conf:
		c += 1
		LCOi[i] = CalularLCOi(i, pi, P)
		if LCOi[i] < LCOi_aux:
			pi[i][1] = P[1]
			Conf = False
		else:
			P = P_aux
			
		r = random.uniform(-1, 1)
		P[1] = P[1] + d*r	
	pygame.display.flip()
	clock.tick(60)
