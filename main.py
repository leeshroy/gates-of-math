import pygame

pygame.init()

width = 1000    
height = 800

game_display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Math 2D Game")

white_color = (255,255,255)

character = pygame.image.load('sus.png')
grass = pygame.image.load('grass.png')
character_rect = character.get_rect()
character_rect.center = (500, 600)

character_move_amount = 10

move_left = False
move_right = False
move_up = False
move_down = False

dead = False
while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False

    if move_left:
        character_rect.x -= 1
    if move_right:
        character_rect.x += 1
    if move_up:
        character_rect.y -= 1
    if move_down:
        character_rect.y += 1

    game_display.blit(grass,(0,0))
    game_display.blit(character, character_rect)
    pygame.display.update()

pygame.quit()