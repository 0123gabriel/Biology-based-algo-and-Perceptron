import numpy as np
from numpy import inf
import random
import time

#Generador de los nodos de las ciudades
def randomCityDistances(numCities):
    cities = np.zeros((numCities, numCities))
    for i in range(numCities):
        for j in range(numCities):
            if i == j:
                pass
            else:
                cities[i][j] = random.randint(1,20)
    
    for i in range(numCities-1):
        for j in range(numCities-1):
            if cities[i][j] == 0:
                distance = cities[i][j+1]
                cities[i+1][j] = distance
                cities[i][j] = np.inf
    cities[-1][-1] = np.inf
    return cities

#Calculo de los pesos de cada camino
def calculateTotalFactors(curLoc, alpha, beta, tempLengthProb):
    #Calculo de la nueva cantidad de feronomas y probabilidad segun la longitud de los ejes
    pheromoneF = np.power(pheromone[curLoc,:],beta)
    lengthProbF = np.power(tempLengthProb[curLoc,:],alpha)
                
    #Se aumenta una columna
    pheromoneF = pheromoneF[:,np.newaxis]
    lengthProbF = lengthProbF[:,np.newaxis]
                
    #Denominador de la probabilidad para escoger un camino
    totalFactors = np.multiply(pheromoneF, lengthProbF)  

    return totalFactors

#Seleccion de otra ciudad
def nextCity(totalFactors, total):
    #Probabilidad de cada camino
    probs = totalFactors/total

    #Probabilidad acumulada (debe sumar 1)
    cumProb = np.cumsum(probs)
                
    #Valor aleatorio para la toma de desicion
    r = random.random()
                
    #Seleccion del primer elemento mas grande que r
    city = np.nonzero(cumProb>r)[0][0]+1

    return city

#Calcular distancias de caminos seguidos por las hormigas
def calcDistances(m, n, everyAntRoute, distCost):
    for i in range(m):
        s = 0
        for j in range(n-1):
            s = s + d[int(everyAntRoute[i,j])-1,int(everyAntRoute[i,j+1])-1]
        distCost[i]=s
    return distCost

#Calculo del nuevo valor de las feromonas
def updatePheromone(pheromone, e, m, n, distCost, everyAntRoute):
    
    pheromone = (1-e)*pheromone #Evaporacion de la feromona
        
    #Actualizcion de la feromonas
    for i in range(m):
        for j in range(n-1):
            dt = 1/distCost[i]
            pheromone[int(everyAntRoute[i,j])-1,int(everyAntRoute[i,j+1])-1] = pheromone[int(everyAntRoute[i,j])-1,int(everyAntRoute[i,j+1])-1] + dt   
    return pheromone

#Funcion para buscar el camino mas corto
def antColonyOptimization(d, iteration, m, n, p, alpha, beta, pheromone, route, Q):
    
    #Reciproco de la distancia entre ciudades
    lengthProb = Q/d
    
    for _ in range(iteration):

        for i in range(m):
            #Copia de probabilidad segun la longitud para modificarla segun se mueva la hormiga y no 
            #alterar la inicial
            tempLengthProb = np.array(lengthProb)
            
            for j in range(n-1):
                #Vector con los pesos de cada camino (suma de feronomas y probabilidad segun 
                #la longitud de cada camino)
                totalFactors = np.zeros(5) 

                #Vector para guardar las probabilidades acumulativas y escoger el camino
                cumProb = np.zeros(5)
                
                #Se coloca un cero en la posicion actual
                curLoc = int(route[i,j]-1)
                tempLengthProb[:,curLoc] = 0

                #Calculo del vector de los pesos de cada camino
                totalFactors = calculateTotalFactors(curLoc, alpha, beta, tempLengthProb)
                total = np.sum(totalFactors)
                
                #Seleccionar nueva ciudad a visitar
                city = nextCity(totalFactors, total)

                #Se aniade la nueva ciudad a la ruta
                route[i,j+1] = city

            #Se aniade la ultima ciudad   
            left = list(set([i for i in range(1,n+1)])-set(route[i,:-2]))[0]
            route[i,-2] = left
        
        #Variable para la evaluacion de cada ruta de cada hormiga
        everyAntRoute = np.array(route)

        #Inicializacion del arreglo con la distancia de todas las rutas
        distCost = np.zeros((m,1))

        #Arreglo con las distancias finales
        distCost = calcDistances(m, n, everyAntRoute, distCost)

        #Se obtiene la mejor ruta a traves del indice de la distancia minima   
        dist_min_loc = np.argmin(distCost)
        dist_min_cost = distCost[dist_min_loc]
        best_route = route[dist_min_loc,:]

        pheromone = updatePheromone(pheromone, p, m, n, distCost, everyAntRoute)
                        
    return best_route, dist_min_cost

#Inicializacion de datos
inicio = time.time() #Medicion del tiempo de ejecucion
semilla = 4
random.seed(semilla)
nodes = 150
d = randomCityDistances(nodes)
iteration = 500
n_ants = nodes
n_cities = nodes
p = 0.5        #evaporacion de las feromonas
alpha = 1      #factor alfa de las feronomas
beta = 2       #factor beta para los caminos
Q = 1

#Feromonas iniciales en los caminos de las ciudades
pheromone = 0.1*np.ones((n_ants,n_cities))

#Inicializacion de un vector para guardar la ruta de las hormigas, y se coloca una columna extra
#porque las hormigas deben volver a la posicion inicial 
route = np.ones((n_ants,n_cities+1))

best_route, dist_min_cost = antColonyOptimization(d, iteration, n_ants, n_cities, p, alpha, beta, pheromone, route, Q)
best_route_list = best_route.tolist()

for i in range(len(best_route_list)):
    best_route_list[i] = int(best_route_list[i])

fin = time.time()

print('Mejor camino :', best_route_list)
print('Distancia recorrida: ', int(dist_min_cost[0]) + d[int(best_route[-2])-1,0])
print("Tiempo tardado: ", fin - inicio)