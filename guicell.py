from drawnbutton import *
from auxiliary_functions import *

class CeldaDrawn(GameButtonDrawn):

	RED = (255,0,0)
	CELDA_SIZE = 32

	def __init__(self,window,location,size,label,value,position,board,sketched):
		
		GameButtonDrawn.__init__(self,window,location,size,label)
		self.value = value	
		self.position = position
		self.board = board
		self.sketched = sketched
		self.editable = False
		if self.value == 0:
			self.editable = True
		
		font = pygame.font.SysFont(None,20)
		width_label, height_label = font.size('0')

		s_label_loc = (self.location[0]+width_label//2,self.location[1]+height_label//8)

		self.sketched_label = SimpleTexto(window, s_label_loc, str(sketched), CeldaDrawn.RED,20)
		




	def handlePress(self, evento):
		if evento.type not in (MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION):
			return False

		touchingButton = self.rect_button.collidepoint(evento.pos)
		
		if self.state == 'presionado': 
			if touchingButton:
				if evento.type == pygame.MOUSEBUTTONDOWN:
					self.state = 'apagado'
					return False
				else:
					return True
			else:
				return True
		elif self.state == 'apagado':
			if touchingButton:
				if evento.type == pygame.MOUSEBUTTONDOWN:
					self.state = 'presionado'
					return True
				else:
					return False
			else:
				return False

	def controlaTeclado(self,evento):

		if evento.type == pygame.KEYDOWN and self.state == 'presionado':
			tecla = pygame.key.name(evento.key)
			if tecla.isdigit() and len(tecla) == 1 and (self.value == 0 or self.editable):
				self.sketched = tecla
				return True
			elif evento.key == K_RETURN and self.sketched != '':
				self.value = int(self.sketched)
				self.sketched = ''
				return True
			return False
		else:
			return False

	def updateCell(self,evento):
		if self.state == 'presionado':
			if self.controlaTeclado(evento):
				modify_cell(self.position[0],self.position[1],self.board,self.value)
				self.button_label.setValue(str(self.value))
				self.button_label_down.setValue(str(self.value))
				self.sketched_label.setValue(self.sketched)
			


	def draw(self):
		if self.state == 'presionado':
			pygame.draw.rect(self.window,GameButtonDrawn.BLUE,self.rect_button,2)
			self.button_label_down.draw()
			self.sketched_label.draw()
		else:
			pygame.draw.rect(self.window,GameButtonDrawn.BLACK,self.rect_button,2)
			self.button_label.draw()
			self.sketched_label.draw()
		