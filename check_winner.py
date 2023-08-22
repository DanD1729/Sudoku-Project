def check_row(board):
    valid_row_count = 0
    for row in board:
        set_for_row = set(row)
        array_for_row = list(set_for_row)
        if len(array_for_row) == 9:
            valid_row_count += 1

    if valid_row_count == 9:
        return True

def check_column(board):
    valid_column_count = 0
    for index in range(9):
        column_list = []
        for row in board:
            column_list.append(row[index])
        set_for_column = set(column_list)
        array_for_column = list(set_for_column)
        if len(array_for_column) == 9:
            valid_column_count += 1

    if valid_column_count == 9:
        return True

def check_block(board, row_start, column_start):
    box_array = []
    row_range = row_start + 3
    column_range = column_start + 3
    for row in range(row_start, row_range):
        for column in range(column_start, column_range):
            box_array.append(board[row][column])
    set_for_block = set(box_array)
    array_for_block = list(set_for_block)

    if len(array_for_block) == 9:
        return True


def check_all_blocks(board):
    valid_block_count = 0
    if check_block(board, 0, 0) == True:
        valid_block_count += 1
    if check_block(board, 0, 3) == True:
        valid_block_count += 1
    if check_block(board, 0, 6) == True:
        valid_block_count += 1
    if check_block(board, 3, 0) == True:
        valid_block_count += 1
    if check_block(board, 3, 3) == True:
        valid_block_count += 1
    if check_block(board, 3, 6) == True:
        valid_block_count += 1
    if check_block(board, 6, 0) == True:
        valid_block_count += 1
    if check_block(board, 6, 3) == True:
        valid_block_count += 1
    if check_block(board, 6, 6) == True:
        valid_block_count += 1
    if valid_block_count == 9:
        return True

def check_winner(board):
    '''Returns True if you won. Returns False if you lost.'''
    if check_row(board) == True:
        if check_column(board) == True:
            if check_all_blocks(board) == True:
                return True

    return False