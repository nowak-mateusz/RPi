import sys
import os
import pygame
from time import strftime
from pgu import gui

class Clock(gui.Widget):

   def __init__(self,**params):
      gui.Widget.__init__(self,**params)
      self.dir=os.path.dirname(sys.modules[self.__class__.__module__].__file__)
      self.clockfont = os.path.join( self.dir,"resources", "SFDigitalReadout-Medium.ttf")
      self.myfont = pygame.font.Font(self.clockfont, 240)
      self.myfontsmall = pygame.font.Font(self.clockfont, 120)
      #self.screensize = width, height = 320,240
      self.surface = pygame.Surface((694,466))
   
   def paint(self,s):
      pygame.transform.scale(s,(694,466),self.surface)
      mytime = strftime("%H:%M")
      mysecs = strftime("%S")
      clocklabel = self.myfont.render(mytime, 1, [0,0,0])
      secondlabel = self.myfontsmall.render(mysecs, 1, [0,0,0])
      textpos = clocklabel.get_rect()
      textpos.centerx = self.surface.get_rect().centerx - 70
      textpos.centery = self.surface.get_rect().centery
      secpos = [ textpos[0] + textpos[2] + 10, textpos[1] + 70 ]
      self.surface.blit(secondlabel, secpos)
      self.surface.blit(clocklabel, textpos)
      # Scale our surface to the required screensize before sending back
      scaled = pygame.transform.scale(self.surface,(self.rect.w,self.rect.h))
      s.blit(scaled,(0,0))
      return

   def update(self,s):
      return [pygame.Rect(0,0,self.rect.w,self.rect.h)]

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
      # Return the width and height of this widget
      return 320,240
