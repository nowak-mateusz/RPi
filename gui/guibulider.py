import pygame
from clock import *
from pgu import gui, timer

def deflautOnClik(value):
   print "Not click function"
   pass

# Director
class Director(object):
   
   def __init__(self):
      self.bulider = None
      
   def construct_gui(self):
      self.builder.new_gui()
      self.builder.build_gui()
      
   def get_gui(self):
      return self.builder.page
      
# Bulider      
class Builder(object):
   
   def __init__(self):
      self.page = None
   
   def new_gui(self):
      self.page = Page()
      
# Main Page Bulider  - clock   
class BuilderMainPage(Builder):

   def __init__(self,onClick=None):
      if (not onClick):
          self.onClick = deflautOnClik
      else:
         self.onClick = onClick
   
   def build_gui(self):
      cl = Clock(width=320, height=240)
      cl.connect(gui.CLICK,self.onClick,1)
      self.page.tr()
      self.page.td(cl)

# Temp page
class BuilderTempPage(Builder):
   
   def __init__(self,onClick=None):
      if (not onClick):
          self.onClick = deflautOnClik
      else:
         self.onClick = onClick
   
   def build_gui(self):
      btn = gui.Button('back')
      btn.connect(gui.CLICK,self.onClick,0)
      self.page.tr()
      self.page.td(btn)

# Product
class Page(gui.Table):

   def __init__(self):
      gui.Table.__init__(self)