import pygame, sys, random, os, eztext, glob
from lib.Player import *
from lib.InputHandler  import *

pygame.init()

BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
WHITE = (255, 255, 255)

SCREENWIDTH, SCREENHEIGHT = 1200, 800

ASSETS      = 'assets/'
AVATARS     = ASSETS + 'avatars/'
PROJECTILES = ASSETS + 'projectiles/'

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
screen.fill(WHITE)

def run():
  clock = pygame.time.Clock()
  avatar = random.choice(glob.glob(AVATARS + "*.png"))
  name = get_player_name()
  player = Player(SCREENWIDTH/2, SCREENHEIGHT/2, avatar, name)

  while True:
    clock.tick(30)
    InputHandler.handle_keyboard(player)
    player.update()
    screen.fill(WHITE)    
    display_text(screen, 28, "echo: " + name, SCREENWIDTH/4, SCREENHEIGHT/4) # Echo user input
    display_text(screen, 28, "Citadel 0.0.1a", SCREENWIDTH  - 75, SCREENHEIGHT) # Version caption
    Entity.List.draw(screen)
    pygame.display.flip()

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
