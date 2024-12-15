## Building the game 2048 using python gui pyGame

import pygame
import random
import sys

pygame.init()

# Initial set up
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode(400, 500)
pygame.displayset_caption('2048')
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
board_values = [[0 for _ in range(4)] for _ in range(4) ]

## Draw background for the board
def draw_board():
    pygame.draw.rect(screen, colors['bg'], (200, 200,), int[0, 0, 400, 400], 0, 10)


def draw_pieces(board_values, board=None):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_colors = colors['light text']
            else:
                value_colors = colors['dark text']
            if value <= 2048:
                clor = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)


# main game Loop
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces(board_values)

    # spawn()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
