import pygame
from pygame.locals import *
from textoSimple import *
class GameButtonDrawn():

	BLUE = (0,0,255)
	BLACK = (0,0,0)
	GAINSBORO = (220,220,220)

	def __init__(self,window,location,size,label):

		self.window = window
		self.location = location
		self.size = size
		self.rect_button = pygame.Rect(self.location,self.size)

		font = pygame.font.SysFont(None,30)
		width_label, height_label = font.size(label)

		self.label_loc = ((location[0] + (size[0]-width_label)/2),(location[1] + (size[1]-height_label)/2))

		self.button_label = SimpleTexto(window, self.label_loc, label, GameButtonDrawn.BLACK,30)
		self.button_label_down = SimpleTexto(window, self.label_loc, label, GameButtonDrawn.BLUE,30)


		self.state = 'apagado'	

	def handlePress(self, evento):
		if evento.type not in (MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION):
			return False

		touchingButton = self.rect_button.collidepoint(evento.pos)

		if self.state == 'presionando' and evento.type == pygame.MOUSEBUTTONUP:
			self.state = 'apagado'
			return True
		elif self.state == 'apagado':
			if touchingButton:
				if evento.type == pygame.MOUSEBUTTONDOWN:
					self.state = 'presionando'
					return False
			else:
				return False

	def draw(self):
		if self.state == 'presionando':
			pygame.draw.rect(self.window,GameButtonDrawn.BLUE,self.rect_button,2)
			self.button_label_down.draw()
		else:
			pygame.draw.rect(self.window,GameButtonDrawn.BLACK,self.rect_button,2)
			self.button_label.draw()
	