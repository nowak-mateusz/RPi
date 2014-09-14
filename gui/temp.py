import sys
import os
import glob
import time
import pygame
from pgu import gui
from ds18b20 import DS18B20
import global_var as g


class Temperature(gui.Widget):
   def __init__(self,**params):
      params.setdefault('cls','temperature')
      gui.Widget.__init__(self,**params)
      self.myfont = g.digitalFont
      print self.myfont
      self.style.check("font")
      self.font = self.style.font
      self.style.width, self.style.height = self.font.size('00.00 C')

      self.sensor = DS18B20()

   def paint(self,s):
      s.blit(self.font.render( "%0.2f C" % (self.sensor.get_temperature()) , 1, self.style.color),(0,0))
   
   def set_font(self, font):
      """Set the font used to render this label."""
      self.font = font
      # Signal to the application that we need a resize
      self.chsize()
      
   def set_font_size(self, font_size):
      self.font = pygame.font.Font(self.myfont, font_size)
      self.chsize()

   def resize(self,width=None,height=None):
      (self.style.width, self.style.height) = self.font.size('00.00 C')
      return (self.style.width, self.style.height)
