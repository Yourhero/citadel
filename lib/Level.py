import pygame

class Level():

  List = []

  def __init__(self, id, name):
    Level.List.add(self)
    self.id = id
    self.name = name
