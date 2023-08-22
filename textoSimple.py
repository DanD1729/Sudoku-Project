import pygame
from pygame.locals import *

class SimpleTexto():
	def __init__(self, window, location, valor, colorTexto, font_size):
		pygame.font.init()
		self.window = window
		self.location = location
		self.font_size = font_size
		self.font = pygame.font.SysFont(None,self.font_size)
		self.colorTexto = colorTexto
		self.text = None
		self.setValue(valor)
	def setValue(self,nuevo):
		if self.text == nuevo:
			return
		self.text = nuevo
		self.textSurface = self.font.render(self.text,True, self.colorTexto)

	def draw(self):
		self.window.blit(self.textSurface,self.location)

	def check_status(self,event):
		return None