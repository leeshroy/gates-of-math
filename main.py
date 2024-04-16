import pygame
import random

pygame.init()

width = 1000
height = 800

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Math Game")

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

color_mapping = { #assigns color based on specifed gate
    2: blue_character,
    3: purple_character
}

font = pygame.font.SysFont(None, 36)

army_count = 1
army = [{'image': character, 'rect': character_rect.copy(), 'color': character_image}] # copies the starting army guy

# for updating the army count and their positions
def update_army_count(count_change):
    global army_count
    army_count += count_change
    for _ in range(count_change):
        army.append({'image': character, 'rect':character_rect.copy(), 'color': character_image})

# how the gates are setup (effect 2 and 3 mean +2 and +3)
gate_width, gate_height = 150, 100
gates = [
    {'rect': pygame.Rect((width // 2) - (1.5 * gate_width), (height - gate_height) // 2, gate_width, gate_height), 'effect': 2, 'active': True},
    {'rect': pygame.Rect((width // 2) + (0.5 * gate_width), (height - gate_height) // 2, gate_width, gate_height), 'effect': 3, 'active': True}
]

# flags
move_left = move_right = move_up = move_down = False
move_speed = 6  # speed of the movement of character (can adjust later)

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
        army_member['rect'].topleft = (character_rect.left + i * 50 - ((army_count - 1) * 25), character_rect.top) # how the army is spread out when added

    game_display.fill(white_color) # moved this from bottom so it doesn't cover over everything and so it is in background
    for army_member in army:
        game_display.blit(army_member['image'], army_member['rect'])

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
            gate['reset'] = True  # Indicate that the gate has been reset

        if gate['active'] and character_rect.colliderect(gate['rect']):
            update_army_count(gate['effect'])
            gate['active'] = False  # Temporarily disable collision detection for this gate
            character_image = color_mapping.get(gate['effect'], character_image)  # Get the color for gate effect
            character = pygame.transform.scale(character_image, (60, 60))  # Scale the character image
            for _ in range(gate['effect']): #position of army
                army.append({'image': character, 'rect': character_rect.copy(), 'color': character_image})

        # Re-enable collision detection if the gate has been reset and is moving down again
        if gate['rect'].y > 0 and not gate['active'] and gate.get('reset', False):
            gate['active'] = True
            gate['reset'] = False  # Clear the reset flag now that the gate is active again

    # the total army count updated (top right)
    army_count_text = font.render(f"Army Count: {army_count}", True, red_color)
    game_display.blit(army_count_text, (width - army_count_text.get_width() - 20, 20))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
