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
    if self.health <= 0:
      die()

  def server_update(self, x, y):
    self.rect.x = x
    self.rect.y = y

  def destroy():
    classes.Player.List.remove(self)
    del self