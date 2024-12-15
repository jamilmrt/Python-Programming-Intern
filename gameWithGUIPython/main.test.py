import pygame
import random
import time
import json
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 500  # Increased height for player info
CELL_SIZE = 100
GRID_SIZE = 4
TILE_COLORS = {
    0: (204, 192, 179),  # Empty cell
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    8: (243, 197, 116),  # Obstacle tile
    16: (243, 167, 86)
}
FONT_SIZE = 36

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

Running = True
clock = pygame.time.Clock()


class Game2048:
    def __init__(self, player_name, difficulty="easy"):
        self.player_name = player_name
        self.score = 0
        self.history = []  # List to store game states
        self.board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.difficulty = difficulty
        print(f"Initializing game for {player_name} with difficulty: {difficulty}")
        self.spawn_initial_tiles()

    def spawn_initial_tiles(self):
        print("Spawning initial tiles")
        if self.difficulty == "easy":
            self.spawn_new_tile()
            self.spawn_new_tile()
        elif self.difficulty == "medium":
            for _ in range(3):
                self.spawn_new_tile()
        elif self.difficulty == "hard":
            for _ in range(4):
                self.spawn_new_tile()
            self.spawn_obstacle()

    def spawn_new_tile(self):
        empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if self.board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = 2 if random.random() < 0.9 else 4
            print(f"Spawned tile {self.board[row][col]} at ({row}, {col})")

    def spawn_obstacle(self):
        empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if self.board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = 8 if random.random() < 0.5 else 16
            print(f"Spawned obstacle {self.board[row][col]} at ({row}, {col})")

    def undo_move(self):
        if len(self.history) > 0:
            prev_state = self.history.pop()
            self.board = [row[:] for row in prev_state["board"]]
            self.score = prev_state["score"]
            print("Move undone")
        else:
            print("No moves to undo")

    def move_tiles(self, direction):
        print(f"Moving tiles {direction}")
        self.history.append({"board": [row[:] for row in self.board], "score": self.score})

        if direction == 'left':
            for i in range(GRID_SIZE):
                self.slide_row_left(self.board[i])
        elif direction == 'right':
            for i in range(GRID_SIZE):
                self.slide_row_right(self.board[i])
        elif direction == 'up':
            for j in range(GRID_SIZE):
                self.slide_col_up(j)
        elif direction == 'down':
            for j in range(GRID_SIZE):
                self.slide_col_down(j)

        self.spawn_new_tile()

    def slide_row_left(self, row):
        new_row = [x for x in row if x != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                self.score += new_row[i]
                new_row[i + 1] = 0
        new_row = [x for x in new_row if x != 0]
        row[:len(new_row)] = new_row
        row[len(new_row):] = [0] * (GRID_SIZE - len(new_row))

    def slide_row_right(self, row):
        row.reverse()
        self.slide_row_left(row)
        row.reverse()

    def slide_col_up(self, col):
        col_values = [self.board[i][col] for i in range(GRID_SIZE)]
        self.slide_row_left(col_values)
        for i in range(GRID_SIZE):
            self.board[i][col] = col_values[i]

    def slide_col_down(self, col):
        col_values = [self.board[i][col] for i in range(GRID_SIZE)]
        col_values.reverse()
        self.slide_row_left(col_values)
        col_values.reverse()
        for i in range(GRID_SIZE):
            self.board[i][col] = col_values[i]

    def is_game_over(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i][j] == 0:
                    return False, ""
                if j < GRID_SIZE - 1 and self.board[i][j] == self.board[i][j + 1]:
                    return False, ""
                if i < GRID_SIZE - 1 and self.board[i][j] == self.board[i + 1][j]:
                    return False, ""
        print("Game over")
        return True, "Game Over!"

    def save_score(self):
        print("Saving score")
        try:
            with open('leaderboard.json', 'r') as f:
                scores = json.load(f)
        except FileNotFoundError:
            scores = []

        scores.append({"name": self.player_name, "score": self.score})
        scores.sort(key=lambda x: x["score"], reverse=True)
        scores = scores[:5]  # Keep only top 5 scores

        with open('leaderboard.json', 'a') as f:
            json.dump(scores, f)

    def display_leaderboard(self):
        try:
            with open('leaderboard.json', 'r') as f:
                scores = json.load(f)
        except FileNotFoundError:
            scores = []

        font = pygame.font.SysFont(None, 24)
        y = HEIGHT - 100
        for entry in scores:
            score_surface = font.render(f"{entry['name']}: {entry['score']}", True, (0, 0, 0))
            screen.blit(score_surface, (50, y))
            y += 30


# if __name__ == "__main__":


#     pygame.font.init()

#     # Create a GUI input window for name and difficulty
#     font = pygame.font.SysFont(None, 48)
#     input_box = pygame.Rect(50, 200, 300, 50)
#     color_inactive = pygame.Color('lightskyblue3')
#     color_active = pygame.Color('dodgerblue2')
#     color = color_inactive
#     active = False
#     text = ''
#     difficulty = 'easy'

#     while True:
#         screen.fill((255, 255, 255))
#         txt_surface = font.render("Enter your name:", True, (0, 255, 255))
#         game = Game2048(txt_surface)
#         screen.blit(txt_surface, (50, 150))
#         dif_surface = font.render(f"Difficulty: {difficulty} (E/M/H)", True, (0, 0, 0))
#         screen.blit(dif_surface, (50, 270))


#         pygame.draw.rect(screen, color, input_box, 2)
#         name_surface = font.render(text, True, (0, 0, 0))
#         screen.blit(name_surface, (input_box.x + 5, input_box.y + 5))

#         pygame.display.flip()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if input_box.collidepoint(event.pos):
#                     active = not active
#                 else:
#                     active = False
#                 color = color_active if active else color_inactive
#             if event.type == pygame.KEYDOWN:
#                 if active:
#                     if event.key == pygame.K_RETURN:
#                         if text: #check if name isn't empty
#                             game = Game2048(text, difficulty)
#                             name_entered = True
#                             break #exit the name input loop
#                     elif event.key == pygame.K_BACKSPACE:
#                         text = text[:-1]
#                     else:
#                         text += event.unicode
#             if event.type == pygame.KEYDOWN and not name_entered: #difficulty selection
#                 if event.key == pygame.K_e:
#                     difficulty = "easy"
#                 elif event.key == pygame.K_m:
#                     difficulty = "medium"
#                 elif event.key == pygame.K_h:
#                     difficulty = "hard"
#         # Handle game inputs and logic
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             game.move_tiles('left')
#         elif keys[pygame.K_RIGHT]:
#             game.move_tiles('right')
#         elif keys[pygame.K_UP]:
#             game.move_tiles('up')
#         elif keys[pygame.K_DOWN]:
#             game.move_tiles('down')
#         elif keys[pygame.K_u]:  # Undo move
#             game.undo_move()

#         # Check for game over
#         is_over, message = game.is_game_over()
#         if is_over:
#             font = pygame.font.SysFont(None, 72)
#             game_over_surface = font.render(message, True, (255, 0, 0))
#             screen.blit(game_over_surface, (50, HEIGHT // 2))
#             pygame.display.flip()
#             pygame.time.delay(3000)
#             game.save_score()
#             pygame.quit()
#             exit()

#         # Render the board
#         screen.fill((255, 255, 255))
#         for row in range(GRID_SIZE):
#             for col in range(GRID_SIZE):
#                 tile_value = game.board[row][col]
#                 tile_color = TILE_COLORS[tile_value]
#                 pygame.draw.rect(
#                     screen,
#                     tile_color,
#                     (col * CELL_SIZE + 10, row * CELL_SIZE + 10, CELL_SIZE - 20, CELL_SIZE - 20),
#                     border_radius=5
#                 )
#                 if tile_value != 0:
#                     text_surface = font.render(str(tile_value), True, (0, 0, 0))
#                     text_rect = text_surface.get_rect(center=(col * CELL_SIZE + 60, row * CELL_SIZE + 60))
#                     screen.blit(text_surface, text_rect)

#         # Display player info
#         info_font = pygame.font.SysFont(None, 36)
#         score_surface = info_font.render(f"Score: {game.score}", True, (0, 0, 0))
#         screen.blit(score_surface, (10, HEIGHT - 80))
#         player_surface = info_font.render(f"Player: {game.player_name}", True, (0, 0, 0))
#         screen.blit(player_surface, (10, HEIGHT - 50))

#         # Display leaderboard
#         game.display_leaderboard()

#         # Refresh the display
#         pygame.display.flip()
#         clock.tick(30)


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    font = pygame.font.SysFont(None, 48)
    input_box = pygame.Rect(50, 200, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    difficulty = "easy"

    name_entered = False
    game = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text:
                            game = Game2048(text, difficulty)
                            name_entered = True
                            break
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            if event.type == pygame.KEYDOWN and not name_entered:
                if event.key == pygame.K_e:
                    difficulty = "easy"
                elif event.key == pygame.K_m:
                    difficulty = "medium"
                elif event.key == pygame.K_h:
                    difficulty = "hard"
        if name_entered:
            break

        screen.fill((255, 255, 255))
        txt_surface = font.render("Enter your name:", True, (0, 0, 0))
        screen.blit(txt_surface, (50, 150))
        dif_surface = font.render(f"Difficulty: {difficulty}", True, (0, 0, 0))
        screen.blit(dif_surface, (50, 270))

        pygame.draw.rect(screen, color, input_box, 2)
        name_surface = font.render(text, True, (0, 0, 0))
        screen.blit(name_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.move_tiles('left')
        elif keys[pygame.K_RIGHT]:
            game.move_tiles('right')
        elif keys[pygame.K_UP]:
            game.move_tiles('up')
        elif keys[pygame.K_DOWN]:
            game.move_tiles('down')
        elif keys[pygame.K_u]:
            game.undo_move()

        is_over, message = game.is_game_over()
        if is_over:
            font = pygame.font.SysFont(None, 72)
            game_over_surface = font.render(message, True, (255, 0, 0))
            screen.blit(game_over_surface, (50, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(3000)
            game.save_score()
            pygame.quit()
            exit()

        screen.fill((255, 255, 255))
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                tile_value = game.board[row][col]
                tile_color = TILE_COLORS.get(tile_value, (0, 0, 0))  # added get to prevent key error
                pygame.draw.rect(
                    screen,
                    tile_color,
                    (col * CELL_SIZE + 10, row * CELL_SIZE + 10, CELL_SIZE - 20, CELL_SIZE - 20),
                    border_radius=5
                )
                if tile_value != 0:
                    text_surface = font.render(str(tile_value), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(col * CELL_SIZE + 60, row * CELL_SIZE + 60))
                    screen.blit(text_surface, text_rect)

        info_font = pygame.font.SysFont(None, 36)
        score_surface = info_font.render(f"Score: {game.score}", True, (0, 0, 0))
        screen.blit(score_surface, (10, HEIGHT - 80))
        player_surface = info_font.render(f"Player: {game.player_name}", True, (0, 0, 0))
        screen.blit(player_surface, (10, HEIGHT - 50))

        game.display_leaderboard()

        pygame.display.flip()
        clock.tick(30)