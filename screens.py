import pygame
from pygame.locals import *
import sys

WHITE = (255, 255, 255)
BLACK = (0,0,0)

class Screen():

	def __init__(self,window,list_screen_objects):
		self.window = window
		self.screen_objects = list_screen_objects
		self.obj_states = {}

	def eventsScreen(self,event):
		self.obj_states = {}
		for object in self.screen_objects:
			check = object.check_status(event)
			self.obj_states[object] = check
		return self.obj_states

	def perFrameScreen(self):
		self.window.fill(WHITE)
		for object in self.screen_objects:
			object.draw()