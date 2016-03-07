import pygame

class Entity(pygame.sprite.Sprite):
  
  List = pygame.sprite.Group()

  def __init__(self, x, y, image):
    pygame.sprite.Sprite.__init__(self)
    Entity.List.add(self)
    self.image  = pygame.image.load(image)
    self.base_image = self.image
    self.rect   = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.vel_x  = 0
    self.vel_y  = 0

  def destroy():
    classes.Entity.List.remove(self)
    del self