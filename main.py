import pygame
import random
import math
import sys
import createMathProblems

from button import Button

pygame.init()

width = 1280
height = 720

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Math Game")
BG = pygame.image.load("assets/Background.png")
mainBG = pygame.image.load("assets/main.png")
mainmusic = "assets/sus.mp3"
exitsus = "assets/exitsus.mp3"

pygame.mixer.init()
pygame.mixer.music.load(mainmusic)
pygame.mixer.music.play()
pygame.event.wait()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

army_count = 1  # Declare army_count globally

def main_menu():
    while True:
        game_display.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        game_display.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(game_display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.load(exitsus)
                    pygame.mixer.music.play()
                    pygame.mixer.wait()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #game_display.fill("white")
        game_display.blit(BG, (0, 0))



        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        game_display.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(game_display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def createGates():
    font = pygame.font.SysFont(None, 36)
    white_color = (255, 255, 255)
    red_color = (255, 0, 0)
    problemSet = createMathProblems.createProblemSet()
    answerSet = createMathProblems.createAnswerSet(problemSet)

    # how the gates are setup (effect 2 and 3 mean +2 and +3)
    gate_width, gate_height = 150, 100
    gates = [
        {'rect': pygame.Rect((width // 2) - (1.5 * gate_width), (height - gate_height) // 2, gate_width, gate_height), 'effect': answerSet[0], 'active': True, 'collided': False},
        {'rect': pygame.Rect((width // 2) + (0.5 * gate_width), (height - gate_height) // 2, gate_width, gate_height), 'effect': answerSet[1], 'active': True, 'collided': False}
    ]
    
    # the actual gates
    for gate in gates:
        pygame.draw.rect(game_display, red_color, gate['rect'])
        effect_text = font.render(f"+{gate['effect']}", True, white_color)
        game_display.blit(effect_text, gate['rect'].center)

    # checks for the collision of the gates and updates accordingly
    for gate in gates:
        gate['rect'].y += 5  # Move the gate down every frame
        if gate['rect'].y > height:
            gate['rect'].y = random.randint(-100, -10)  # Reset to top with a random start above the screen
            gate['active'] = True  # Re-enable the gate for collision detection
            gate['collided']= False  #reset the collison flag

        if gate['active'] and character_rect.colliderect(gate['rect']) and not gate['collided']:
            update_army_count(gate['effect'])
            gate['collided'] = True  #set the collision flag

        # Re-enable collision detection if the gate has been reset and is moving down again
        if gate['rect'].y > 0 and not gate['active'] and gate.get('reset', False):
            gate['active'] = True
            gate['reset'] = False  # Clear the reset flag now that the gate is active again

def play():
    # white for background, red for gates and army count to right
    white_color = (255, 255, 255)
    red_color = (255, 0, 0)

    # size and color of the army person
    character_image = pygame.image.load('sus.png')
    purple_character= pygame.image.load('purple.png')
    blue_character= pygame.image.load('blue.png')

    character = pygame.transform.scale(character_image, (60, 60))
    purple_character = pygame.transform.scale(purple_character, (60, 60))
    blue_character = pygame.transform.scale(blue_character, (60, 60))
    character_rect = character.get_rect(center=(width // 2, height - 75))

    font = pygame.font.SysFont(None, 36)

    army = [{'image': character, 'rect': character_rect.copy(),'angle':0}] # copies the starting army guy
    createGates()
    
    # for updating the army count and their positions
    def update_army_count(gate_effect):
        global army_count  # Refer to the global variable
        army_count += gate_effect  # Increment army count by 2 for gate effect +2
        for _ in range(gate_effect):
            new_rect = character_rect.copy()
            new_rect.x = character_rect.left + i * 50 - ((army_count - 1) * 25)
            army.append({'image': blue_character, 'rect': character_rect.copy(), 'color': blue_character, 'angle':(i+1) * (360 / 10)})

    # flags
    move_left = move_right = move_up = move_down = False
    move_speed = 8  # speed of the movement of character (can adjust later)

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

        if move_left and character_rect.left > 0:
            character_rect.x -= move_speed
        if move_right and character_rect.right < width:
            character_rect.x += move_speed
        if move_up and character_rect.top > 0:
            character_rect.y -= move_speed
        if move_down and character_rect.bottom < height:
            character_rect.y += move_speed

        # position of army
        for i, army_member in enumerate(army):
            angle_step = 360 / len(army)
            angle_rad = math.radians(army_member['angle'] + i * angle_step)
            radius = 20 # Adjust the radius of the circle as needed
            center_x = character_rect.centerx  
            center_y = character_rect.centery
            army_member['rect'] = character.get_rect(center=(center_x + int(radius * math.cos(angle_rad)), center_y + int(radius * math.sin(angle_rad))))
            army_member['angle'] += 3 #changes the speed of the rotation for the army members


        game_display.blit(mainBG, (0, 0))
        #game_display.fill(white_color) # moved this from bottom so it doesn't cover over everything and so it is in background
        for army_member in army:
            game_display.blit(army_member['image'], army_member['rect'])
            game_display.blit(army[0]['image'], army[0]['rect'])

        # the total army count updated (top right)
        army_count_text = font.render(f"Army Count: {army_count}", True, red_color)
        game_display.blit(army_count_text, (width - army_count_text.get_width() - 20, 20))

        pygame.display.flip()

        pygame.time.Clock().tick(60)


main_menu()

pygame.quit()
