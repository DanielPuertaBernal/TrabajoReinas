import random

# Cada individuo es una lista de 8 números (columna de cada reina en cada fila)
def create_individual():
    return [random.randint(0, 7) for _ in range(8)]

def fitness(individual):
    attacks = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            # Dos reinas atacan si están en la misma columna o diagonal
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                attacks += 1
    return attacks

def crossover(parent1, parent2):
    cut = random.randint(1, 7)
    return parent1[:cut] + parent2[cut:]

def mutate(individual):
    idx = random.randint(0, 7)
    individual[idx] = random.randint(0, 7)

def genetic_algorithm():
    population = [create_individual() for _ in range(100)]
    generation = 0

    while True:
        population.sort(key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            return population[0]

        next_generation = population[:20]  # Elitismo: conservamos los mejores

        # Reproducir
        while len(next_generation) < 100:
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = crossover(parent1, parent2)
            if random.random() < 0.3:  # 30% de mutación
                mutate(child)
            next_generation.append(child)

        population = next_generation
        generation += 1
        if generation % 10 == 0:
            print(f"Generación {generation} - Mejor fitness: {fitness(population[0])}")

