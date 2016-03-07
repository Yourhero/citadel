import pygame, sys, random, os, eztext, glob
from Mastermind           import *
from lib.Player           import *
from lib.InputHandler     import *
from config.client_config import *
from config.server_config import *

pygame.init()
pygame.display.set_caption("Citadel 0.0.1a Testing")
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
screen.fill(WHITE)

def run():

  avatar = random.choice(glob.glob(AVATARS + "*.png"))
  username = get_player_name()
  my_player = Player(SCREENWIDTH/2, SCREENHEIGHT/2, avatar, username)
  client = MastermindClientTCP(5.0, 10.0) # connection timeout, receive timeout

  try:
    client.connect(SERVER_ADDRESS, SERVER_PORT)
  except MastermindError:
    # server not up?
    pass

  client.send(['login', username, avatar], None)
  if client.receive(True)[0] == "success":
    connected = True
  clock = pygame.time.Clock()

  while connected:
    ## LOCAL CLIENT LOGIC ##
    InputHandler.handle_keyboard(my_player)
    old_pos = [my_player.rect.x, my_player.rect.y]
    my_player.client_update()
    new_pos = [my_player.rect.x, my_player.rect.y]

    ## CLIENT / SERVER INTERACTION ##
    if old_pos[0] != new_pos[0] or old_pos[1] != new_pos[1]: # if we've moved
      client.send(['update', username, my_player.rect.x, my_player.rect.y, my_player.vel_x, my_player.vel_y], None)
    else: # haven't moved
      client.send(['sync', username])
    
    state = client.receive(True) # true = blocking
    print "State: " + str(state)

    if isinstance(state, list) and state[0] == "new_player":
      # make new player
      new_player_name = state[1]
      nstate = state[2]
      create = False
      for player in Player.List:
        if new_player_name != player.name:
          Player(nstate['x_pos'], nstate['y_pos'], nstate['avatar'], new_player_name)
        else:
          print "Skipping creating ourselves twice..."
    else:
      # update player states as normal
      pass # temp

    ## LOCAL CLIENT DRAW ##
    screen.fill(WHITE)    
    display_text(screen, 28, "Logged in as: " + username, 85, 30) # Echo user input
    display_text(screen, 28, "Citadel 0.0.1a", SCREENWIDTH  - 75, SCREENHEIGHT) # Version caption
    Entity.List.draw(screen)
    pygame.display.flip()
    clock.tick(30)

  client.disconnect()
  pygame.quit()

def get_player_name():
  named = False
  txt_input = eztext.Input(maxlength=32, color=(140, 20, 20), prompt='Choose a username: ')
  while not named:
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          named = True
    username = txt_input.value
    txt_input.update(events)
    txt_input.draw(screen)
    pygame.display.flip()
  return username

def display_text(screen, size, text, centerx, centery):
  font = pygame.font.Font(None, size)
  text = font.render(text, 1, (10, 10, 10))
  textpos = text.get_rect()
  textpos.centerx = centerx
  textpos.centery = centery - textpos.height
  screen.blit(text, textpos)

if __name__ == "__main__":
  run()
