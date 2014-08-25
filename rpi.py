import sys
import os
import pygame
import threading
import gui as mygui
from pgu import gui
#from gui.clock import *

#for raspberry PiTFT
#os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV' , '/dev/fb1')
#os.putenv('SDL_MOUSEDRV' , 'TSLIB')
#os.putenv('SDL_MOUSEDEV' , '/dev/input/touchscreen')

mode = 0
click = False


def onClick(value):
   global mode, click
   mode = value
   click = True
   print 'Click '+ str(value)     

def main():
   global mode, click
   director = mygui.Director()
   director.builder = mygui.BuilderTempPage(onClick)
   director.construct_gui()
 
   app = gui.Desktop()
   app.connect(gui.QUIT,app.quit,None)
   app.connect(gui.QUIT,app.quit,None)
   
   size = width, height = 320, 240
   
   #init
   pygame.init()
   #pygame.mouse.set_visible(0)
   screen = pygame.display.set_mode(size)
   
   
   app.init(director.get_gui(),screen)
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
	
      # Give pgu a chance to update the displa
      if mode == 0 and click:
         director.builder = mygui.BuilderMainPage(onClick)
         director.construct_gui()
         app.init(director.get_gui())
         click = False
      elif mode == 1 and click:
         director.builder = mygui.BuilderTempPage(onClick)
         director.construct_gui()
         app.init(director.get_gui())
         click = False
         
      app.paint()
      pygame.display.update()
      pygame.time.wait(10)
   
      
   '''
   app = gui.Desktop()
   app.connect(gui.QUIT,app.quit,None)
   
   main = gui.Container(width=320, height=240)
   main.add(Clock(width=320, height=240),0,0)
   main.add(gui.Button("test"),130,180)

   app.run(main)   

 
   print os.name
   size = width, height = 320, 240
   
   #init
   pygame.init()
   #pygame.mouse.set_visible(0)
   screen = pygame.display.set_mode(size)
   
   clock = Clock()
   
   print "mainloop.."
   
   while(True):
   
      while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if(event.type is MOUSEBUTTONDOWN):
               pos = pygame.mouse.get_pos()
               for b in buttons[screenMode]:
                  if b.selected(pos):
                     break
         
         if screenMode >= 0: break
         
      if screenMode == 0:
         screen.fill((0,0,0))
         clock.showClock(screen)
         
      if screenMode == 1:
         screen.fill((0,0,0))
         
      for i,b in enumerate(buttons[screenMode]):
         b.draw(screen)
         
         
         
      pygame.display.update()  
      '''
        
if __name__ == '__main__':
   main()
