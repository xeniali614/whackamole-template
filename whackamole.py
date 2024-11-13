import pygame
import random

pygame.init()
GRID_WIDTH=20
GRID_HEIGHT=16
SQUARE_SIZE=32
SCREEN_WIDTH=GRID_WIDTH*SQUARE_SIZE
SCREEN_HEIGHT=GRID_HEIGHT*SQUARE_SIZE

def draw_grid(screen):
    for i in range(1,SCREEN_WIDTH,SQUARE_SIZE):
        pygame.draw.line(screen,
    (0,0,0),
    (i,0),
    (i,SCREEN_HEIGHT)
    )
    for i in range(1,SCREEN_HEIGHT,SQUARE_SIZE):
        pygame.draw.line(screen,
    (0,0,0),
    (0,i),
    (SCREEN_WIDTH,i)
    )

def handle_click(mouse_pos, mole_pos):
    grid_x = mouse_pos[0] // SQUARE_SIZE
    grid_y = mouse_pos[1] // SQUARE_SIZE


    if grid_x == mole_pos[0] and grid_y == mole_pos[1]:
        new_x = random.randrange(0, GRID_WIDTH)
        new_y = random.randrange(0, GRID_HEIGHT)
        return (new_x, new_y)
    return mole_pos

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_pos=(0,0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type== pygame.MOUSEBUTTONDOWN:
                    mole_pos= handle_click(event.pos,mole_pos)
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image,mole_image.get_rect(topleft=(mole_pos[0]*SQUARE_SIZE,mole_pos[1]*SQUARE_SIZE)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
