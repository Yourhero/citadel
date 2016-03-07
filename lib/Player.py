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
    self.last_face = 2
    self.max_speed = 20
    self.vel_gain = 5
    self.vel_decay = 2
    self.SCREENHEIGHT = y*2
    self.SCREENWIDTH = x*2
    
    
  def client_update(self):
    if self.vel_x > self.max_speed:
      self.vel_x = self.max_speed
    elif self.vel_x < -self.max_speed:
      self.vel_x = -self.max_speed
    if self.vel_y > self.max_speed:
      self.vel_y = self.max_speed
    elif self.vel_y < -self.max_speed:
      self.vel_y = -self.max_speed
      
    #edge detection        
    predicted_x = self.rect.x + self.vel_x
    predicted_y = self.rect.y + self.vel_y
        
    if predicted_x < 0:
      self.vel_x = 0
    elif predicted_x + self.rect.width > self.SCREENWIDTH:
      self.vel_x = 0
    if predicted_y < 0:
      self.vel_y = 0
    elif predicted_y + self.rect.width > self.SCREENHEIGHT:
      self.vel_y = 0
      
      
    self.rect.x += self.vel_x
    self.rect.y += self.vel_y
    self.align_image_with_direction()

  def server_update(self, x, y):
    self.rect.x = x
    self.rect.y = y
    self.align_image_with_direction()
   
  def align_image_with_direction(self):
    if self.face == 0: #up
      if self.last_face == 0:
        return
      elif self.last_face in [5,6,7]:
        self.image = pygame.transform.rotate(pygame.transform.flip(self.base_image, True, False), 270)
      else:
        self.image = pygame.transform.rotate(self.base_image, 90)
    elif self.face == 1: #up-right
      if self.last_face == 1:
        return
      self.image = pygame.transform.rotate(self.base_image, 45)
    elif self.face == 2: #right
      if self.last_face == 2:
        return
      self.image = self.base_image
    elif self.face == 3: #down-right
      if self.last_face == 3:
        return
      self.image = pygame.transform.rotate(self.base_image, 315)
    elif self.face == 4: #down
      if self.last_face == 4:
        return          
      elif self.last_face in [5,6,7]:
        self.image = pygame.transform.rotate(pygame.transform.flip(self.base_image, True, False), 90)
      else:
        self.image = pygame.transform.rotate(self.base_image, 270)
    elif self.face == 5: #down-left
      if self.last_face == 5:
        return
      self.image = pygame.transform.rotate(pygame.transform.flip(
        self.base_image, True, False), 45)
    elif self.face == 6: #left
      if self.last_face == 6:
        return
      self.image = pygame.transform.flip(self.base_image, True, False)
    elif self.face == 7: #up-left
      if self.last_face == 7:
        return
      self.image = pygame.transform.rotate(pygame.transform.flip(
        self.base_image, True, False), 315)

  def destroy():
    classes.Player.List.remove(self)
    del self
  
  def decay(self, vector):
    if vector == 'x':
      #self.vel_x = 0
      if self.vel_x > 0:
        self.vel_x -= self.vel_decay
      elif self.vel_x < 0:
        self.vel_x += self.vel_decay
    elif vector == 'y':
      #self.vel_y = 0
      if self.vel_y > 0:
        self.vel_y -= self.vel_decay
      elif self.vel_y < 0:
        self.vel_y += self.vel_decay
