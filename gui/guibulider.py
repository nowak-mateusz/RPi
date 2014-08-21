import pygame
from clock import *
from pgu import gui, timer

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
      
# Main Page Bulider  - clock and button   
class BuilderMainPage(Builder):
   
   def build_gui(self):
      main = gui.Container(width=320, height=240)
      main.add(Clock(width=320, height=240),0,0)
      self.page.tb = gui.Table()
      self.page.tb.tr()
      self.page.tb.td(main)
      self.page.tb.tr()
      self.page.tb.td(gui.Button('test'))


# Product
class Page(gui.Desktop):

   def __init__(self):
      gui.Desktop.__init__(self)
      self.tb = None
      
   def ini(self,disp=None):
      self.init(self.tb, disp)
      
      
if __name__ == "__main__":
   director = Director()
   director.builder = BuilderMainPage()
   director.construct_gui()
   app = director.get_gui()
   app.ini()
   app.update()
   done = False
   
   while not done:
      # Process events
      for ev in pygame.event.get():
          if (ev.type == pygame.QUIT or 
              ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
              done = True
          else:
              # Pass the event off to pgu
              app.event(ev)

      # Give pgu a chance to update the display
      app.paint()
      pygame.display.update()
      pygame.time.wait(10)
   
      
