import os
import pygame
pygame.font.init()

# COLOR
RED = (255, 0, 0)
PINK = (255, 192, 203)
BLACK = (0, 0, 0)
L_GREEN = (35, 186, 123)
GREY = (115, 126, 133)
MAROON = (128, 0, 0)
BLUE = (24, 148, 156)
TEAL_BLUE = (77, 124, 138)
MORNING_BLUE = (127, 156, 150)


# Sizes
screen_size = (660, 660)
bot_size = (30, 30)

# FPS
FPS = 5

# Pics
BOT = pygame.transform.scale(pygame.image.load(os.path.join('pics', 'Test_bot2.png')), (60, 60))
FOOD = pygame.transform.scale(pygame.image.load(os.path.join('pics', 'Apple.gif')), (60, 60))
X = pygame.transform.scale(pygame.image.load(os.path.join('pics', 'X.png')), (60, 60))


# Velocity
VEL = 60

# Texts
FONT = pygame.font.SysFont('comicsans', 100)