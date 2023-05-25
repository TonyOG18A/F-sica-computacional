import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

def pbcPosition(s, L):
	if s > L:
		s -= L
	elif s < 0:
		s += L
	return s
	
def pbcSeparation(ds, L):
	if ds > 0.5*L:
		ds -= L
	elif ds < -0.5*L:
		ds += L
	return ds
N, L, dt = 64, 10, 0.01
vxSum, vySum = 0, 0
posx, posy = [], []
vx, vy = [0]*64, [0]*64

# posiciones iniciales
for r in range(1, 9):
	for c in range(1, 9):
		posx.append(1.125*r)
		posy.append(1.125*c)
# velocidades iniciales
for i in range(0, N):
	vx[i] = random.uniform(-0.5, 0.5)
	vy[i] = random.uniform(-0.5, 0.5)
	vxSum += vx[i]
	vySum += vy[i]
vxcm, vycm = vxSum/N, vySum/N
for i in range(0, N):
	vx[i] -= vxcm
	vy[i] -= vycm
v2Sum = 0
for i in range(0, N):
	v2Sum += vx[i]**2 + vy[i]**2
EnergiaCineticaPorParticula = 0.5*v2Sum/N
#Animacion
fig = plt.figure()
axes = fig.gca()
jaula = [[0, 10, 10, 0, 0], [0, 0, 10, 10, 0]]
def actualizar(T):
	axes.clear()
	axes.plot(jaula[0], jaula[1], "-", color = "black")
	axes.plot(posx, posy, "o", color = "red")	
	plt.title("t= " + str(round(T*dt, 2)))
	axes.set_ylabel("y")
	axes.set_xlabel("x")
	ax, ay = [0]*64, [0]*64
	AcumuladorDeEnergiaPotencialTotal = 0
	AcumuladorVirial = 0
	for i in range(0, N - 1):
		for j in range(i + 1, N):
			dx = pbcSeparation(posx[i] - posx[j], L)
			dy = pbcSeparation(posy[i] - posy[j], L)
			r2 = dx**2 + dy**2
			unoEntreR2 = 1/r2
			unoEntreR6 = unoEntreR2**3
			fEntreR = 48*unoEntreR6*(unoEntreR6 - 0.5)*unoEntreR2
			fx = fEntreR*dx
			fy = fEntreR*dy
			ax[i] += fx
			ay[i] += fy
			ax[j] -= fx
			ay[j] -= fy
			AcumuladorDeEnergiaPotencialTotal += 4*(unoEntreR6**2 - unoEntreR6)
			AcumuladorVirial += dx*fx + dy*fy
	#Actualizar posiciones
	for i in range(0, N):
		posx[i] += vx[i]*dt + 0.5*ax[i]*dt**2
		posy[i] += vy[i]*dt + 0.5*ay[i]*dt**2
		posx[i] = pbcPosition(posx[i], L)
		posy[i] = pbcPosition(posy[i], L)
		vx[i] += 0.5*ax[i]*dt
		vy[i] += 0.5*ay[i]*dt
		
	#plt.grid()
ani = animation.FuncAnimation(fig, actualizar, 1000, interval = 100)
plt.show()
ani.save('Animación.gif', writer='ffmpeg', fps=20);

