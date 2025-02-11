import random
import heapq

# Funcion para iniciar las  particulas
def iniciar_swarm(inicio, fin, tamano_poblacion):
    x = [round(random.uniform(inicio, fin),5) for _ in range(tamano_poblacion)]
    y = [round(random.uniform(inicio, fin),5) for _ in range(tamano_poblacion)]
    return x,y

# Funcion para iniciar las velocidades de las particulas
def iniciar_Vels(tamano_poblacion):
    v = [0]*tamano_poblacion
    #v = [round(random.uniform(-3, 3),5) for _ in range(tamano_poblacion)]
    return v

# Funcion para evaluar la funcion y la aptitud de las particulas
# Se retorna dos arreglos. Uno con los valores de la funcion y el valor de X que lo genero, y otro con
# los valores de Y
def evaluar_aptitud(x,y):
    datosX = []
    datosY = []
    for i in range(len(x)):
        f = (1.5 - x[i] + x[i]*y[i])**2 + (2.25 - x[i] + x[i]*(y[i]**2))**2 + (2.625 - x[i] + x[i]*(y[i]**3))**2
        datosX.append([f, x[i]])
        datosY.append([f, y[i]])
    return datosX, datosY

# Se obtiene la mejor posicion de cada X comparandola con las posiciones anteriores
def get_BestPersonal(p_ij, x):
    for i in range(len(x)):
        if x[i][0] < p_ij[i][0]:
            p_ij[i] = x[i]
    return p_ij

# Se obtiene la posicion de cada X con respecto a todas
def get_BestGlobal(x):
    return heapq.nsmallest(1,x)[0][1]

# Funcion para calcular la siguiente posicion
def calcularXplus1(x, v_ijplus1):
    xplus1 = []
    for i in range(len(x)):
        xplus1.append(x[i] + v_ijplus1[i])
    return xplus1

# Funcion para calular la siguiente velocidad
def calcularVplus1(v, a1, p1, p_ij, x_ij, a2, p2, p_gj):
    vplus1 = []
    for i in range(len(v)):
        vplus1.append(v[i] + a1*p1*(p_ij[i][1] - x_ij[i]) + a2*p2*(p_gj - x_ij[i]))
    return vplus1

# Datos
inicio = -4.5
fin = 4.5
tamano_poblacion = 100
alpha_1 = 1
alpha_2 = 1
phi_1 = random.random()
phi_2 = random.random()

# Inicializacion de las particulas y velocidades
swarmInicialX, swarmInicialY = iniciar_swarm(inicio, fin, tamano_poblacion)
velocidadesX = iniciar_Vels(tamano_poblacion)
velocidadesY = iniciar_Vels(tamano_poblacion)

# La mejor posicion al inicio es la actual, por lo que los valores de p_ij son los mismos que la aptitud
p_xj, p_yj = evaluar_aptitud(swarmInicialX, swarmInicialY)

for i in range(100):

    # Se inicializan valores para cada iteracion
    currentX = swarmInicialX
    currentY = swarmInicialY
    currentVX = velocidadesX
    currentVY = velocidadesY

    # Calculo de la aptitud de cada iteracion
    aptitudX, aptitudY = evaluar_aptitud(currentX, currentY)

    # Re asignacion de los de p_ij basados en los anteriores y los nuevos obtenidos de evaluar los 
    # nuevos valores de X
    p_xj = get_BestPersonal(p_xj, aptitudX)
    p_yj = get_BestPersonal(p_yj, aptitudY)

    # Mejor valor de X con respecto a los demas y a cada iteracion
    p_gx = get_BestGlobal(p_xj)
    p_gy = get_BestGlobal(p_yj)

    # Calculo de la velocidad en t + 1 y reasignacion para la siguiente iteracion
    velocidadesX = calcularVplus1(currentVX, alpha_1, phi_1, p_xj, currentX, alpha_2, phi_2, p_gx)
    velocidadesY = calcularVplus1(currentVY, alpha_1, phi_1, p_yj, currentY, alpha_2, phi_2, p_gy)

    # Calculo de la posicion en t + 1 y reasignacion para la siguiente iteracion
    swarmInicialX = calcularXplus1(currentX, velocidadesX)
    swarmInicialY = calcularXplus1(currentY, velocidadesY)

print("Valor de X: ", p_gx)
print("Valor de Y: ", p_gy)
print("Valor de la funcion: ", evaluar_aptitud([p_gx], [p_gy])[0][0][0])
