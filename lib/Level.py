import pygame

class Level():

  List = []

  def __init__(self, id, name, SCREENHEIGHT, SCREENWIDTH):
    #Level.List.add(self)
    self.id = id
    self.name = name
    self.max_y = SCREENHEIGHT
    self.max_x = SCREENWIDTH
