dBar = "="*27
print(f"\n{dBar} Part 1 {dBar}\n")


import random
import numpy as np


def create_population(N, T, n=10):
    population = []
    for i in range(n):
        chromosome = ""
        for j in range(N*T):
            chromosome += str(random.randint(0, 1))
        population.append(chromosome)
    return population


def parent_selection(population):
    choice = list(range(len(population)))
    random.shuffle(choice)
    return choice


def fitnessTest(chromosome, N, T):
    chromosome_array = np.array(list(map(int, chromosome)))
    overlap = 0
    consist = np.zeros(N, dtype=int)

    for i in range(T):
        segment = chromosome_array[i*N:(i+1)*N]
        count = np.sum(segment)
        consist += segment
        overlap += abs(count - 1)

    consist = np.abs(consist - 1)
    return -(overlap + np.sum(consist))


def mutate_chromosome(chromosome, N, T):
    chromosome_list = list(chromosome)
    idx = random.randint(0, N*T-1)
    chromosome_list[idx] = '0' if chromosome_list[idx] == '1' else '1'
    return ''.join(chromosome_list)


def mutation(offsprings, N, T):
    if random.random() > 0.5:
        offsprings[0] = mutate_chromosome(offsprings[0], N, T)
    if random.random() > 0.5:
        offsprings[1] = mutate_chromosome(offsprings[1], N, T)
    return offsprings


def SP_crossover(p1, p2, N, T):
    i = random.randint(1, (N*T)-1)
    return p1[:i]+p2[i:], p2[:i]+p1[i:]


def GenAlg(population, N, T):
    n = len(population)
    selection = parent_selection(population)
    for i in range(0, n-1, 2):
        p1 = population[selection[i]]
        p2 = population[selection[i+1]]
        offsprings = mutation(list(SP_crossover(p1, p2, N, T)), N, T)
        population.extend(offsprings)
    fitnessSorted = [(fitnessTest(chromosome, N, T), chromosome)
                     for chromosome in population]
    fitnessSorted.sort(reverse=True)
    new_population = [chromosome[1] for chromosome in fitnessSorted[:n]]
    return new_population


infile = open("input.txt")

N, T = infile.readline().split()
N, T = int(N), int(T)
courses = []
for _ in range(N):
    courses.append(infile.readline().strip())

infile.close()

solutions = create_population(N, T)
MAX_ITER = 100
i = 0

while fitnessTest(solutions[0], N, T) != 0 and i < MAX_ITER:
    solutions = GenAlg(solutions, N, T)
    i += 1

if i == MAX_ITER:
    print("No optimal solution found within the iteration limit.")
else:
    print(f"Optimal solution found: ({solutions[0]}) with fitness {
          fitnessTest(solutions[0], N, T)} in {i} iterations")


print(f"\n{dBar} Part 2 {dBar}\n")


def TP_crossover(p1, p2, N, T):
    length = N*T
    i = random.randint(1, length - 2)
    j = random.randint(i + 1, length - 1)

    c1 = p1[:i] + p2[i:j] + p1[j:]
    c2 = p2[:i] + p1[i:j] + p2[j:]
    return c1, c2


population = create_population(N, T)

selection = parent_selection(population)

p1 = population[selection[0]]
p2 = population[selection[1]]

print("Parent 1:", p1)
print("Parent 2:", p2)

c1, c2 = TP_crossover(p1, p2, N, T)

print("-"*20)
print("Child 1:", c1)
print("Child 2:", c2)
