
def modify_cell(row,column,board,new):
	if board[row][column]==0:
		board[row][column]=new
def printcodeboard(board):
	for i in range(9):
		for j in range(9):
			print(str(board[i][j]), end=' ')
			if (j+1)%3==0:
				print('|',end='')
		print()
		if (i+1)%3==0:
			print('-'*21)


def valid_in_row(board,row,num):
	return not(num in board[row])


def valid_in_col(board, col, num):
	return not(num in [board[i][col] for i in range(9)])

def valid_in_box(board, row_start, col_start, num):
	box = []
	for i in range(row_start, row_start+3):
		for j in range(col_start,col_start+3):
			if board[i][j] == num:
				return False
	return True

def is_valid(board,row,col,num):

	rowb = row//3 * 3
	colb = col//3 * 3
	return (valid_in_box(board,rowb,colb,num) and valid_in_row(board,row,num) and valid_in_col(board,col,num))
