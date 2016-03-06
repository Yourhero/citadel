import pygame, sys, random, os, eztext
import lib.Player

pygame.init()

BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
WHITE = (255, 255, 255)
SCREENWIDTH, SCREENHEIGHT = 1200, 800

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
screen.fill(WHITE)

font = pygame.font.Font(None, 36)
text = font.render("Citadel  0.0.1a", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = SCREENWIDTH  - textpos.width
textpos.centery = SCREENHEIGHT - textpos.height
screen.blit(text, textpos)

for file in os.listdir('assets/avatars'):
  if os.path.isfile(file):
    print file


avatars = ("avatar01.png", "avatar02.png", "avatar03.png")
avatar = random.choice(avatars)

while True:
  clock.tick(30)
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.flip()






#def get_player_name():
