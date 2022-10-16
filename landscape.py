import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()
pygame.display.set_caption('Daniel Chen - Landscape Lab')

WIDTH = 800
HEIGHT = 250
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ----
# init

circle_sun_x = 400
circle_sun_y = 160

EVERGREEN = (5, 71, 42)
FOREST_GREEN = (34, 139, 34)
DARK_GREEN = (74, 139, 34)

y = 50
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


tree_x = 544
tree_y = 160

bush_1_x = 244
bush_1_y = 230

bush_2_x = 62
bush_2_y = 209

bush_3_x = 700
bush_3_y = 206

radious = 30
rect = 100
radious_bush = 25

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    circle_sun_x += 1.5
    circle_sun_y -= 1
    tree_x -= 2
    bush_1_x -= 2
    bush_2_x -= 2
    bush_3_x -= 2
    y += 1

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    # https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon

    # Sun
    SUNCOLOUR = (255, y, 0)
    pygame.draw.circle(screen, SUNCOLOUR, (circle_sun_x, circle_sun_y), 40)

    # Mountain
    pygame.draw.polygon(screen, 'darkgrey', ((0, 200), (50, 40), (100, 200)))
    pygame.draw.polygon(screen, 'darkgrey', ((100, 200), (250, 100), (300, 200)))
    pygame.draw.polygon(screen, 'darkgrey', ((200, 200), (250, 100), (300, 200)))
    pygame.draw.polygon(screen, 'darkgrey', ((300, 200), (350, 100), (400, 200)))
    pygame.draw.polygon(screen, 'darkgrey', ((400, 200), (450, 100), (500, 200)))
    pygame.draw.polygon(screen, 'darkgrey', ((500, 200), (550, 150), (600, 200)))
    pygame.draw.polygon(screen, 'darkgrey', ((600, 200), (650, 100), (700, 200)))
    pygame.draw.polygon(screen, 'darkgrey', ((700, 200), (750, 150), (800, 200)))

    #Green Land
    pygame.draw.rect(screen, 'lightgreen', (0, 200, 800, 50))

    # Tree
    pygame.draw.rect(screen, EVERGREEN, (tree_x, tree_y, 20, rect))  # trunk
    pygame.draw.circle(screen, FOREST_GREEN, (tree_x+9, tree_y), radious)  # leaves

    # Bush
    pygame.draw.circle(screen, DARK_GREEN, (bush_1_x, bush_1_y), radious_bush)
    pygame.draw.circle(screen, DARK_GREEN, (bush_1_x + 26, bush_1_y), radious_bush)
    pygame.draw.circle(screen, DARK_GREEN, (bush_1_x - 25, bush_1_y - 1), radious_bush)
    pygame.draw.circle(screen, DARK_GREEN, (bush_2_x, bush_2_y), radious_bush)
    pygame.draw.circle(screen, DARK_GREEN, (bush_2_x + 26, bush_2_y), radious_bush)
    pygame.draw.circle(screen, DARK_GREEN, (bush_2_x - 25, bush_2_y - 1), radious_bush)
    pygame.draw.circle(screen, DARK_GREEN, (bush_3_x, bush_3_y), radious_bush)
    pygame.draw.circle(screen, DARK_GREEN, (bush_3_x + 26, bush_3_y), radious_bush)
    pygame.draw.circle(screen, DARK_GREEN, (bush_3_x - 25, bush_3_y - 1), radious_bush)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
