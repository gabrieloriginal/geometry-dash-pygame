import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1100, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash Pygame")

clock = pygame.time.Clock()

#i am dumb because idk my email :(


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34,139,34)
spike_speed = 1
player_pos = [200, 450]
spike_pos = [1050, 450]
ground_height = 150
gravity = -10


# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Espacio presionado")

        
    # Update player position
    player_pos[1] -= 1
    if player_pos[1] < 115:
        player_pos[1] = 450       

    # Move obstacle
    spike_pos[0] -=  1
    if spike_pos[0] < -50:
        spike_pos[0] = WIDTH


    # Collision detection
        

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK,(player_pos[0],player_pos[1],100,100))
    pygame.draw.rect(screen, GREEN,(spike_pos[0],spike_pos[1],50,100))
    pygame.display.flip()

    clock.tick(225)