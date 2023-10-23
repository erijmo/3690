import random

target = "110110001"

class GeneticAlgorithm:
    def __init__(self, pop_size, mutation_rate):
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.pop = self.init_pop()

    def init_pop(self):
        return [''.join(random.choice('01') for _ in range(len(target))) for _ in range(self.pop_size)]

    def calc_fit(self, individual):
        return sum(1 for a, b in zip(individual, target) if a == b)

    def select_parents(self):
        return random.choices(self.pop, k=2)

    def crossover(self, parent1, parent2):
        pivot = random.randint(1, len(parent1) - 1)
        return parent1[:pivot] + parent2[pivot:]

    def mutate(self, individual):
        return ''.join(
            '1' if random.random() < self.mutation_rate else bit
            for bit in individual
        )

    def run(self, generations):
        for generation in range(1, generations + 1):
            self.pop = sorted(self.pop, key=self.calc_fit, reverse=True)
            best_individual = self.pop[0]
            print(f"Generation {generation}: {best_individual}, Fitness: {self.calc_fit(best_individual)}")

            if best_individual == target:
                print("Target reached.")
                break

            new_pop = [best_individual]

            for _ in range(self.pop_size - 1):
                parent1, parent2 = self.select_parents()
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_pop.append(child)

            self.pop = new_pop


ga = GeneticAlgorithm(pop_size=100, mutation_rate=0.01)
ga.run(generations=100)