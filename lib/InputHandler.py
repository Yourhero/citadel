import pygame

class InputHandler():

  @staticmethod
  def handle_keyboard(player):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
          player.vel_x = 15
        elif event.key == pygame.K_a:
          player.vel_x = -15
        else:
          player.vel_x = 0 
        if event.key == pygame.K_w:
          player.vel_y = -15
        elif event.key == pygame.K_s:
          player.vel_y = 15
        else:
          player.vel_y = 0