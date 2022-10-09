import pygame
import numpy as np
import constants as const
from time import sleep
import random as rd


WIN = pygame.display.set_mode(const.screen_size)
w, h = pygame.display.get_surface().get_size()


def coordinate(pixel):
    return (pixel[0] / 60, pixel[1] / 60)

def draw_line(h, color):
    space = h // 11
    for i in range(1, 11):
        pygame.draw.line(WIN, color, (space, i * space), (h-space, i * space), 1)
        for j in range(1, 11):
            pygame.draw.line(WIN, color, (j * space, space), (j * space, h-space), 1)

def check_bot_position(bot, food): # returns (collision?, food get?)
    bot_coor = coordinate((bot.x, bot.y))
    food_coor = coordinate((food.x, food.y))
    ground = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    truth_value = [False, False]
    if bot_coor[0] not in ground or bot_coor[1] not in ground:
        truth_value[0] = True
    if bot_coor == food_coor:
        truth_value[1] = True
        food.x, food.y = rd.randint(1, 9)*60, rd.randint(1, 9)*60
    return truth_value

def draw_window(bot, food):
    background_color = const.TEAL_BLUE
    WIN.fill(background_color)
    pygame.draw.rect(WIN, const.MORNING_BLUE, pygame.Rect(60, 60, 540, 540))
    draw_line(h, const.BLACK)
    WIN.blit(const.BOT, (bot.x, bot.y))
    WIN.blit(const.FOOD, (food.x, food.y))
    #pygame.draw.line(WIN, const.RED, (50, 0), (50, 660), 3)

def bot_handle_movement(keys_pressed, bot):
    if keys_pressed[pygame.K_a]:  # LEFT
        bot.x -= const.VEL
    if keys_pressed[pygame.K_d]:  # RIGHT
        bot.x += const.VEL
    if keys_pressed[pygame.K_w]:  # UP
        bot.y -= const.VEL
    if keys_pressed[pygame.K_s]:  # DOWN
        bot.y += const.VEL

def update_game_state(collision, food_got, scores, bot, food):
    if collision is True:
        # WIN.blit(const.DEATH, (bot.x, bot.y))
        # text = "Bot ded"
        # draw_text = const.FONT.render(text, 1, const.BLACK)
        # WIN.blit(draw_text, (100, 330))
        WIN.blit(const.X, (bot.x, bot.y))
        pygame.display.update()
        bot.x, bot.y = 60, 60
        food.x, food.y = 540, 540
        pygame.time.delay(3000)
    if food_got is True:
        scores['food_score'] += 1
        print(scores['food_score'])

def bot_manual_brain(bot, food, turns):
    x_dis = bot.x - food.x; y_dis = bot.y - food.y
    if x_dis > 0:
        bot.x -= 60
    elif y_dis < 0:
        bot.y += 60
    elif x_dis < 0:
        bot.x += 60
    elif y_dis > 0:
        bot.y -= 60

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('GA Bot')
    run = True
    bot = pygame.Rect(60, 60, 60, 60)
    food = pygame.Rect(540, 540, 60, 60)
    scores = {
        'food_score': 0
    }
    turns = 0
    while run:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        bot_handle_movement(keys_pressed, bot)
        bot_manual_brain(bot, food, turns)
        draw_window(bot, food)
        collision, food_got = check_bot_position(bot, food)
        update_game_state(collision, food_got, scores, bot, food)
        pygame.display.update()
        turns += 1


main()