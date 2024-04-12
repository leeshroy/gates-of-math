import pygame

pygame.init()

width = 1000    
height = 800

game_display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Math 2D Game")

white_color = (255,255,255)

dead = False

character = pygame.image.load('sus.png')
grass = pygame.image.load('grass.png')

character_move_amount = 10
x_change = 0

def add_character_at_location(x,y):
    game_display.blit(character, (x,y))

x = (width * 0.95)
y = (height * 0.5)




while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change  -= character_move_amount
            elif event.key == pygame.K_RIGHT:
                x_change += character_move_amount
            elif event.key == pygame.K_UP:
                y -= character_move_amount
            elif event.key == pygame.K_DOWN:
                y +- character_move_amount


    x += x_change

    game_display.blit(grass,(0,0))
    add_character_at_location(-1000 + x,y)
    pygame.display.update()



pygame.quit()