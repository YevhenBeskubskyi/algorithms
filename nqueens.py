def is_safe(i, j, board):
	for r in range(len(board)):
		for c in range(len(board)):
			if board[r][c] == 'q' and r == i and c != j:
				return False
			if board[r][c] == 'q' and r != i and c == j:
				return False
			if board[r][c] == 'q' and r + c == i + j:
				return False
			if board[r][c] == 'q' and r - c == i - j:
				return False
	return True

def place_queens(n, board):
	if n == len(board):
		return True
	for i in range(len(board)):
		if is_safe(i, n, board):
			board[i][n] = 'q'
			if place_queens(n+1, board):
				return True
		board[i][n] = '-'
	return False

def place_queens_test(board):
	place_queens(0, board)
	for row in board:
		print(' '.join(row))
	print('-' * (len(board) * 2 - 1))

x = int(input('enter a board size: '))
board = [['-'] * x for i in range(x)]
place_queens_test(board)
