import pygame

class InputHandler():
  
  @staticmethod
  def handle_keyboard(player):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      #elif event.type == pygame.KEYDOWN:
       # if event.key == pygame.K_d:
        #  player.decay('y')
        #elif event.key == pygame.K_a:
         # player.decay('y')
        #elif event.key == pygame.K_w:
        #  player.decay('x')
        #elif event.key == pygame.K_s:
        #  player.decay('x')
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_d] and keys[pygame.K_w]:
      player.face = 1
      if abs(player.vel_x) <= player.max_speed:
        player.vel_x += player.vel_gain
      if abs(player.vel_y) <= player.max_speed:
        player.vel_y -= player.vel_gain
    elif keys[pygame.K_d] and keys[pygame.K_s]:
      player.face = 3
      if abs(player.vel_x) <= player.max_speed:
        player.vel_x += player.vel_gain
      if abs(player.vel_y) <= player.max_speed:
        player.vel_y += player.vel_gain
    elif keys[pygame.K_a] and keys[pygame.K_s]:
      player.face = 5
      if abs(player.vel_x) <= player.max_speed:
        player.vel_x -= player.vel_gain
      if abs(player.vel_y) <= player.max_speed:
        player.vel_y += player.vel_gain
    elif keys[pygame.K_a] and keys[pygame.K_w]:
      player.face = 7
      if abs(player.vel_x) <= player.max_speed:
        player.vel_x -= player.vel_gain
      if abs(player.vel_y) <= player.max_speed:
        player.vel_y -= player.vel_gain
    elif keys[pygame.K_d]:
      player.face = 2
      player.decay('y')
      if abs(player.vel_x) <= player.max_speed:
        player.vel_x += player.vel_gain
    elif keys[pygame.K_a]:
      player.face = 6
      player.decay('y')
      if abs(player.vel_x) <= player.max_speed:
        player.vel_x -= player.vel_gain
    elif keys[pygame.K_w]:
      player.face += 0
      player.decay('x')
      if abs(player.vel_y) <= player.max_speed:
        player.vel_y -= player.vel_gain
    elif keys[pygame.K_s]:
      player.face = 4
      player.decay('x')
      if abs(player.vel_y) <= player.max_speed:
        player.vel_y += player.vel_gain
    else:
      player.decay('x')
      player.decay('y')