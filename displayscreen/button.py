import pygame
from pygame.locals import *

class Icon:
   
   def __init__(self, name):
      self.name = name
      try:
         self.bitmap = pygame.image.load(iconPath + '/' + name + '.png')
      except:
         pass


class Button:
   
   def __init__(self, rect, **kwargs):
      self.rect = rect # Bounds
      self.color = None # Background fill color, if any
      self.iconBg = None # Background Icon (atop color fill)
      self.iconFg = None # Foreground Icon (atop background)
      self.bg = None # Background Icon name
      self.fg = None # Foreground Icon name
      self.callback = None # Callback function
      self.value = None # Value passed to callback
      self.text = None		
      for key, value in kwargs.iteritems():
         if key == 'color': self.color = value
         elif key == 'bg' : self.bg = value
         elif key == 'fg' : self.fg = value
         elif key == 'cb' : self.callback = value
         elif key == 'value': self.value = value
         elif key == 'text' : self.text = value

   def selected(self, pos):
      x1 = self.rect[0]
      y1 = self.rect[1]
      x2 = x1 + self.rect[2] - 1
      y2 = y1 + self.rect[3] - 1
      if ((pos[0] >= x1) and (pos[0] <= x2) and
          (pos[1] >= y1) and (pos[1] <= y2)):
         if self.callback:
            if self.value is None: self.callback()
            else: self.callback(self.value)
         return True
      return False

   def draw(self, screen):
      if self.color:
         screen.fill(self.color, self.rect)
      if self.iconBg:
         screen.blit(self.iconBg.bitmap,
         (self.rect[0]+(self.rect[2]-self.iconBg.bitmap.get_width())/2,
          self.rect[1]+(self.rect[3]-self.iconBg.bitmap.get_height())/2))
      if self.iconFg:
         screen.blit(self.iconFg.bitmap,
            (self.rect[0]+(self.rect[2]-self.iconFg.bitmap.get_width())/2,
             self.rect[1]+(self.rect[3]-self.iconFg.bitmap.get_height())/2))
      if self.text:
         myfont = pygame.font.SysFont("Arial", 30)
         label = myfont.render(self.text , 1, (255,255,255))
         label_coordinates = label.get_rect()
         label_width = tuple(label_coordinates)[2]
         label_hight = tuple(label_coordinates)[3]
         x = self.rect[0] + (self.rect[2] - label_width - 1)/2
         y = self.rect[1] + (self.rect[3] - label_hight - 1)/2
         screen.blit(label, (x, y))


   def setBg(self, name):
      if name is None:
         self.iconBg = None
      else:
         for i in icons:
            if name == i.name:
               self.iconBg = i
               break
