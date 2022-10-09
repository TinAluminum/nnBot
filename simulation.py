import copy
import environment
import numpy as np
from organism import Organism
from copy import deepcopy
from time import sleep
import math
import random as rd

def read_surrounding(coordinate, map):
    x = coordinate[1]; y = coordinate[0]
    coordinate_chunk = map[(x-1):(x+2), (y-1):(y+2)]
    length = coordinate_chunk.size
    flatten_chunk = coordinate_chunk.reshape(length, 1)

    return flatten_chunk

def cap(hypothesis): # read output layer ad return index of max value
    max = hypothesis.max(axis=0)
    max_index = np.where(hypothesis==max)[0][0]
    return max_index

def moves(coordinate, dicision):
    if dicision == 0: # LEFT
        coordinate[0] -= 1
    elif dicision == 1: # RIGHT
        coordinate[0] += 1
    elif dicision == 2: # UP
        coordinate[1] -= 1
    elif dicision == 3: # DOWN
        coordinate[1] += 1

def check_collision(coordinate, map):
    x = coordinate[0]; y = coordinate[1]
    if map[x, y] == 1.0:
        return True
    else:
        return False

def check_game_state(coor, food_loc, map):
    if coor == food_loc:
        # food_loc = [rd.randint(2, map.shape[0]-3), rd.randint(2, map.shape[1]-3)]
        if food_loc == [7, 7]:
            food_loc = [2, 2]
        else:
            food_loc = [7, 7]
        return True, food_loc
    else:
        return False, food_loc

def simulate(generation, map, max_turns, start_coor):
    for member in generation:
        food_taken = 1
        coordinate = deepcopy(start_coor)
        path_history = [coordinate]
        food_loc = [7, 7]
        assert isinstance(member, Organism)
        turn = 1
        while turn <= max_turns:
            surrounding = read_surrounding(coordinate, map)
            # INPUT INPUTLAYER HERE
            input_layer = environment.inp_layer_init(coordinate, surrounding, food_loc, turn, max_turns, map)
            #  ---------------------
            dicision = member.forward_pass(input_layer)
            dicision = cap(dicision)
            moves(coordinate, dicision)
            new_surrounding = read_surrounding(coordinate, map)
            collision = check_collision(coordinate, map)
            if collision is True:
                member.fitness -= 0.9
                turns_used = max_turns - (turn + 1)
                break
            path_history.append(coordinate)
            food_got, food_loc = check_game_state(coordinate, food_loc, map)
            # FITNESS FUNCTION
            environment.fitness(member, food_got, path_history)
            turn += 1


def simulate_rl(generation, map, max_turns, start_coor):
    for member in generation:
        coordinate = deepcopy(start_coor)
        path_history = [coordinate]
        food_loc = [7, 7]
        assert isinstance(member, Organism)
        turn = 1
        while turn <= max_turns:
            print(coordinate)
            surrounding = read_surrounding(coordinate, map)
            # INPUT INPUTLAYER HERE
            input_layer = environment.inp_layer_init(coordinate, surrounding, food_loc, turn, max_turns, map)
            #  -----------------------
            dicision = member.forward_pass(input_layer)
            dicision = cap(dicision)
            moves(coordinate, dicision)
            new_surrounding = read_surrounding(coordinate, map)
            collision = check_collision(coordinate, map)
            if collision is True:
                member.fitness -= 1
                turns_used = max_turns - (turn + 1)
                print('DEAD')
                print(member.fitness)
                break
            path_history.append(coordinate)
            food_got, food_loc = check_game_state(coordinate, food_loc, map)
            if food_got is True:
                print('FOOD GET at', food_loc)
            # FITNESS FUNCTION
            environment.fitness(member, food_got, path_history)
            turn += 1
            sleep(0.5)
