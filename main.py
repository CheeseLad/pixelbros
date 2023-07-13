import pygame

screen_width = 480
screen_height = 360

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    bg_img = pygame.image.load('img/background.png')
    bg_img = pygame.transform.scale(bg_img,(screen_width,screen_height))

    screen.blit(bg_img,(0,0))
  

    grass_files = "img/grass1.png"
    #grass_sprites = [pygame.image.load(filename).convert_alpha() for filename in grass_files]
    grass_sprites = pygame.image.load("img/grass1.png").convert_alpha()
    grass_sprites = pygame.transform.scale(grass_sprites, (500, 500))
    grass1_index = 0
    grassX = -10
    grassY = -50
    screen.blit(grass_sprites, (grassX, grassY))

    # MAIN CHARACTER

    player = pygame.image.load('img/pixel_bro_1.png').convert_alpha()
    player = pygame.transform.scale(player, (100, 100))
    playerX = 10
    playerY = 40
    screen.blit(player, (playerX, playerY))
    playerLeft = pygame.transform.flip(player, True, False)
    playerRunning = player
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) :
      playerX = playerX + 3
      playerRunning = player
      screen.blit(playerRunning, (playerX, playerY))
      pygame.display.update()
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) :
      playerX = playerX - 3
      playerRunning = playerLeft
      screen.blit(playerRunning, (playerX, playerY))
      pygame.display.update()


    pygame.display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()