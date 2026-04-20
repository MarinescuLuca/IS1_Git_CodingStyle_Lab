import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for the grid and display
GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)
REGENERATION_INTERVAL = 5000  # 5 seconds in milliseconds

def generate_color_grid():
    """
    Generates a 10x10 grid of random RGB colors.

    Returns:
        list: A 2D list where each element is a tuple representing an RGB color.
    """
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
             for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Set up the display
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate or wait 5 seconds)")

# Generate initial color data
color_data = generate_color_grid()

# Track the last regeneration time
last_regeneration_time = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the color grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = color_data[row][col]
            rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

    # Update the display
    pygame.display.flip()

    # Check for automatic regeneration every 5 seconds
    current_time = pygame.time.get_ticks()
    if current_time - last_regeneration_time > REGENERATION_INTERVAL:
        color_data = generate_color_grid()
        last_regeneration_time = current_time

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Manual regeneration on SPACE key press
            color_data = generate_color_grid()
            last_regeneration_time = current_time

# Quit Pygame
pygame.quit()