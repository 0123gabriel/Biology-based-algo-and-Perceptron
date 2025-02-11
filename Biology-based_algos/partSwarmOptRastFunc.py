import random
import heapq
import math
import numpy as np

# Funcion para iniciar las  particulas
def iniciar_swarm(inicio, fin, tamano_poblacion, n):
    x = []
    for _ in range(tamano_poblacion):
        xi = [round(random.uniform(inicio, fin),5) for _ in range(n)]
        x.append(xi)
    return x

# Funcion para iniciar las velocidades de las particulas
def iniciar_Vels(tamano_poblacion, n):
    velocidades = []
    for _ in range(tamano_poblacion):
        v = [0]*n
        velocidades.append(v)
    #v = [round(random.uniform(-3, 3),5) for _ in range(tamano_poblacion)]
    return velocidades

# Funcion para evaluar la funcion y la aptitud de las particulas
# Se retorna dos arreglos. Uno con los valores de la funcion y el valor de X que lo genero, y otro con
# los valores de Y
def evaluar_aptitud(x):
    datosX = []
    for i in range(len(x)):
        f = A*n + sum([(xi**2 - A * math.cos(2 * math.pi * xi)) for xi in x[i]])
        datosX.append([f, x[i]])
    return datosX

# Se obtiene la mejor posicion de cada X comparandola con las posiciones anteriores
def get_BestPersonal(p_ij, x):
    for i in range(len(x)):
        if x[i][0] < p_ij[i][0]:
            p_ij[i] = x[i]
    return p_ij

# Se obtiene la posicion de cada X con respecto a todas
def get_BestGlobal(x):
    return heapq.nsmallest(1,x)[0][1]

#swarmInicialX = calcularXplus1(currentX, velocidadesX)

# Funcion para calcular la siguiente posicion
def calcularXplus1(x, v_ijplus1):
    xplus1 = []
    for i in range(len(x)):
        xi = np.array(x[i])
        vijplus1 = np.array(v_ijplus1[i])
        result = xi + vijplus1
        xplus1.append(result.tolist())
    return xplus1

# Funcion para calular la siguiente velocidad
def calcularVplus1(v, a1, p1, p_ij, x_ij, a2, p2, p_gj):
    vplus1 = []
    for i in range(len(v)):
        vi = np.array(v[i])
        pij = np.array(p_ij[i][1])
        xij = np.array(x_ij[i])
        pgj = np.array(p_gj)
        result = (vi + a1*p1*(pij - xij) + a2*p2*(pgj - x_ij))
        vplus1.append(result.tolist())
    return vplus1[0]

# Datos
A = 10
n = 10
inicio = -5.12
fin = 5.12
tamano_poblacion = 100
alpha_1 = 1
alpha_2 = 1
phi_1 = random.random()
phi_2 = random.random()

# Inicializacion de las particulas y velocidades
swarmInicialX = iniciar_swarm(inicio, fin, tamano_poblacion, n)
velocidadesX = iniciar_Vels(tamano_poblacion, n)

# La mejor posicion al inicio es la actual, por lo que los valores de p_ij son los mismos que la aptitud
p_xj = evaluar_aptitud(swarmInicialX)

for i in range(300):

    # Se inicializan valores para cada iteracion
    currentX = swarmInicialX
    currentVX = velocidadesX
    #print("CurrentX: ", currentX)
    #print("CurrentVelX:", currentVX)
    #print("pxj: ",p_xj)

    # Calculo de la aptitud de cada iteracion
    aptitudX = evaluar_aptitud(currentX)
    #print("aptitudX: ", aptitudX)

    # Re asignacion de los de p_ij basados en los anteriores y los nuevos obtenidos de evaluar los 
    # nuevos valores de X
    p_xj = get_BestPersonal(p_xj, aptitudX)
    #print("pxj: ",p_xj)

    # Mejor valor de X con respecto a los demas y a cada iteracion
    p_gx = get_BestGlobal(p_xj)
    #print("pgx: ",p_gx)

    # Calculo de la velocidad en t + 1 y reasignacion para la siguiente iteracion
    velocidadesX = calcularVplus1(currentVX, alpha_1, phi_1, p_xj, currentX, alpha_2, phi_2, p_gx)
    #print("VelocidadesX: ", velocidadesX)
    # Calculo de la posicion en t + 1 y reasignacion para la siguiente iteracion
    swarmInicialX = calcularXplus1(currentX, velocidadesX)
    #print("swarmInicialX: ", swarmInicialX)

print("Valores del vector X: ")
for i in range(len(p_gx)):
    if i == 0:
        print("[", p_gx[i])

    elif i == len(p_gx)-1:
        print(p_gx[i], "]")

    else:
        print(p_gx[i])
print("Valor de la funcion: ", evaluar_aptitud([p_gx])[0][0])
