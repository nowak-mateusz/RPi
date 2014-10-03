import pygame
import platform
from pygame.locals import *
from pgu import gui

from clock import *
from temp import *

import global_var as g
#if platform.machine() == 'armv6l':
#   from Adafruit.Adafruit_MCP4725 import MCP4725

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

class BuilderWelcomPage(Builder):

   def build_gui(self):
      self.page.tr()
      self.page.td(gui.Label('Welcom'))

# Main Page Bulider  - clock
class BuilderMainPage(Builder):

   def build_gui(self):
      cl = Clock()
      cl.connect(gui.CLICK,self.onClick,1)
      cl.set_font_size(90)
      self.page.tr()
      self.page.td(cl,colspan=2)
      #self.page.tr()
      #self.page.td(gui.Label("Slider"))
      #self.page.td(gui.Label("Slider"))

   def onClick(self,value):
     g.mode = value
     g.click = True

# Temp page
class BuilderTempPage(Builder):

   def build_gui(self):
       if g.TEMP_SENSOR == None :
           btn_n = gui.Button('next',height=50)
           btn_n.connect(gui.CLICK,self.onClick,2)
           btn_b = gui.Button('back',height=50)
           btn_b.connect(gui.CLICK,self.onClick,0)
           self.page.tr()
           self.page.td(gui.Label('Not found temperature sensor.'),colspan=2)
           self.page.tr()
           self.page.td(btn_b)
           self.page.td(btn_n,colspan=2)
       else:
           temp = Temperature()
           temp.set_font_size(90)
           btn_n = gui.Button('next',height=50)
           btn_n.connect(gui.CLICK,self.onClick,2)
           btn_b = gui.Button('back',height=50)
           btn_b.connect(gui.CLICK,self.onClick,0)
           self.page.tr()
           self.page.td(temp,colspan=2)
           self.page.tr()
           self.page.td(btn_b)
           self.page.td(btn_n,colspan=2)

   def onClick(self,value):
      g.mode = value
      g.click = True

# Slider page
class BuilderSliderPage(Builder):

   def build_gui(self):
      btn_n = gui.Button('next',height=50)
      btn_n.connect(gui.CLICK,self.onClick,3)
      btn_b = gui.Button('back',height=50)
      btn_b.connect(gui.CLICK,self.onClick,1)
      slider = gui.HSlider(value=g.DAC_value,min=0,max=4095,size=30,width=220,height=30)
      slider.connect(gui.CHANGE, self.sliderFunction, slider)
      self.lbl = gui.Label('Out Value: ' + "%0.3f" % (g.DAC_value * 4.56 / 4095) + ' V')

      if g.PID_start == 1:
         slider.disabled = True
         slider.blur()
         slider.chsize()
      else:
          slider.disabled = False
          slider.blur()
          slider.chsize()

      self.page.tr()
      self.page.td(self.lbl,colspan=2)
      self.page.tr()
      self.page.td(slider,colspan=2,height=50)
      self.page.tr()
      self.page.td(btn_b)
      self.page.td(btn_n,colspan=2)

   def onClick(self,value):
      g.mode = value
      g.click = True

   def sliderFunction(self,value):
      g.DAC_value = value.value;
      self.lbl.set_text('Out Value: ' + "%0.3f" % (value.value * 4.56 / 4095) + ' V')
      g.DAC.setVoltage(value.value)
      #print str(value.value*100/4095)

class BuilderPIDMainPage(Builder):

   def build_gui(self):
      self.btn_start = gui.Button('Start',height=50)
      self.btn_stop = gui.Button('Stop',height=50)
      self.btn_settings = gui.Button('Settings',height=50)
      self.btn_plot = gui.Button('Plot',height=50)
      self.btn_back = gui.Button('Back',height=50)

      self.btn_start.connect(gui.CLICK,self.btn_start_click,1)
      self.btn_stop.connect(gui.CLICK,self.btn_stop_click,0)
      self.btn_back.connect(gui.CLICK,self.btn_chmode_click,2)
      self.btn_settings.connect(gui.CLICK,self.btn_chmode_click,10)


      if g.PID_start == 0:
         self.btn_start_on()
      else:
         self.btn_start_off()

      self.page.tr()
      self.page.td(gui.Label('PID'),colspan=2)
      self.page.tr()
      self.page.td(self.btn_start)
      self.page.td(self.btn_stop)
      self.page.tr()
      self.page.td(self.btn_settings)
      self.page.td(self.btn_plot,height=80)
      self.page.tr()
      self.page.td(self.btn_back,colspan=2)

   def btn_start_click(self,value):
      self.btn_start_off()
      g.PID_start = value

   def btn_stop_click(self,value):
      self.btn_start_on()
      g.PID_start = value

   def btn_start_on(self):
      self.btn_start.disabled = False
      self.btn_stop.disabled = True
      self.btn_settings.disabled = False
      self.btn_stop.blur()
      self.btn_stop.chsize()

   def btn_start_off(self):
      self.btn_start.disabled = True
      self.btn_stop.disabled = False
      self.btn_settings.disabled = True
      self.btn_settings.blur()
      self.btn_settings.chsize()
      self.btn_start.blur()
      self.btn_start.chsize()

   def btn_chmode_click(self,value):
      g.mode = value
      g.click = True

class BuilderPIDSettingsPage(Builder):

    def build_gui(self):
        self.lbl_title = gui.Label('PID Settings')

        self.lbl_SP = gui.Label('SP: ' + "%0.2f" % g.PID_SP)

        self.lbl_Kp = gui.Label('Kp: ' + "%0.4f" % g.PID_Kp)
        self.lbl_Ti = gui.Label('Ti: ' + "%0.4f" % g.PID_Ti)
        self.lbl_Td = gui.Label('Td: ' + "%0.4f" % g.PID_Td)

        self.btn_SP_change = gui.Button('Change',height=30)

        self.btn_Kp_change = gui.Button('Change',height=30)
        self.btn_Ti_change = gui.Button('Change',height=30)
        self.btn_Td_change = gui.Button('Change',height=30)

        #self.btn_save = gui.Button('Save',height=30)
        #self.btn_cancel = gui.Button('Cancel',height=30)
        self.btn_ok = gui.Button('OK',height=40)

        self.btn_SP_change.connect(gui.CLICK,self.btn_change_click,0)
        self.btn_Kp_change.connect(gui.CLICK,self.btn_change_click,1)
        self.btn_Ti_change.connect(gui.CLICK,self.btn_change_click,2)
        self.btn_Td_change.connect(gui.CLICK,self.btn_change_click,3)

        #self.btn_cancel.connect(gui.CLICK,self.btn_cancel_click,3)
        self.btn_ok.connect(gui.CLICK,self.btn_ok_click,3)

        self.page.tr()
        self.page.td(self.lbl_title,colspan=2)
        self.page.tr()
        self.page.td(self.lbl_SP)
        self.page.td(self.btn_SP_change,height=50,width=100)
        self.page.tr()
        self.page.td(self.lbl_Kp)
        self.page.td(self.btn_Kp_change,height=35)
        self.page.tr()
        self.page.td(self.lbl_Ti)
        self.page.td(self.btn_Ti_change,height=35)
        self.page.tr()
        self.page.td(self.lbl_Td)
        self.page.td(self.btn_Td_change,height=35)
        self.page.tr()
        #self.page.td(self.btn_save)
        #self.page.td(self.btn_cancel,height=50)
        self.page.td(self.btn_ok,colspan=2,height=50)

    #def btn_cancel_click(self,value):
    #   g.mode = value
    #   g.click = True

    def btn_ok_click(self,value):
       g.mode = value
       g.click = True

    def btn_change_click(self,value):
        g.keymode = value
        g.mode = 11
        g.click = True
        if g.keymode == 0:
            g.key_val = str(g.PID_SP)
        elif g.keymode == 1:
            g.key_val = str(g.PID_Kp)
        elif g.keymode == 2:
            g.key_val = str(g.PID_Ti)
        elif g.keymode == 3:
            g.key_val = str(g.PID_Td)


class BuilderKeyboardPage(Builder):

    def build_gui(self):

        self.btn_1 = gui.Button('1',width=40,height=40)
        self.btn_2 = gui.Button('2',width=40,height=40)
        self.btn_3 = gui.Button('3',width=40,height=40)
        self.btn_4 = gui.Button('4',width=40,height=40)
        self.btn_5 = gui.Button('5',width=40,height=40)
        self.btn_6 = gui.Button('6',width=40,height=40)
        self.btn_7 = gui.Button('7',width=40,height=40)
        self.btn_8 = gui.Button('8',width=40,height=40)
        self.btn_9 = gui.Button('9',width=40,height=40)
        self.btn_0 = gui.Button('0',width=40,height=40)
        self.btn_dot = gui.Button('.',width=40,height=40)

        self.btn_clear = gui.Button('Clear',width=50,height=40)
        self.btn_del = gui.Button('DEL',width=50,height=40)
        self.btn_cancel = gui.Button('Cancel',width=50,height=40)
        self.btn_ok = gui.Button('OK',width=50,height=40)

        self.btn_1.connect(gui.CLICK,self.keyCallback,1)
        self.btn_2.connect(gui.CLICK,self.keyCallback,2)
        self.btn_3.connect(gui.CLICK,self.keyCallback,3)
        self.btn_4.connect(gui.CLICK,self.keyCallback,4)
        self.btn_5.connect(gui.CLICK,self.keyCallback,5)
        self.btn_6.connect(gui.CLICK,self.keyCallback,6)
        self.btn_7.connect(gui.CLICK,self.keyCallback,7)
        self.btn_8.connect(gui.CLICK,self.keyCallback,8)
        self.btn_9.connect(gui.CLICK,self.keyCallback,9)
        self.btn_0.connect(gui.CLICK,self.keyCallback,0)

        self.btn_dot.connect(gui.CLICK,self.keyCallback,10)
        self.btn_clear.connect(gui.CLICK,self.keyCallback,11)
        self.btn_del.connect(gui.CLICK,self.keyCallback,12)
        self.btn_cancel.connect(gui.CLICK,self.keyCallback,13)
        self.btn_ok.connect(gui.CLICK,self.keyCallback,14)

        self.lbl = gui.Label()
        self.lbl.set_text(g.key_val)
        self.lbl_prefix = gui.Label()
        if g.keymode == 0:
           self.lbl_prefix.set_text('SP:')
        elif g.keymode == 1:
           self.lbl_prefix.set_text('Kp:')
        elif g.keymode == 2:
           self.lbl_prefix.set_text('Ti:')
        elif g.keymode == 3:
           self.lbl_prefix.set_text('Td:')


        self.page.tr()
        self.page.td(self.lbl_prefix)
        self.page.td(self.lbl,height=35,colspan=3)
        self.page.tr()
        self.page.td(self.btn_7,width=60,height=45)
        self.page.td(self.btn_8,width=60,height=45)
        self.page.td(self.btn_9,width=60,height=45)
        self.page.td(self.btn_clear)
        self.page.tr()
        self.page.td(self.btn_4,width=60,height=45)
        self.page.td(self.btn_5,width=60,height=45)
        self.page.td(self.btn_6,width=60,height=45)
        self.page.td(self.btn_del)
        self.page.tr()
        self.page.td(self.btn_1,width=60,height=45)
        self.page.td(self.btn_2,width=60,height=45)
        self.page.td(self.btn_3,width=60,height=45)
        self.page.td(self.btn_cancel)
        self.page.tr()
        self.page.td(self.btn_0,width=50,height=45)
        self.page.td(self.btn_dot,width=50,height=45)
        self.page.td(gui.Spacer(50,45))
        self.page.td(self.btn_ok)

    def keyCallback(self, value):
        if int(value) < 10 :
            #print str(value)
            g.key_val = g.key_val + str(value)
            self.lbl.set_text(g.key_val)
        elif int(value) == 10 : #dot
            g.key_val = g.key_val + '.'
            self.lbl.set_text(g.key_val)
        elif int(value) == 11 : #Clear
            g.key_val = ''
            self.lbl.set_text(g.key_val)
        elif int(value) == 12 : #DEL
            g.key_val = g.key_val[:-1]
            self.lbl.set_text(g.key_val)
        elif int(value) == 13 : #Cancel
            g.mode = 10
            g.click = True
        elif int(value) == 14 : #OK
            if g.key_val == '':
                g.key_val = '0'

            if g.keymode == 0:
                g.PID_SP = float(g.key_val)
            elif g.keymode == 1:
                g.PID_Kp = float(g.key_val)
            elif g.keymode == 2:
                g.PID_Ti = float(g.key_val)
            elif g.keymode == 3:
                g.PID_Td = float(g.key_val)

            g.mode = 10
            g.click = True


# Product
class Page(gui.Table):

   def __init__(self):
      gui.Table.__init__(self)
      self.width=320
      self.height=240

