import sys
import os
import pygame
from pygame.locals import *
from pgu import gui
#import threading
import global_var as g
from gui.guibulider import *
from Adafruit.Adafruit_MCP4725 import MCP4725

#for raspberry PiTFT
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV' , '/dev/fb1')
os.putenv('SDL_MOUSEDRV' , 'TSLIB')
os.putenv('SDL_MOUSEDEV' , '/dev/input/touchscreen')


def main():
   director = Director()
   director.builder = BuilderWelcomPage()
   director.construct_gui()

   app = gui.Desktop()
   app.connect(gui.QUIT,app.quit,None)

   #c = gui.Table()
   #c.tr()
   #c.td(gui.Label("Gui Widgets"))

   #app.run(c)

   #init
   g.screenSurface = pygame.display.set_mode((g.SCREEN_WIDTH, g.SCREEN_HEIGHT))

   pygame.mouse.set_visible(0)

   app.init(director.get_gui(), g.screenSurface)
   done = False
   pygame.time.wait(10)

   while not done:
      # Process events
      for ev in pygame.event.get():
          if (ev.type == pygame.QUIT or
              ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
              done = True
          else:
              # Pass the event off to pgu
              app.event(ev)

      # Give pgu a chance to update the displa
      if g.mode == 0 and g.click:
         director.builder = BuilderMainPage()
         director.construct_gui()
         app.init(director.get_gui())
         g.click = False
      elif g.mode == 1 and g.click:
         director.builder = BuilderTempPage()
         director.construct_gui()
         app.init(director.get_gui())
         g.click = False
      elif g.mode == 2 and g.click:
         director.builder = BuilderSliderPage()
         director.construct_gui()
         app.init(director.get_gui())
         g.click = False
      elif g.mode == 3 and g.click:
	 director.builder = BuilderPIDMainPage()
	 director.construct_gui()
	 app.init(director.get_gui())
	 g.click = False
      elif g.mode == 10 and g.click:
         director.builder = BuilderPIDSettingsPage()
         director.construct_gui()
         app.init(director.get_gui())
         g.click = False
      elif g.mode == 11 and g.click:
         director.builder = BuilderKeyboardPage()
         director.construct_gui()
         app.init(director.get_gui())
         g.click = False

      app.repaintall()
      rects = app.update(g.screenSurface)
      pygame.display.update(rects)
      pygame.time.wait(10)

if __name__ == '__main__':
   main()
