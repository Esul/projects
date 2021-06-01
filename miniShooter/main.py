import pygame
from player import Player, Aim, Shoot
from enemy import Enemy

pygame.init()

# Variables
CARRYON = True
SCORE = 0
HEALTH = 100

WIDTH = 800
HEIGHT = 600
NUMBER_OF_ENEMIES = 0
MAX_ENEMIES = 10

COLLISION_TIME = 100

all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
# COLORS
BACKGROUND = (127, 198, 164)
BG = pygame.image.load("images/grass.jpg")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_IMAGE = pygame.image.load("images/player.png")


# Opening new window
display = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(BLACK)
background.set_colorkey(BLACK)
pygame.display.set_caption('Shooter?')

# Adding Player and Aim
player = Player()
player.rect.x = (WIDTH / 2 - player.rect.width / 2)
player.rect.y = (HEIGHT / 2 - player.rect.height / 2)

aim = Aim((0, 0), (0, 0))

all_sprites.add(player)
all_sprites.add(aim)

# Clock for FPS and shooting cooldown
clock = pygame.time.Clock()
cooldown_start = pygame.time.get_ticks()
cooldown = 50


while CARRYON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CARRYON = False

    # Player, mouse positions and cooldown
    mouse_pos = pygame.mouse.get_pos()
    player_pos = (player.rect.x, player.rect.y)

    # Updating Aim and bullets
    all_bullets.update()
    aim.kill()
    aim = Aim(player_pos, mouse_pos)
    all_sprites.add(aim)

    for bullet in all_bullets:
        if bullet.rect.x > 800 or bullet.rect.y > 600 or bullet.rect.x < -bullet.rect.width or bullet.rect.y < -bullet.rect.width:
            bullet.kill()

    # Spawning and Updating Enemies
    all_enemies.update(player_pos)

    if NUMBER_OF_ENEMIES == 0:
        for index in range(MAX_ENEMIES - 1):
            enemy = Enemy(player_pos)
            NUMBER_OF_ENEMIES += 1
            all_sprites.add(enemy)
            all_enemies.add(enemy)

        MAX_ENEMIES += 1

    # Moving and shooting
    keys = pygame.key.get_pressed()
    # Detecting if mouse left button[0] is clicked.
    mouse_left = pygame.mouse.get_pressed()[0]
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.moveUp()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.moveRight()
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.moveDown()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_SPACE] or mouse_left:
        cooldown_now = pygame.time.get_ticks()
        if cooldown_now - cooldown_start >= cooldown:

            cooldown_start = pygame.time.get_ticks()

            bullet = Shoot(player_pos, mouse_pos)
            all_bullets.add(bullet)
            all_sprites.add(bullet)

    # Checking collisions between bullets and Enemies
    for bullet in all_bullets:
        killed_list = pygame.sprite.spritecollide(bullet, all_enemies, False)
        for killed in killed_list:
            SCORE += 1
            HEALTH += 1
            killed.kill()
            bullet.kill()
            NUMBER_OF_ENEMIES -= 1

    if HEALTH > 100:
        HEALTH = 100

    # Colision between Player and Enemy
    collided_list = pygame.sprite.spritecollide(player, all_enemies, False)
    for enemy in collided_list:
        if pygame.time.get_ticks() - enemy.last_collision > COLLISION_TIME:
            enemy.last_collision = pygame.time.get_ticks()
            HEALTH -= 5

    if HEALTH < 0:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU LOSE", 1, WHITE)
        display.blit(text, ((WIDTH - text.get_width()) /
                            2, (HEIGHT - text.get_height()) / 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        CARRYON = False

    # Drawing
    display.fill(BACKGROUND)
    display.blit(BG, (0, 0))
    display.blit(PLAYER_IMAGE, player_pos)
    all_sprites.draw(display)

    # SCORE
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(SCORE), 1, WHITE)
    display.blit(text, ((WIDTH - text.get_width()) / 2, 15))
    text = font.render("Health: " + str(HEALTH), 1, WHITE)
    display.blit(text, ((WIDTH - text.get_width()) / 2, 40))

    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()
