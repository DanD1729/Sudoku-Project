import pygame
from pygame.locals import *
from sudoku_generator import *
from auxiliary_functions import *
from guicell import *

from check_winner import *
BLACK = (0,0,0)
DIMGRAY = (105,105,105)
class Board():
	def __init__(self,window,location,removed,codeboard = ''):
		self.board = []
		self.window = window
		self.location = location
		self.width = CeldaDrawn.CELDA_SIZE
		self.copy = location
		self.mover = self.width
		self.modified = []
		self.blank = []
		if codeboard == '':
			self.boardcode = generate_sudoku(9, removed)
		else:
			self.boardcode = codeboard 
		blocation = self.location
		self.activecells = []

		for i in range(9):
			row = []
			for j in range(9):
				cell = CeldaDrawn(self.window,blocation,(32,32),str(self.boardcode[i][j]),self.boardcode[i][j],[i,j],self.boardcode,'')
				if cell.value == 0:
					self.blank.append(cell.position)
				row.append(cell)
				if (j+1)%3 == 0:
					blocation = (blocation[0]+self.mover+1,blocation[1])
				else:
					blocation = (blocation[0]+self.mover,blocation[1])

			self.board.append(row)
			blocation = (self.copy[0],blocation[1])
			if (i+1)%3 == 0:
				blocation = (blocation[0],blocation[1] + self.mover+1)
			else:
				blocation = (blocation[0],blocation[1] + self.mover)
			


	def draw(self):
		n = 3
		for i in range(1,n):
			x = (20+96*(i%n)+((i-1)%(n-1)),20)
			y = (20+96*(i%n)+((i-1)%(n-1)),20+32*9+1)
			pygame.draw.line(self.window, DIMGRAY, x, y,1)
			pygame.draw.line(self.window, DIMGRAY, x[::-1], y[::-1],1)
			
		for i in range(9):
			for j in range(9):
				self.board[i][j].draw()

	def check_status(self,evento):
		for i in range(9):
			for j in range(9):
				click = self.board[i][j].handlePress(evento)

				previous = self.activecells
				if click:
					self.activecells = self.board[i][j]
					if self.activecells != previous and previous!=[]:
						previous.state = 'apagado'
				if self.activecells != []:
					if self.activecells.state =='apagado':
						self.activecells = []

				
				old_val = self.board[i][j].value
				self.board[i][j].updateCell(evento)
				if old_val != self.board[i][j].value:
					if self.board[i][j].position not in self.modified:
						self.modified.append(self.board[i][j].position)
					if self.board[i][j].value == 0:
						self.modified.remove(self.board[i][j].position)
		
		self.keyboardcontrol(evento)
		if len(self.blank) == len(self.modified):
			return check_winner(self.boardcode)
					
	def keyboardcontrol(self,evento):
			if evento.type == pygame.KEYDOWN and self.activecells != []:
				position = self.activecells.position
				
				if evento.key == K_UP:
					self.activecells.state = 'apagado'
					self.board[position[0]-1][position[1]].state = 'presionado'
					self.activecells = self.board[position[0]-1][position[1]]
				elif evento.key == K_DOWN:
					self.activecells.state = 'apagado'
					self.board[(position[0]+1)%9][position[1]].state = 'presionado'
					self.activecells = self.board[(position[0]+1)%9][position[1]]
				elif evento.key == K_LEFT:
					self.activecells.state = 'apagado'
					self.board[position[0]][(position[1]-1)%9].state = 'presionado'
					self.activecells = self.board[position[0]][(position[1]-1)%9]
				elif evento.key == K_RIGHT:
					self.activecells.state = 'apagado'
					self.board[position[0]][(position[1]+1)%9].state = 'presionado'
					self.activecells = self.board[position[0]][(position[1]+1)%9]
					