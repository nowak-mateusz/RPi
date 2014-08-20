import sys
import os
import pygame
import threading
from pygame.locals import *
from displayscreen.clock import *
from displayscreen.button import *            

def viewCallback(n): # Viewfinder buttons
   global screenMode
   screenMode = n

screenMode = 0 
      
buttons = [
   # Screen 0 
   [Button((130,180, 60, 60), color=[255,0,0], cb=viewCallback, value=1)],
   # Screen 1 
   [Button((130,180, 60, 60), color=[0,255,0], cb=viewCallback, value=0)]
]

def main():
   
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
     
        
if __name__ == '__main__':
   main()