import pygame
import sys
import math


# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 800
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# Load the image
image = pygame.image.load('images\gameState_assets\gameOver_text.png')
imageWidth, imageHeight = image.get_size()
aspectRatioOfImage =  imageWidth / imageHeight

newHeightOfImage = 80
newWidthOfImage = int(newHeightOfImage * aspectRatioOfImage)
print(newWidthOfImage, newHeightOfImage )

new_image = pygame.transform.smoothscale(image, (newWidthOfImage, newHeightOfImage))
image_rect = image.get_rect(center=(WIDTH//2, HEIGHT//3.5))

# Set the initial angle and rotation direction
angle = 0
rotateSpeed = 1

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

timer = 0
Run = True
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False


    # Clear the screen
    WINDOW.fill((0, 84, 0))

    # Adjust the angle
    angle = math.sin(timer) * 3.5  # Adjust this value to change the speed of rotation
    timer += 0.043
    # Rotate the image only if the angle has changed

    rotated_image = pygame.transform.rotate(new_image, angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    WINDOW.blit(rotated_image, rotated_rect)
    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
print(image.get_size())