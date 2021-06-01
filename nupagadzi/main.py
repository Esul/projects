from random import randint
import pygame
from egg import Egg
from bascket import Bascket
pygame.init()


# Global Colors
BACKGROUND_COLOR = (229, 88, 18)
LINE_COLOR = (14, 71, 73)
SCORE_COLOR = (237, 175, 184)

POSITIONS = ['LU', 'LD', 'RU', 'RD']
SCORE = 0
LIVES = 3
# Open window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Nu Pagadzi!!!")

# Adding bascket
bascket = Bascket()

# List containing all sprites
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(bascket)

# Loop stopper
CARRY_ON = True

# Clock to control FPS
clock = pygame.time.Clock()

# Main loop
NUMBER_OF_EGGS = 0
while CARRY_ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CARRY_ON = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                CARRY_ON = False

    # Detecting if player has 0 lives left
    if LIVES == 0:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU LOST!", 1, SCORE_COLOR)
        screen.blit(text, (400 - text.get_width() / 2, 253))
        pygame.display.flip()
        pygame.time.wait(3000)
        CARRY_ON = False

    # Moving Bascket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bascket.moveLeft()
    if keys[pygame.K_RIGHT]:
        bascket.moveRight()
    if keys[pygame.K_UP]:
        bascket.moveUp()
    if keys[pygame.K_DOWN]:
        bascket.moveDown()

    # -----Gama Logic
    all_sprites_list.update()


    # Laying an egg if there is none
    if NUMBER_OF_EGGS == 0:
        egg = Egg(POSITIONS[randint(0, 3)])
        NUMBER_OF_EGGS += 1
        all_sprites_list.add(egg)

    # Collision detection
    if pygame.sprite.collide_mask(bascket, egg):
        SCORE += 1
        egg.kill()
        NUMBER_OF_EGGS = 0

    # Detecting if the egg went from the screen
    if egg.rect.x > 800 or egg.rect.x < 0 or egg.rect.y > 600:
        LIVES -= 1
        egg.kill()
        NUMBER_OF_EGGS = 0

    # -----Drawing
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, (LINE_COLOR), [0, 100], [180, 160], 10)
    pygame.draw.line(screen, (LINE_COLOR), [0, 300], [180, 360], 10)
    pygame.draw.line(screen, (LINE_COLOR), [800, 100], [620, 160], 10)
    pygame.draw.line(screen, (LINE_COLOR), [800, 300], [620, 360], 10)

    # Score and lives display
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(SCORE), 1, SCORE_COLOR)
    screen.blit(text, (400 - text.get_width() / 2, 25))
    text = font.render("Lives: " + str(LIVES), 1, SCORE_COLOR)
    screen.blit(text, (400 - text.get_width() / 2, 65))

    # Draw all sprites
    all_sprites_list.draw(screen)

    # Update the screen
    pygame.display.flip()

    # FPS
    clock.tick(60)


pygame.quit()
