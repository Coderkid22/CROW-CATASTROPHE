import sys
import os
import math

stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')
import pygame
sys.stdout = stdout
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800
pygame.init()

def main(WIDTH, HEIGHT):
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT),  pygame.RESIZABLE)
    JUMPHEIGHT = -21
    FPS = 60
    clock = pygame.time.Clock()
    fontFuture = pygame.font.Font('font(s)/KarmaSuture.otf', 50)
    fontSuture_ForGameOver_Text = pygame.font.Font('font(s)/KarmaFuture.otf', 150)
    fontSuture_ForTimeAlive = pygame.font.Font('font(s)/KarmaFuture.otf', 50)

    player_gravity = 0
    run_whileLoop = True
    run_game = True   
    gameOver = False
    angle = 0
    timer = 0
    timeAlive = 0

    def display_image(sprite, spriteRectangle):
        WINDOW.blit(sprite, spriteRectangle)

    def imageLoad(imageRelativePath, convertAlpha):
        if convertAlpha:
            return pygame.image.load(imageRelativePath).convert_alpha()
        elif not convertAlpha:
            return pygame.image.load(imageRelativePath).convert()
        else:
            return pygame.image.load(imageRelativePath)

    def Display_timeAlive():
        currentTime = pygame.time.get_ticks() // 1000 - timeAlive
        TimeAlive_Text = fontSuture_ForTimeAlive.render(f'Time Alive : {currentTime}s', False, (64, 64, 64))
        TimeAlive_TextRectangle = TimeAlive_Text.get_rect(center = (400, 75))
        display_image(TimeAlive_Text, TimeAlive_TextRectangle)

    def surfaces():
        runningGame_background = imageLoad('images/Sky.png', False)
        ground = imageLoad('images/ground.png', False)
        topOfGround = HEIGHT - ground.get_size()[1]

        # scoreSuture = fontFuture.render('SCORE', False, (64, 64, 64))
        # scoreFuture = fontSuture.render('SCORE', False, (64, 64, 64))
        # scoreRectangle = scoreSuture.get_rect(center = (400, 75))
        
        gameOver_text = fontSuture_ForGameOver_Text.render('GAME OVER!', False, (255, 89, 41))
        gameOver_textRectangle = gameOver_text.get_rect(center = (WIDTH//2, HEIGHT//4))
        gameOver_textWidth, gameOver_textHeight = gameOver_text.get_size()
        aspectRatioOfGameOver_text = gameOver_textWidth / gameOver_textHeight

        retry_button = imageLoad('images/gameState_assets/retry_button.png', True)
        new_retry_button = 'soon to be used'
        retry_buttonRectangle = retry_button.get_rect(center = (400, 600))

        newHeightOfGameOver_text = 120
        newWidthOfGameOver_text = 700

        lizard = imageLoad('images/lizard/lizard (1).png', True)
        new_lizard = pygame.transform.smoothscale(lizard, (99, 100))
        lizardRectangle = new_lizard.get_rect(midbottom = (704, 681))
        jumpOver_lizardDetection_rectangle = new_lizard.get_rect()
        lizardRectangle.width = 60
        lizardRectangle.height = 1

        player = imageLoad('images/player/player_walk_1.png', True)
        new_player = pygame.transform.smoothscale(player, (90, 120))
        playerRectangle = player.get_rect(midbottom = (80, topOfGround))
        playerRectangle.width = 90
        playerRectangle.height = 120
        playerStand = imageLoad('images\player\player_stand.png', True)


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
                        player_gravity = JUMPHEIGHT

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or pygame.K_UP or pygame.K_w:
                        if variables['playerRectangle'].bottom == variables['topOfGround']:
                            player_gravity = JUMPHEIGHT
            elif gameOver:
                mouse_position = pygame.mouse.get_pos()
                if variables['retry_buttonRectangle'].collidepoint(mouse_position) and event.type == pygame.MOUSEBUTTONDOWN:
                    run_game, gameOver = True, False
                    variables['lizardRectangle'].left = 850
                    variables['playerRectangle'].midbottom = (variables['playerRectangle'].midbottom[0], variables['topOfGround'])
                    timeAlive = pygame.time.get_ticks() // 1000
        if run_game:
            display_image(variables['runningGame_background'], (0, 0))
            display_image(variables['ground'], (0, variables['topOfGround'] ))

            # pygame.draw.rect(WINDOW, '#F0B27A', variables['scoreRectangle'], 0, 30)
            # display_image(variables['scoreSuture'], variables['scoreRectangle'])
            Display_timeAlive()

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
                run_game, gameOver = False, True

        elif gameOver:
            angle = math.sin(timer) * 3.5 
            timer += 0.043

            WINDOW.fill(('black'))
            rotated_gameOver_text = pygame.transform.rotate(variables['gameOver_text'], angle)
            rotated_rectangleOfgameOver_text = rotated_gameOver_text.get_rect(center = variables['gameOver_textRectangle'].center)

            display_image(rotated_gameOver_text, rotated_rectangleOfgameOver_text)
            display_image(variables['retry_button'], variables['retry_buttonRectangle'])
            display_image(variables['playerStand'], variables['playerStand_Rectangle'])

        pygame.display.update()
        clock.tick(FPS)

main(WINDOW_WIDTH, WINDOW_HEIGHT)
# display_image(variables['start_button'], variables['start_buttonRectangle'])
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_SPACE]:
            #     print('LES JUMP')
            
            # if variables['playerRectangle'] .colliderect(variables['lizardRectangle'] ):
            #     pass
            # mousePositon = pygame.mouse.get_pos()
            # if variables['playerRectangle'] .collidepoint(mousepos):
            #     pass