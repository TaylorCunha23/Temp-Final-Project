import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Set the window title
pygame.display.set_caption('Pygame Test')

# Fill the screen with black
screen.fill((0, 0, 0))

# Update the display
pygame.display.flip()

# Wait for the user to close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
