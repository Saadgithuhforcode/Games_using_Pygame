import pygame
import time
import random

pygame.font.init()

FONT = pygame.font.SysFont("time new roman", 30)

WIDTH,HEIGHT = 800,500

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Space Invaders")

BG = pygame.image.load("space image.png")
PLAYER_HEIGHT = 30
PLAYER_WIDTH = 20

VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

def draw(player, elapsed_time, stars):
    WINDOW.blit(BG,(0,0))

    time_text = FONT.render(f'Time: {round(elapsed_time)}s', 1, 'white')
    WINDOW.blit(time_text, (10, 10))

    for star in stars:
        pygame.draw.rect(WINDOW, 'yellow', star)

    pygame.draw.rect(WINDOW, 'red', player)

    pygame.display.update()

def game():

    run = True

    player = pygame.Rect(400, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False
    while run:

        star_count += clock.tick(60)  

        elapsed_time = time.time() - start_time

        if star_count >= star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x , -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

                star_add_increment = max(200, star_add_increment - 50)
                star_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - VEL > 0 or keys[pygame.K_LEFT] and player.x - VEL > 0:
            player.x -= VEL
        if keys[pygame.K_d] and player.x + VEL + PLAYER_WIDTH < WIDTH or keys[pygame.K_RIGHT] and player.x + VEL + PLAYER_WIDTH < WIDTH:
            player.x += VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + STAR_HEIGHT >= player.y and star.colliderect(player):
                hit = True
                break

        if hit:
            lost_text = FONT.render('YOU LOST!', 1, 'RED')
            WINDOW.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break


        draw(player, elapsed_time, stars)

if __name__ == "__main__":
    game()
