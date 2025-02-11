import random

#Inicializacion de abejas con valores de (x,y), y la seleccion de la mejor solucion (abeja)
def initialize(n_employed, inicio, fin):
    employed_bees = [(random.uniform(inicio, fin), random.uniform(inicio, fin)) for _ in range(n_employed)]
    employed_values = [objective_function(x, y) for x, y in employed_bees]
    best_solution = min(employed_values)
    best_position = employed_bees[employed_values.index(best_solution)]
    return employed_bees, employed_values, best_solution, best_position

#Funcion a optimizar
def objective_function(x, y):
    f = (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2
    return f

#Busqueda de mejores soluciones alrededor de una abeja
def new_food_pos_cand(employed_bees, employed_values, i, best_position):
    x, y = employed_bees[i]
    phi = random.uniform(-1, 1)
    new_x = x + phi * (x - best_position[0])
    new_y = y + phi * (y - best_position[1])
    new_value = objective_function(new_x, new_y)

    if new_value < employed_values[i]:
        employed_bees[i] = (new_x, new_y)
        employed_values[i] = new_value

#Abejas empleadas buscando nuevas soluciones a su alrededor
def employed_bee_phase(employed_bees, employed_values, best_position):
    for i in range(len(employed_bees)):
        new_food_pos_cand(employed_bees, employed_values, i, best_position)

#Abejas observadoras y la probabilidad de encontrar otra solucion
def onlooker_bee_phase(employed_bees, employed_values, best_position, n_onlookers):
    total_values = sum(employed_values)
    probabilities = [value / total_values for value in employed_values]

    for _ in range(n_onlookers):
        i = select_bee(probabilities)
        new_food_pos_cand(employed_bees, employed_values, i, best_position)

#Funcion para seleccionar una abeja como observadora
def select_bee(probabilities):
    r = random.uniform(0, 1)
    cumulative_prob = 0
    for i, prob in enumerate(probabilities):
        cumulative_prob += prob
        if cumulative_prob >= r:
            return i

#Abejas exploradoras: cambian su valor cuando estan muy lejos de la solucion
def scout_bee_phase(employed_bees, employed_values, limit, inicio, fin):
    for i in range(len(employed_bees)):
        if employed_values[i] > limit:
            employed_bees[i] = (random.uniform(inicio, fin), random.uniform(inicio, fin))
            x, y = employed_bees[i]
            employed_values[i] = objective_function(x,y)

#Algortimo de optimizacion
def optimize(n_employed, n_onlookers, limit, num_iterations, inicio, fin):
    employed_bees, employed_values, best_solution, best_position = initialize(n_employed, inicio, fin)

    for _ in range(num_iterations):
        employed_bee_phase(employed_bees, employed_values, best_position)
        onlooker_bee_phase(employed_bees, employed_values, best_position, n_onlookers)
        scout_bee_phase(employed_bees, employed_values, limit, inicio, fin)

        current_best = min(employed_values)
        if current_best < best_solution:
            best_solution = current_best
            best_position = employed_bees[employed_values.index(current_best)]

    return best_position, best_solution

# Datos
inicio = -4.5
fin = 4.5
employedBees = 100
onlookersBees = 100
limit = 10
num_iterations = 100

best_position, best_solution = optimize(employedBees, onlookersBees, limit, num_iterations, inicio, fin)

print("Mejor solución para X: ", best_position[0])
print("Mejor solución para Y: ", best_position[1])
print("Valor de la función: ", best_solution)