import numpy as np
import pygame

# Set colors
BG_COLOR = (50, 50, 50)
GRID_COLOR = (0, 0, 0)
DIE_COLOR = (219, 112, 147)
ALIVE_COLOR = (255, 255, 255)

# Define a glider pattern as an example
def glider_pattern():
    pattern = np.zeros((20, 20))
    pattern[1, 2] = 1
    pattern[2, 3] = 1
    pattern[3, 1:4] = 1
    return pattern

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros(cells.shape)
    
    for row, col in np.ndindex(cells.shape):
        alive_cells = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = BG_COLOR if cells[row, col] == 0 else ALIVE_COLOR
        
        if cells[row, col] == 1:
            if alive_cells < 2 or alive_cells > 3:
                if with_progress:
                    color = DIE_COLOR
            elif 2 <= alive_cells <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = ALIVE_COLOR
        else:
            if alive_cells == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = ALIVE_COLOR

        pygame.draw.rect(screen, color, 
                         (col * size, row * size, size - 1, size - 1))
        
    return updated_cells

def main():
    # Get grid dimensions from user
    HEIGHT = int(input("Please input the height of the grid: "))
    WIDTH = int(input("Please input the width of the grid: "))
    #HEIGHT=300
    #WIDTH=300
    pygame.init()
    size = 10
    
    # Randomly initialize cells
    cells = np.random.randint(0, 2, size=(HEIGHT // size, WIDTH // size))

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    screen.fill(GRID_COLOR)
    update(screen, cells, size)
    pygame.display.flip()

    running = False
    step = False
    clock = pygame.time.Clock()
    speed = 10  # Set a reasonable speed for the continuous simulation

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                elif event.key == pygame.K_r:
                    cells = np.random.randint(0, 2, size=(HEIGHT // size, WIDTH // size))
                    update(screen, cells, size)
                    pygame.display.update()
                elif event.key == pygame.K_c:
                    cells = np.zeros((HEIGHT // size, WIDTH // size))
                    update(screen, cells, size)
                    pygame.display.update()
                elif event.key == pygame.K_n:
                    step = True
                elif event.key == pygame.K_p:
                    pattern = glider_pattern()
                    cells[:pattern.shape[0], :pattern.shape[1]] = pattern
                    update(screen, cells, size)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                cells[position[1] // size, position[0] // size] = 1 - cells[position[1] // size, position[0] // size]
                update(screen, cells, size)
                pygame.display.update()
    
        if running or step:
            cells = update(screen, cells, size, with_progress=True)
            pygame.display.update()
            step = False
            clock.tick(speed)  # Control the speed of the simulation

if __name__ == "__main__":
    main()


