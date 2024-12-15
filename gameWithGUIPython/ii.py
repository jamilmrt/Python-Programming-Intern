import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

# Set up the display
width, height = 400, 400
grid_size = 4
cell_size = width // grid_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2048")

# Create the game grid
grid = [[0] * grid_size for _ in range(grid_size)]

# Function to draw the grid and tiles
def draw_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            pygame.draw.rect(screen, grey, (j * cell_size, i * cell_size, cell_size, cell_size), 1)

def draw_tiles():
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] != 0:
                color = get_tile_color(grid[i][j])
                x = j * cell_size + cell_size // 2
                y = i * cell_size + cell_size // 2
                font = pygame.font.Font(None, 30)
                text = font.render(str(grid[i][j]), True, black)
                text_rect = text.get_rect(center=(x, y))
                pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
                screen.blit(text, text_rect)

def get_tile_color(value):
    colors = {
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
        2048: (237, 194, 46)
    }
    return colors.get(value, (204, 192, 179))  # Default color for higher values

# Function to add a new tile to the grid
def add_new_tile():
    empty_cells = []
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 0:
                empty_cells.append((i, j))

    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[row][col] = random.choice([2, 4])

# Function to move tiles (example: move tiles to the right)
def move_right():
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            if grid[i][j] != 0:
                row.append(grid[i][j])
        row = merge(row)
        row = row + [0] * (grid_size - len(row))
        for j in range(grid_size):
            grid[i][j] = row[j]

# Helper function to merge tiles (for right movement)
def merge(row):
    merged = []
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            merged.append(row[i] * 2)
            i += 1
        else:
            merged.append(row[i])
    if len(row) > 0 and len(merged) < len(row):
        merged.append(row[-1])
    return merged

# Function to check for game over
def game_over():
    # Check for empty cells
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 0:
                return False

    # Check for possible moves
    for i in range(grid_size):
        for j in range(grid_size - 1):
            if grid[i][j] == grid[i][j + 1]:
                return False
    for i in range(grid_size - 1):
        for j in range(grid_size):
            if grid[i][j] == grid[i + 1][j]:
                return False
    return True

# Main game loop
add_new_tile()
add_new_tile()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_LEFT:
                # Implement move_left() function
                pass
            elif event.key == pygame.K_UP:
                # Implement move_up() function
                pass
            elif event.key == pygame.K_DOWN:
                # Implement move_down() function
                pass

            if any(grid[i][j] == 2048 for i in range(grid_size) for j in range(grid_size)):
                print("You Win!")
                running = False

            if game_over():
                print("Game Over!")
                running = False

            add_new_tile()

    screen.fill(white)
    draw_grid()
    draw_tiles()
    pygame.display.update()

pygame.quit()