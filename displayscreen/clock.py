import sys
import os
import pygame
from time import strftime

class Clock():
   
   def __init__(self):
      self.dir=os.path.dirname(sys.modules[self.__class__.__module__].__file__)
      self.clockfont = os.path.join( self.dir,"resources", "SFDigitalReadout-Medium.ttf")
      self.myfont = pygame.font.Font(self.clockfont, 240)
      self.myfontsmall = pygame.font.Font(self.clockfont, 120)
      self.screensize = width, height = 320,240
      self.surface = pygame.Surface((694,466))

   def showClock(self,screen):
      self.surface.fill([0,0,0])
      mytime = strftime("%H:%M")
      mysecs = strftime("%S")
      clocklabel = self.myfont.render(mytime, 1, [255,255,255])
      secondlabel = self.myfontsmall.render(mysecs, 1, [255,255,255])
      textpos = clocklabel.get_rect()
      textpos.centerx = self.surface.get_rect().centerx - 70
      textpos.centery = self.surface.get_rect().centery
      secpos = [ textpos[0] + textpos[2] + 10, textpos[1] + 70 ]
      self.surface.blit(secondlabel, secpos)
      self.surface.blit(clocklabel, textpos)
      # Scale our surface to the required screensize before sending back
      scaled = pygame.transform.scale(self.surface,self.screensize)
      screen.blit(scaled,(0,0))