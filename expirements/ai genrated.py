a
import pygame.freetype

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
sum = '38329y32846' + 'ea28332sfs'
print(sum)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load a font
font = pygame.freetype.SysFont("arial", 24)

# Render the text to a surface
surface, rect = font.render("Hello World!", WHITE)

# Rotate the surface

import math
timer = 0
angle = 1

# Main loop
running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

   # Clear the screen
    screen.fill((0, 0, 0))

  
    angle = math.sin(timer) * 5
    timer += 0.001
    rotated_surface = pygame.transform.rotate(surface, angle)
   # Blit the rotated surface onto the screen
    screen.blit(rotated_surface, (WIDTH // 2, HEIGHT // 2))

   # Update the display
    pygame.display.flip()

pygame.quit()