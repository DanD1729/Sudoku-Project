
import math,random

class SudokuGenerator:

	def __init__(self, row_length, removed_cells):
		self.row_length = row_length
		self.box_length = int(math.sqrt(row_length))
		self.removed_cells = removed_cells
		self.board = []
		for i in range(row_length):
			self.board.append([0]*row_length)

	def get_board(self):
		return self.board

	def valid_in_row(self,row,num):
		return not(num in self.board[row])


	def valid_in_col(self, col, num):
		return not(num in [self.board[i][col] for i in range(self.row_length)])

	def valid_in_box(self, row_start, col_start, num):
		box = []
		for i in range(row_start, row_start+3):
			for j in range(col_start,col_start+3):
				if self.board[i][j] == num:
					return False
		return True

	def is_valid(self,row,col,num):

		rowb = row//3 * 3
		colb = col//3 * 3
		return (self.valid_in_box(rowb,colb,num) and self.valid_in_row(row,num) and self.valid_in_col(col,num))

	def fill_box(self,row_start,col_start):
		possible = random.randint(1, 9)
		used = []
		for i in range(row_start, row_start+3):
			for j in range(col_start,col_start+3):
				while possible in used:
					possible = random.randint(1, 9)
				used.append(possible)
				self.board[i][j] = possible

	def fill_diagonal(self):
		for i in range(3):
			self.fill_box(i*3,i*3)

	def fill_remaining(self, row, col):
		if (col >= self.row_length and row < self.row_length - 1):
			row += 1
			col = 0
		if row >= self.row_length and col >= self.row_length:
			return True
		if row < self.box_length:
			if col < self.box_length:
				col = self.box_length
		elif row < self.row_length - self.box_length:
			if col == int(row // self.box_length * self.box_length):
				col += self.box_length
		else:
			if col == self.row_length - self.box_length:
				row += 1
				col = 0
				if row >= self.row_length:
					return True    
		for num in range(1, self.row_length + 1):
			if self.is_valid(row, col, num):
				self.board[row][col] = num
				if self.fill_remaining(row, col + 1):
					return True
				self.board[row][col] = 0

		return False

	def fill_values(self):
		self.fill_diagonal()
		self.fill_remaining(0, self.box_length)

	def remove_cells(self):
		n = self.removed_cells
		used = []
		coords = (random.randint(0, 8),random.randint(0, 8))
		for i in range(n):
			while coords in used:
				coords = (random.randint(0, 8),random.randint(0, 8))
			used.append(coords)
			self.board[coords[0]][coords[1]] = 0

def generate_sudoku(size, removed):
	sudoku = SudokuGenerator(size, removed)
	sudoku.fill_values()
	board = sudoku.get_board()
	sudoku.remove_cells()
	board = sudoku.get_board()
	return board


		