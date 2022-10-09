import numpy as np
import random
from copy import deepcopy


class Organism:
    def __init__(self, architecture, genome, ID):
        self.arch = architecture
        if genome is None:
            first_genome = generate_first_genome(architecture)
            self.genome = first_genome
        else:
            self.genome = genome
        self.fitness = 0
        self.weights = transform(self.genome, architecture)
        self.ID = ID
        self.food = 0

    def __str__(self):
        return 'Organism ID: ' + str(self.ID)

    def mutate(self):
        if random.uniform(0.0, 1.0) <= 0.1:
            print('original genome:', self.genome)
            index = random.choice(range(len(self.genome)))
            print('index is:', index)
            self.genome[index] = np.random.randn()
            print('new genome:', self.genome)

    def forward_pass(self, X):
        weights = self.weights
        pass_num = len(self.arch) - 1
        for passes in range(pass_num):
            key = str(passes + 1) + '-' + str(passes + 2)
            if passes == 0:
                current_mat = X
            else:
                current_mat = A
            Theta = weights[key]

            Z = np.matmul(Theta.T, current_mat)
            A_no_bias = sigmoid(Z)
            if passes == pass_num - 1:
                break
            bias = np.ones((1, 1))
            A = np.append(bias, A_no_bias, axis=0)
        return A_no_bias


def sigmoid(z):
    return 1. / (1. + np.exp(-1. * z))

def generate_first_genome(architecture):
    size = 0
    for index in range(len(architecture)-1):
        current_layer_size = architecture[index]
        next_layer_size = architecture[index + 1]
        if index != len(architecture) - 1:
            current_layer_size += 1
        size += current_layer_size * next_layer_size

    first_genome = np.random.uniform(-0.5, 0.5, (1, size)).tolist()
    return first_genome[0]


def transform(genome, architecture):
    dna = deepcopy(genome)
    weights = {}
    for index in range(len(architecture) - 1):

        layer_number = index + 1;
        key = str(layer_number) + '-' + str(layer_number + 1)
        current_layer_size = architecture[index]
        next_layer_size = architecture[index + 1]
        if index != len(architecture) - 1:
            current_layer_size += 1
        size = current_layer_size * next_layer_size
        dimension = (current_layer_size, next_layer_size)
        chromosome = dna[0:size];
        del dna[0:size]
        weights[key] = np.array(chromosome).reshape(dimension)
    return weights

def mate(mate1, mate2):
    cut_index = random.choice(range(1, len(mate1.genome)))
    front_cut = mate1.genome[0:cut_index]
    back_cut = mate2.genome[cut_index:len(mate2.genome)]
    child_genome = front_cut + back_cut
    return child_genome







