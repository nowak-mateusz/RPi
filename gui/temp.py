import os
import glob
import time
import pygame
from pgu import gui

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


class Temperature(gui.Widget):
   def __init__(self,**params):
      params.setdefault('cls','temperature')
      gui.Widget.__init__(self,**params)

      os.system('modprobe w1-gpio')
      os.system('modprobe w1-therm')

      self.base_dir = '/sys/bus/w1/devices/'
      self.device_folder = glob.glob(base_dir + '28*')[0]
      self.device_file = device_folder + '/w1_slave'

      self.myfont = os.path.join( os.path.dirname(sys.modules[self.__class__.__module__].__file__),"resources", "SFDigitalReadout-Medium.ttf")
      self.style.check("font")
      self.font = self.style.font
      self.style.width, self.style.height = self.font.size('00.00 C')

   def paint(self,s):
      deg_c, deg_f = read_temp()
      s.blit(self.font.render( "%0.2f C" % (deg_c) , 1, self.style.color),(0,0))
   

   def read_temp_raw():
      f = open(self.device_file, 'r')
      lines = f.readlines()
      f.close()
      return lines

   def read_temp():
      lines = read_temp_raw()
      while lines[0].strip()[-3:] != 'YES':
         time.sleep(0.2)
         lines = read_temp_raw()
      equals_pos = lines[1].find('t=')
      if equals_pos != -1:
         temp_string = lines[1][equals_pos+2:]
         temp_c = float(temp_string) / 1000.0
         temp_f = temp_c * 9.0 / 5.0 + 32.0
         return temp_c, temp_f

   def set_font(self, font):
      """Set the font used to render this label."""
      self.font = font
      # Signal to the application that we need a resize
      self.chsize()
      
   def set_font_size(self, font_size):
      self.font = pygame.font.Font(self.myfont, font_size)
      self.chsize()


