import random
import heapq
import struct
import time

def iniciar_poblacion(inicio, fin, tamano_poblacion):
    x = [round(random.uniform(inicio, fin),5) for _ in range(tamano_poblacion)]
    y = [round(random.uniform(inicio, fin),5) for _ in range(tamano_poblacion)]
    return x,y

def evaluar_aptitud(x,y):
    datos = []
    for i in range(len(x)):
        f = (1.5 - x[i] + x[i]*y[i])**2 + (2.25 - x[i] + x[i]*(y[i]**2))**2 + (2.625 - x[i] + x[i]*(y[i]**3))**2
        datos.append([f,[x[i],y[i]]])
    return datos

def get_mejores(datos, num_elite):

    mejores_f = heapq.nsmallest(num_elite, datos)
    mejores_xy = []

    for i in mejores_f:
        mejores_xy.append(i[1])

    return mejores_xy

def float_a_binario(num):
    # Empaquetar el número como una cadena de bytes de 4 bytes (32 bits)
    packed = struct.pack('f', num)

    # Desempaquetar los bytes y convertirlos a una cadena binaria
    binary_representation = ''.join(f'{byte:08b}' for byte in packed)

    return binary_representation

def binario_a_float(binary):
    # Asegurarse de que la cadena tenga una longitud múltiplo de 8
    while len(binary) % 8 != 0:
        binary = '0' + binary

    # Dividir la cadena en bytes de 8 bits y convertirlos a enteros
    bytes_list = [int(binary[i:i+8], 2) for i in range(0, len(binary), 8)]

    # Empaquetar los bytes y desempaquetarlos como un número en coma flotante
    packed = struct.pack('4B', *bytes_list)
    result = struct.unpack('f', packed)[0]

    return result


#Genera las combianciones de todos los hijos
def cruzar(x):

    # Arreglo con los valores de x en binario
    x_bin = []
    for i in x:
        x_bin.append(float_a_binario(i))

    # Posicion para combinar a partes de los padres y generar a los hijos
    mitad = random.randint(0,len(x_bin[1])-1)
    x_bin_ab = []
    x_bin_arr = []
    for i in x_bin:
        x_bin_ab.append(i[:mitad])
        x_bin_arr.append(i[mitad:])

    hijos = []

    # Creacion de los hijos
    for i in range(len(x_bin_ab)):
        for j in range(len(x_bin_ab)):
            if i == j:
                pass
            else:
                hijos.append(x_bin_ab[i] + x_bin_arr[j])

    return hijos

# Generar la descendencia con las mutaciones          
def descendencia(hijos):
    for i in range(len(hijos)):
        if random.randint(1,100) <= prob_mutar:
            hijos[i] = mutar(hijos[i])
    
    hijos_final = descendencia_float(hijos)
    
    return hijos_final

# Funcion para mutar un numero float
def mutar(i):
    pos = random.randint(0,len(i)-1)
    cad_1 = i[:pos]
    cad_2 = i[(pos+1):]
    centro = int(i[pos])

    if centro == 1:
        centro = 0
    else:
        centro = 1

    mutado = cad_1 + str(centro) + cad_2
    return mutado    

# Cambio de binario a float
def descendencia_float(hijos_bin):
    hijos_float = []
    for hijo in hijos_bin:
        hijos_float.append(round(binario_a_float(hijo),8))
    return hijos_float


# Datos
inicio = -4.5
fin = 4.5
tamano = 100
numMejores = 10
prob_mutar = 10 # Este es el porcentaje (10%)
pobIniX, pobIniY = iniciar_poblacion(inicio, fin, tamano)
mejores_ep = []

for i in range(100):

    # Poblacion inicial
    currentX = pobIniX
    currentY = pobIniY

    # Evaluacion de la poblacion
    aptitud = evaluar_aptitud(currentX,currentY)

    # Mejores individuos de cada epoca
    mejores_ep.append(aptitud[0])

    # Mejores candidatos de X y Y
    mejoresXY = get_mejores(aptitud,numMejores)

    # Variables para guardar los mejores X y Y en arreglos diferentes
    mejoresX = []
    mejoresY = []

    for dato in mejoresXY:
        mejoresX.append(dato[0])
        mejoresY.append(dato[1])

    # Cruce de cada X con el resto de X's
    mejoresX_bin = cruzar(mejoresX)

    # Cruce de cada Y con el resto de Y's
    mejoresY_bin = cruzar(mejoresY)

    # Obtencion de la descendencia de cada X y Y despues de mutar algunos con una probabilidad del 10%
    descendenciaX = descendencia(mejoresX_bin)
    descendenciaY = descendencia(mejoresY_bin)

    # Reinicializacion de la poblacion
    pobIniX = descendenciaX
    pobIniY = descendenciaY

print("Mejores de cada epoca: ")
for i in range(len(mejores_ep)):
    print()
    print("Epoca", i)
    print("Valor de f: ", mejores_ep[i][0])
    print("Par ordenado: ", mejores_ep[i][1])


