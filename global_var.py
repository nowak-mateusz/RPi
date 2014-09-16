import os
import pygame
from pygame.locals import *

#pygame.init()

dataPath = os.path.join(os.getcwd(),'data')

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

screenSurface = None

digitalFont = '/home/pi/projects/RPi/data/fonts/SFDigitalReadout-Medium.ttf'#dataPath + '/fonts/SFDigitalReadout-Medium.ttf'

mode = 3
click = True

TEMP_SENSOR = None

DAC = None
I2C_port = 0x60
DAC_value = 0

PID_start = 0

PID_SP = 1.0
PID_Kp = 1.0
PID_Ti = 1.0
PID_Td = 1.0

keymode = 0
key_val = 'aa'
