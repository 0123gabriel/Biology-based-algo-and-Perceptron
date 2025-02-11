import random
import time

# Generacion de ciudades y sus ubicaciones
def citiesGenerator(num_cities):
    cities = {}
    for i in range(num_cities):
        x = random.randint(1,20)
        y = random.randint(1,20)
        cities[str(i)] = (x,y)
    return cities

# Función para calcular la distancia entre dos ciudades
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

# Función para calcular la distancia total de una ruta
def total_distance(route):
    total = 0
    for i in range(len(route)-1):
        total += distance(cities[route[i]], cities[route[i+1]])
    total += distance(cities[route[-1]], cities[route[0]])  # Volver al punto de partida
    return total

# Generar una población inicial
def generate_population(population_size):
    population = []
    for _ in range(population_size):
        route = list(cities.keys())
        random.shuffle(route)
        population.append(route)
    return population

# Función de selección (usando selección por torneo)
def selection(population, num_parents):
    parents = []
    for _ in range(num_parents):
        tournament = random.sample(population, 3)
        winner = min(tournament, key=lambda x: total_distance(x))
        parents.append(winner)
    return parents

# Función de cruce (crossover)
def crossover(parent1, parent2):
    start = random.randint(0, len(parent1)-1)
    end = random.randint(start, len(parent1))
    child = parent1[start:end] + [city for city in parent2 if city not in parent1[start:end]]
    return child

# Función de mutación (intercambio de dos ciudades)
def mutate(route, prob_mut):
    if random.randint(1,100) <= prob_mut:
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]
        return route
    else:
        return route

# Algoritmo genético
def genetic_algorithm(num_generations, population_size, num_parents, prob_mut):
    population = generate_population(population_size)
    #print(len(population))

    for generation in range(num_generations):
        parents = selection(population, num_parents)
        #print("Parents: ")
        #print(len(parents))
        offspring = []

        for i in range(0, len(parents), 2):
            child1 = crossover(parents[i], parents[i+1])
            child2 = crossover(parents[i+1], parents[i])
            offspring.extend([mutate(child1, prob_mut), mutate(child2, prob_mut)])

        population = parents + offspring

    best_route = min(population, key=lambda x: total_distance(x))
    return best_route, total_distance(best_route)

# Definir las ciudades y sus coordenadas, y el resto de datos
inicio = time.time()
semilla = 4
random.seed(semilla)
num_cities = 150
cities = citiesGenerator(num_cities)
num_generations=500
population_size=50
num_parents=30
prob_mut = 10

# Uso del algoritmo genético
best_route, distance = genetic_algorithm(num_generations, population_size, num_parents, prob_mut)
fin = time.time()

best_route_int = []
for i in best_route:
    best_route_int.append(int(i))

print("La mejor ruta encontrada es: ", best_route_int)
print("La distancia total es: ", distance)
print("Tiempo tardado: ", fin - inicio)
