import pygame

class Entity(pygame.sprite.Sprite):
  
  List = pygame.sprite.Group()
  
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    Entity.List.add(self)
    self.x = x
    self.y = y

  def update():

  def destroy():
    classes.Entity.List.remove(self)
    del self