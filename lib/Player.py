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
    self.face = 2
    self.max_speed = 20
    self.vel_gain = 6
    self.vel_decay = 3
    
  def client_update(self):
    self.rect.x += self.vel_x
    self.rect.y += self.vel_y
    self.align_image_with_direction()

  def server_update(self, x, y):
    self.rect.x += x
    self.rect.y += y
    self.align_image_with_direction()
   
  def align_image_with_direction(self):
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

  def destroy():
    classes.Player.List.remove(self)
    del self
  
  def decay(self, vector):
    if vector == 'x':
      self.vel_x = 0
      #if self.vel_x > 0:
       # self.vel_x -= self.vel_decay
      #elif self.vel_x < 0:
       # self.vel_x += self.vel_decay
    elif vector == 'y':
      self.vel_y = 0
      #if self.vel_y > 0:
       # self.vel_y -= self.vel_decay
      #elif self.vel_y < 0:
       # self.vel_y += self.vel_decay
