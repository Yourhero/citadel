import pygame
from lib.Entity import *

class Player(Entity):

  List = pygame.sprite.Group()

  @staticmethod
  def update_all():
    for player in Player.List:
      player.update()

  def __init__(self, x, y, image, name):
    Entity.__init__(self, x, y, image)
    Player.List.add(self)
    self.health = 100
    self.name   = name


  def client_update(self):
    self.rect.x += self.vel_x
    self.rect.y += self.vel_y
    if self.face == 0:
      self.image = pygame.transform.rotate(self.base_image, 90)
    elif self.face == 1:
      self.image = pygame.transform.rotate(self.base_image, 45)
    elif self.face == 2:
      self.image = self.base_image
    elif self.face == 3:
      self.image = pygame.transform.rotate(self.base_image, 315)
    elif self.face == 4:
      self.image = pygame.transform.rotate(self.base_image, 270)
    elif self.face == 5:
      self.image = pygame.transform.flip(self.base_image, True, False)
      self.image = pygame.transform.rotate(self.image, 45)
    elif self.face == 6:
      self.image = pygame.transform.flip(self.base_image, True, False)
    elif self.face == 7:
      self.image = pygame.transform.flip(self.base_image, True, False)
      self.image = pygame.transform.rotate(self.image, 315)
    
    if self.health <= 0:
      die()

  def server_update(self, x, y):
    self.rect.x = x
    self.rect.y = y

  def destroy():
    classes.Player.List.remove(self)
    del self