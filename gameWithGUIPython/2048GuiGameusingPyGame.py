import pygame
import random


# Pygame Initialization
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE

# Colors and Fonts
COLORS = {
    0: (205, 193, 180), 2: (238, 228, 218), 4: (237, 224, 200),
    8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
    64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 204, 97),
    512: (237, 200, 80), 1024: (237, 197, 63), 2048: (237, 194, 46)
}
FONT = pygame.font.Font(None, 50)
BIG_FONT = pygame.font.Font(None, 70)

# Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 Game")


def initialize_board():
    """Initialize the 4x4 grid with two random tiles."""
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_random_tile(board)
    add_random_tile(board)
    return board


def add_random_tile(board):
    """Add a random tile (2 or 4) to an empty position."""
    empty_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = random.choice([2, 4])


def slide_row(row):
    """Slide tiles to the left and merge."""
    new_row = [tile for tile in row if tile != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [tile for tile in new_row if tile != 0]
    return new_row + [0] * (GRID_SIZE - len(new_row))


def move_left(board):
    """Slide all rows left."""
    for r in range(GRID_SIZE):
        board[r] = slide_row(board[r])


def transpose(board):
    """Transpose the board for vertical moves."""
    return [list(row) for row in zip(*board)]


def move_up(board):
    """Slide tiles up."""
    board = transpose(board)
    move_left(board)
    board = transpose(board)


def move_down(board):
    """Slide tiles down."""
    board = transpose(board)
    move_left(board[::-1])
    board = transpose(board[::-1])


def move_right(board):
    """Slide all rows to the right."""
    for r in range(GRID_SIZE):
        board[r] = slide_row(board[r][::-1])[::-1]


def is_game_over(board):
    """Check if there are no valid moves left."""
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == 0: return False
            if r > 0 and board[r][c] == board[r - 1][c]: return False
            if c > 0 and board[r][c] == board[r][c - 1]: return False
    return True


def draw_board(board, score):
    """Draw the grid and tiles."""
    screen.fill((187, 173, 160))  # Background color
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = board[r][c]
            color = COLORS.get(value, (60, 58, 50))
            pygame.draw.rect(screen, color, (c * TILE_SIZE, r * TILE_SIZE + 100, TILE_SIZE, TILE_SIZE), border_radius=8)
            if value:
                text = FONT.render(str(value), True, (0, 0, 0) if value < 128 else (255, 255, 255))
                text_rect = text.get_rect(center=(c * TILE_SIZE + TILE_SIZE // 2, r * TILE_SIZE + TILE_SIZE // 2 + 100))
                screen.blit(text, text_rect)

    # Draw score
    pygame.draw.rect(screen, (119, 110, 101), (0, 0, WIDTH, 100))
    score_text = BIG_FONT.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))


def calculate_score(board):
    """Calculate the current score."""
    return sum(sum(row) for row in board)


def save_score(score):
    """Save the score to a leaderboard file."""
    with open("leaderboard.txt", "a") as file:
        file.write(str(score) + "\n")


def get_leaderboard():
    """Read and display the leaderboard."""
    try:
        with open("leaderboard.txt", "r") as file:
            scores = [int(line.strip()) for line in file.readlines()]
            return sorted(scores, reverse=True)[:5]
    except FileNotFoundError:
        return []


undo_stack = []


def save_state(board):
    """Save the current state of the board."""
    undo_stack.append([row[:] for row in board])


def undo_move(board):
    """Revert to the previous state."""
    if undo_stack:
        return undo_stack.pop()
    return board


def animate_movement(board, movements):
    """Animate the movement of tiles based on their positions."""
    frames = 10  # Number of animation frames
    for frame in range(frames):
        screen.fill((187, 173, 160))  # Background color

        for (start_pos, end_pos, value) in movements:
            start_x, start_y = start_pos
            end_x, end_y = end_pos
            current_x = start_x + (end_x - start_x) * frame / frames
            current_y = start_y + (end_y - start_y) * frame / frames
            pygame.draw.rect(
                screen,
                COLORS.get(value, (60, 58, 50)),
                (current_x * TILE_SIZE, current_y * TILE_SIZE + 100, TILE_SIZE, TILE_SIZE),
                border_radius=8
            )
            # Draw tile value
            if value:
                text = FONT.render(str(value), True, (0, 0, 0) if value < 128 else (255, 255, 255))
                text_rect = text.get_rect(
                    center=(current_x * TILE_SIZE + TILE_SIZE // 2, current_y * TILE_SIZE + TILE_SIZE // 2 + 100)
                )
                screen.blit(text, text_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Limit frame rate


def main():
    board = initialize_board()
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                save_state(board)
                if event.key == pygame.K_LEFT: move_left(board)
                if event.key == pygame.K_RIGHT: move_right(board)
                if event.key == pygame.K_UP: move_up(board)
                if event.key == pygame.K_DOWN: move_down(board)
                if event.key == pygame.K_u: board = undo_move(board)
                add_random_tile(board)
                score = calculate_score(board)

        draw_board(board, score)
        pygame.display.flip()

        if is_game_over(board):
            print("Game Over!")
            save_score(score)
            running = False

    pygame.quit()


if __name__ == "__main__":
    main()
