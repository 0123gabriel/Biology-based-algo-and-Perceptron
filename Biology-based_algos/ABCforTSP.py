import random
import time
import numpy as np

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
    return cities

#Generar un camino de ciudades al azar
def generate_random_solution(num_cities):
    return random.sample(range(num_cities), num_cities)

#Calcular la distancia de un camino
def calculate_total_distance(solution, distances):
    total_distance = 0
    num_cities = len(solution)
    for i in range(num_cities - 1):
        total_distance += distances[solution[i]][solution[i+1]]
    total_distance += distances[solution[-1]][solution[0]]  # Volver a la primera ciudad
    return total_distance

#Abejas empleadas que trabajan en una solucion y coluciones cercanas a esta
#Se permuta dos ciudades y se comprueba si esto da una mejor solucion
def employed_bees_phase(solutions, distances):
    num_cities = len(solutions[0])
    num_solutions = len(solutions)
    for i in range(num_solutions):
        new_solution = list(solutions[i])
        index1, index2 = random.sample(range(num_cities), 2)
        new_solution[index1], new_solution[index2] = new_solution[index2], new_solution[index1]
        
        current_distance = calculate_total_distance(solutions[i], distances)
        new_distance = calculate_total_distance(new_solution, distances)
        
        if new_distance < current_distance:
            solutions[i] = new_solution

#Abejas observadoras que escogen una solucion segun su probabilidad y exploran una nueva solucion
#permutando dos ciudades de la misma
def onlooker_bees_phase(solutions, distances):
    num_solutions = len(solutions)
    probabilities = [1 / calculate_total_distance(solution, distances) for solution in solutions]
    total_prob = sum(probabilities)
    probabilities = [prob / total_prob for prob in probabilities]
    
    for _ in range(num_solutions):
        selected_solution = random.choices(solutions, probabilities)[0]
        new_solution = list(selected_solution)
        index1, index2 = random.sample(range(len(selected_solution)), 2)
        new_solution[index1], new_solution[index2] = new_solution[index2], new_solution[index1]
        
        current_distance = calculate_total_distance(selected_solution, distances)
        new_distance = calculate_total_distance(new_solution, distances)
        
        if new_distance < current_distance:
            solutions[solutions.index(selected_solution)] = new_solution

#Se cambia una posible solucion al azar
def scout_bees_phase(solutions, proba):
    num_solutions = len(solutions)
    for i in range(num_solutions):
        if random.random() < 1/proba:
            solutions[i] = generate_random_solution(len(solutions[i]))

#Algoritmo para encontrar el mejor camino
def abc_tsp(num_solutions, num_cities, distances, max_iterations, proba):
    solutions = [generate_random_solution(num_cities) for _ in range(num_solutions)]
    best_solution = min(solutions, key=lambda x: calculate_total_distance(x, distances))
    
    for _ in range(max_iterations):
        employed_bees_phase(solutions, distances)
        onlooker_bees_phase(solutions, distances)
        best_solution = min(solutions, key=lambda x: calculate_total_distance(x, distances))
        scout_bees_phase(solutions, proba)
    
    return best_solution, calculate_total_distance(best_solution, distances)

# Ejemplo de uso
inicio = time.time() #Medicion del tiempo de ejecucion
semilla = 4
random.seed(semilla)
numCities = 150
distances = randomCityDistances(numCities)
num_solutions = 150
max_iterations = 500
proba = 10

best_solution, best_distance = abc_tsp(num_solutions, numCities, distances, max_iterations, proba)

fin = time.time()

print("La mejor solución encontrada es: ", best_solution)
print("La distancia total es: ", best_distance)
print("Tiempo tardado: ", fin - inicio)