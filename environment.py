import numpy as np
from organism import Organism

def inp_layer_init(current_coor, surrounding, food_loc, turns, max_turns, map): #len =  13
    input_layer = np.ones((1, 1))
    map_len = map.shape[0] - 4
    food_x = (food_loc[0]-current_coor[0])/map_len; food_y = (food_loc[1]-current_coor[1])/map_len
    turns_percentage = turns / max_turns
    food_info_and_turns = np.array([food_x, food_y, turns]).reshape(3, 1)
    input_layer = np.concatenate((input_layer, surrounding), axis=0)
    input_layer = np.concatenate((input_layer, food_info_and_turns), axis=0)
    return input_layer

def fitness(member, food_got, path_history):
    assert isinstance(member, Organism)
    if food_got is True:
        member.fitness += 1
    if len(path_history) > 2:
        if path_history[-1] == path_history[-2]:
            member.fitness -= 0.005
    member.fitness += 0.01
