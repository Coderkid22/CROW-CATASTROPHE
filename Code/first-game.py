import sys
import os

stdout = sys.stdout  # save original stdout
sys.stdout = open(os.devnull, 'w')  # redirect stdout to null
import pygame  # pygame will not be able to print to stdout now
sys.stdout = stdout  # reset stdout back to original




# rest of your code
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800
pygame.init()



def main(WIDTH, HEIGHT):
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font1 = pygame.font.Font('font(s)/KarmaSuture.otf', 50)
    font2 = pygame.font.Font('font(s)/KarmaFuture.otf', 50)
    player_gravity = 0
    run_whileLoop = True
    run_game = True   
    jumpHeight = -21
    gameOver = False

    def display_image(sprite, spriteRectangle):
        WINDOW.blit(sprite, spriteRectangle)

    def image(variableName, imageRelativePath, convertAlpha):
        if convertAlpha:
            variableName = pygame.image.load(imageRelativePath).convert_alpha()
        elif convertAlpha is False:
            variableName = pygame.image.load(imageRelativePath).convert()
        else:
            variableName = pygame.image.load(imageRelativePath)
        
    def surfaces():
        image(runningGame_background, 'images/Sky.png', False)
        image(ground, 'images/ground.png', False)
        topOfGround = HEIGHT - ground.get_size()[1]

        scoreSuture = font1.render('SCORE', False, (64, 64, 64))
        scoreFuture = font2.render('SCORE', False, 'Black')
        scoreRectangle = scoreSuture.get_rect(center = (400, 75))

        image(retry_button, 'images/gameState_assets/retry_button.png', True)
        new_retry_button = 1
        retry_buttonRectangle = retry_button.get_rect(center = (400, 150))

        image(start_button, 'images\gameState_assets\start_button.png', True)
        start_buttonRectangle = start_button.get_rect(center = (400,400))

        image(lizard, 'images/lizard/lizard (1).png', True)
        new_lizard = pygame.transform.smoothscale(lizard, (99, 100))
        lizardRectangle = new_lizard.get_rect(midbottom = (704, 681))
        lizardRectangle.width = 60
        lizardRectangle.height = 1

        image(player, 'images/player/player_walk_1.png', True)
        new_player = pygame.transform.smoothscale(player, (90, 120))
        playerRectangle = player.get_rect(midbottom = (80, topOfGround))
        playerRectangle.width = 90
        playerRectangle.height = 120

        variables = {name: value for name, value in locals().items() if not name.startswith('__')}

        return variables
    
    variables = surfaces()


   

    while run_whileLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_whileLoop, run_game = False, False

            if run_game: 
                if event.type == pygame.MOUSEBUTTONDOWN and variables['playerRectangle'].bottom == variables['topOfGround']:
                    if variables['playerRectangle'].collidepoint(event.pos) or pygame.MOUSEBUTTONDOWN:
                        player_gravity = jumpHeight

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or pygame.K_UP or pygame.K_w:
                        if variables['playerRectangle'].bottom == variables['topOfGround']:
                            player_gravity = jumpHeight
            elif gameOver:
                mouse_position = pygame.mouse.get_pos()
                if variables['retry_buttonRectangle'].collidepoint(mouse_position) and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.time.wait(1000)
                    run_game = True
                    variables['lizardRectangle'].left = 850
                    variables['playerRectangle'].midbottom = (variables['playerRectangle'].midbottom[0], variables['topOfGround'])

        if run_game:
            display_image(variables['runningGame_background'], (0, 0))
            display_image(variables['ground'], (0, variables['topOfGround'] ))

            pygame.draw.rect(WINDOW, '#F0B27A', variables['scoreRectangle'], 30, 15)
            display_image(variables['scoreSuture'], variables['scoreRectangle'])

            variables['lizardRectangle'].x += -5

            if variables['lizardRectangle'].right <= 0:
                variables['lizardRectangle'].left = 850

            display_image(variables['new_lizard'], variables['lizardRectangle'])

            player_gravity += 0.9
            variables['playerRectangle'] .y += player_gravity
            if variables['playerRectangle'].bottom >= variables['topOfGround']:
                variables['playerRectangle'].bottom = variables['topOfGround']  
            display_image(variables['new_player'], variables['playerRectangle'])

            if variables['lizardRectangle'].colliderect(variables['playerRectangle']):                        
                run_game = False
                gameOver = True
        elif gameOver:
            display_image(variables['retry_button'], variables['retry_buttonRectangle'])
            display_image(va)
            # display_image(variables['start_button'], variables['start_buttonRectangle'])
            
        

            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_SPACE]:
            #     print('LES JUMP')
            
            # if variables['playerRectangle'] .colliderect(variables['lizardRectangle'] ):
            #     pass
            # mousePositon = pygame.mouse.get_pos()
            # if variables['playerRectangle'] .collidepoint(mousepos):
            #     pass
        pygame.display.update()
        clock.tick(60)

main(WINDOW_WIDTH, WINDOW_HEIGHT)