## Building the game 2048 using python gui pyGame

import pygame
import random
import sys

pygame.init()

# Initial set up
<<<<<<< HEAD
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('2048')
=======
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode(400, 500)
pygame.displayset_caption('2048')
>>>>>>> origin/main
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)

## 2048 Game color library
colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 288),
          8: (242, 127, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)
          }

# game variable initialize
<<<<<<< HEAD
board_values = [[2 for _ in range(4)] for _ in range(4)]

## Draw background for the board


def draw_board():
    pygame.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)

def draw_pieces(board):
board_values = [[0 for _ in range(4)] for _ in range(4) ]

## Draw background for the board
def draw_board():
    pygame.draw.rect(screen, colors['bg'], (200, 200,), int[0, 0, 400, 400], 0, 10)


def draw_pieces(board_values, board=None):
>>>>>>> origin/main
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
<<<<<<< HEAD
                value_color = colors['light text']
            else:
                value_colors = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95, 57))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
=======
                value_colors = colors['light text']
            else:
                value_colors = colors['dark text']
            if value <= 2048:
                clor = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
>>>>>>> origin/main


# main game Loop
run = True
while run:
    timer.tick(fps)
<<<<<<< HEAD
    screen.fill((169, 169, 169))
=======
    screen.fill('gray')
>>>>>>> origin/main
    draw_board()
    draw_pieces(board_values)

    # spawn()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
