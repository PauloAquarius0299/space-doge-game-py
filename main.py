import pygame
import time 
import random 
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Dodge')

BG = pygame.image.load('space.jpg')

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 90

PLAYER_VEL = 5
STAR_WIDTH = 25
STAR_HEIGHT = 25
STAR_RADIUS = 15  
STAR_VEL = 5

FONT = pygame.font.SysFont('comicsans', 30)

PLAYER_IMG = pygame.image.load('player.png')
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f'Tempo: {round(elapsed_time)}s', 1, 'white')
    WIN.blit(time_text, (10,10))
    WIN.blit(PLAYER_IMG, (player.x, player.y))
    for star in stars:
        pygame.draw.circle(WIN, "saddlebrown", (star.x + STAR_RADIUS, star.y + STAR_RADIUS), STAR_RADIUS)
    pygame.display.update()
    
def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
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
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
            
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
            
        if hit:
            lost_text = FONT.render('Você Perdeu!', 1, "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        draw(player, elapsed_time, stars)
    
    pygame.quit()
    
if __name__ == '__main__':
    main()
