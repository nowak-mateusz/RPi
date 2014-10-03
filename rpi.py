import sys
import os
import platform
import pygame
from pygame.locals import *
from pgu import gui
#import threading
import global_var as g
from gui.guibulider import *
if platform.machine() == 'armv6l':
   from Adafruit.Adafruit_MCP4725 import MCP4725
   from ds18b20 import DS18B20
   from pid import pidpy as PIDController

#for raspberry PiTFT
if platform.machine() == 'armv6l':
   os.putenv('SDL_VIDEODRIVER', 'fbcon')
   os.putenv('SDL_FBDEV' , '/dev/fb1')
   os.putenv('SDL_MOUSEDRV' , 'TSLIB')
   os.putenv('SDL_MOUSEDEV' , '/dev/input/touchscreen')


def main():

   try:
       g.TEMP_SENSOR = DS18B20()
   except:
       g.TEMP_SENSOR = None
       print 'Not found temperature sensor. Is it plugged in?'
   g.DAC = MCP4725(g.I2C_port)


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

   if platform.machine() == 'armv6l':
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

      if g.PID_start:
         pid = PIDController.pidpy(0.1, g.PID_Kp, g.PID_Ti, g.PID_Td) #init pid
         if g.TEMP_SENSOR == None:
             print 'Not found temperature sensor. Is it plugged in?'
         else:
             temp = g.TEMP_SENSOR.get_temperature()
             duty_cycle = pid.calcPID_reg4(temp, g.PID_SP, True)
             print str(temp) + ' ' + str(duty_cycle)


      app.repaintall()
      rects = app.update(g.screenSurface)
      pygame.display.update(rects)
      pygame.time.wait(10)

if __name__ == '__main__':
   main()
