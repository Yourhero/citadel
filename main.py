import pygame, sys, random, os, eztext, glob
from Mastermind           import *
from lib.Player           import *
from lib.InputHandler     import *
from config.client_config import *
from config.server_config import *
from lib.Level            import *

pygame.init()
pygame.display.set_caption("Citadel 0.0.1a Testing")
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
screen.fill(WHITE)
level = Level(1,'test',SCREENHEIGHT,SCREENWIDTH)

def run():

  avatar = random.choice(glob.glob(AVATARS + "*.png"))
  name = get_player_name()
  player = Player(SCREENWIDTH/2, SCREENHEIGHT/2, avatar, name)
  client = MastermindClientTCP(5.0, 10.0) # connection timeout, receive timeout

  try:
    client.connect(SERVER_ADDRESS, SERVER_PORT)
  except MastermindError:
    # server not up?
    pass

  client.send(['login', name, avatar], None)
  if client.receive(True)[0] == "success":
    connected = True
    clock = pygame.time.Clock()

  while connected:
    InputHandler.handle_keyboard(player)
    old_pos = [player.rect.x, player.rect.y]
    player.client_update()
    new_pos = [player.rect.x, player.rect.y]
    if old_pos[0] != new_pos[0] or old_pos[1] != new_pos[1]:
      client.send(['update', name, player.rect.x, player.rect.y, player.vel_x, player.vel_y], None)
      state = client.receive(True) # false = non-blocking
      print "The state: " + str(state)
      if state[0] == 'move':
        player.server_update(state[1], state[2])
    else: # player hasn't moved
      pass
    screen.fill(WHITE)    
    display_text(screen, 28, "echo: " + name, 10, 10) # Echo user input
    display_text(screen, 28, "Citadel 0.0.1a", SCREENWIDTH  - 75, SCREENHEIGHT) # Version caption
    Entity.List.draw(screen)
    pygame.display.flip()
    clock.tick(30)

  client.disconnect()
  pygame.quit()

def get_player_name():
  named = False
  txt_input = eztext.Input(maxlength=32, color=(140, 20, 20), prompt='Choose a name: ')
  while not named:
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          named = True
    name = txt_input.value
    txt_input.update(events)
    txt_input.draw(screen)
    pygame.display.flip()
  return name

def display_text(screen, size, text, centerx, centery):
  font = pygame.font.Font(None, size)
  text = font.render(text, 1, (10, 10, 10))
  textpos = text.get_rect()
  textpos.centerx = centerx
  textpos.centery = centery - textpos.height
  screen.blit(text, textpos)

if __name__ == "__main__":
  run()
