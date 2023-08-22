from drawnbutton import *
import pygame
from pygame.locals import *
import sys

class Menu2():
	def __init__(self,window,name,buttonType,location,label_list):
		self.name = name
		self.types = [GameButtonDrawn]
		self.buttonType = buttonType
		self.label_list = label_list
		self.window = window
		self.location = location
		self.n = len(label_list)
		self.buttons = []
		self.w_win,self.h_win = self.window.get_size()
		self.states = {}
		menuw = self.w_win-2*location[0]
		but_w = int(menuw/(self.n+1))
		if self.n>1:
			self.move = int(but_w/(self.n-1))
		else:
			self.move = 0
			self.location = (int((self.w_win-but_w)/2),self.location[1])
		locb = self.location
		for i in range(self.n):
				self.buttons.append(self.types[self.buttonType](self.window,locb,((but_w),20),self.label_list[i]))
				locb = (locb[0] + self.move + but_w,locb[1])

	def draw(self):
		for i in range(self.n):
			self.buttons[i].draw()

	def check_status(self,evento):
		self.states = {}
		for i in range(self.n):
			self.states[self.label_list[i]] = self.buttons[i].handlePress(evento)
		return self.states
		