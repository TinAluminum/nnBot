import random as rd
from simulation import simulate, simulate_rl
from organism import Organism
import operator
import numpy as np
import time

def generate_simple_map(dimension): # Take in tuple
    map = np.ones((dimension))
    map[2:(dimension[0]-2), 2:(dimension[1]-2)] = 0.0 # make inside border value to 0.0
    return map

def generate_first_gen(population, arch, identification):
    generation = []
    for i in range(population):
        member = Organism(arch, None, identification)
        generation.append(member)
        identification += 1
    return generation, identification

def mate(mate1, mate2):
    cut_index = rd.choice(range(1, len(mate1.genome)))
    front_cut = mate1.genome[0:cut_index]
    back_cut = mate2.genome[cut_index:len(mate2.genome)]
    child_genome = front_cut + back_cut
    return child_genome

def mating(old_gen, count, arch, ID):
    mated_population = []
    for new_mem in range(count):
        mem1 = rd.choice(old_gen); mem2 = rd.choice(old_gen)
        child_genome = mate(mem1, mem2)
        child = Organism(arch, child_genome, ID)
        mated_population.append(child)
        ID += 1
    return mated_population, ID

def random_kil(gen, number, arch, ID):
    for kill in range(number):
        index = rd.randint(1, 90)
        gen.pop(index)
        gen.append(Organism(arch, None, ID))
        ID += 1
    return ID

def reset_fitness(members):
    for member in members:
        member.fitness = 0
        member.food = 0
    pass

def generate_new_generation(gen, pass_over_num, arch, ID):
    top_mem = gen[0:pass_over_num]
    reset_fitness(top_mem)
    mate_count = len(gen) - pass_over_num
    mated_poppulation, ID = mating(gen, mate_count, arch, ID)
    new_gen = top_mem + mated_poppulation
    return new_gen, ID

def genetic_algorithm(epoch, population, map, arch):
    ID = 1
    gen, ID = generate_first_gen(population, arch, ID)
    for run in range(epoch):
        simulate(gen, map, 50, [3, 3])
        #if run == 0:
            #[print(mem.fitness) for mem in gen]
        gen.sort(key = operator.attrgetter('fitness'), reverse=True)
        if run == 0:
            print('Best in first gen', gen[0].fitness)
        if run % 25 == 0 or run == epoch-1:
            print('Best in gen', str(run), 'is Member:',  gen[0].ID, 'Score:', gen[0].fitness)
            print('Top 10 in Gen:')
            [print(mem.fitness) for mem in gen[0:10]]
            print('-------------')
        if gen[0].food == 2:
            print('----------- FOOD More than 2 ----------')
            break
        if run != epoch-1:
            new_gen, ID = generate_new_generation(gen, 10, arch, ID)
            ID = random_kil(new_gen, 10, arch, ID)
            gen = new_gen

    print('done')
    gen.sort(key=operator.attrgetter('fitness'), reverse=True)
    best = gen[0]
    print('Best fitness:', best.ID)
    best.fitness = 0
    return best

start_time = time.time()
map = generate_simple_map((12, 12))
print(map)
bot = genetic_algorithm(1000, 100, map, [12, 18, 17, 4])
simulate_rl([bot], map, 50, [2, 2])
print("--- %s seconds ---" % (time.time() - start_time))