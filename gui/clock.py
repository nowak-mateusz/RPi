import sys
import os
import pygame
from time import strftime
from pgu import gui

class Clock(gui.Widget):

   def __init__(self,**params):
      params.setdefault('cls','clock')
      gui.Widget.__init__(self,**params)
      self.clockfont = os.path.join( os.path.dirname(sys.modules[self.__class__.__module__].__file__),"resources", "SFDigitalReadout-Medium.ttf")
      self.style.check("font")
      self.font = self.style.font
      self.style.width, self.style.height = self.font.size('00:00:00')
   
   def paint(self,s):
      s.blit(self.font.render(strftime("%H:%M:%S"), 1, self.style.color),(0,0))

   def event(self,e):
      if e.type == gui.ENTER: self.repaint()
      elif e.type == gui.EXIT: self.repaint()
      elif e.type == gui.FOCUS: self.repaint()
      elif e.type == gui.BLUR: self.repaint()
      elif e.type == gui.MOUSEBUTTONDOWN: self.repaint()
      elif e.type == gui.MOUSEBUTTONUP: self.repaint()
      elif e.type == gui.CLICK: self.click()

   def click(self):
      pass
   
   def resize(self,width=None,height=None):
      (self.style.width, self.style.height) = self.font.size('00:00:00')
      return (self.style.width, self.style.height)

   def set_font(self, font):
      """Set the font used to render this label."""
      self.font = font
      # Signal to the application that we need a resize
      self.chsize()
      
   def set_font_size(self, font_size):
      self.font = pygame.font.Font(self.clockfont, font_size)
      self.chsize()