import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 800
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the image
image = pygame.image.load('images\gameState_assets\gameOver_text.png')
#new_image = pygame.transform.scale(image, , height)
image_rect = image.get_rect(center=(WIDTH//2, HEIGHT//2))

# Set the initial angle and rotation direction
angle = 0
rotateSpeed = 1

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

timer = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Adjust the angle
    angle = math.cos(timer) * 5  # Adjust this value to change the speed of rotation
    timer += 0.045
    # Rotate the image only if the angle has changed

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    screen.blit(rotated_image, rotated_rect)
    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
