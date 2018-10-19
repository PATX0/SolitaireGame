# 1 PROJETO DE INTELIGENCIA ARTIFIAL
# GRUPO 88
# Rodrigo Lima nr 83559
# Tiago Soares nr 78658

import copy
from search import *


# TAI color
# sem cor = 0
# com cor > 0
def get_no_color():
	return 0
def no_color (c):
	return c == 0
def color (c):
	return c > 0

# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
	return (l, c)
def pos_l (pos):
	return pos[0]
def pos_c (pos):
	return pos[1]

def board_find_groups(board):
	nr_lines = len(board)
	nr_columns = len(board[0])
	list_of_groups = []
	positions_vector = []
	# generate the mapping of the board as positions in positions_vector
	for lines in range(0, nr_lines):
		for columns in range(0, nr_columns):
			position = make_pos(lines, columns)
			positions_vector.append(position)

	while(positions_vector != []):
		a_group = []
		counter = 0
		position = positions_vector[0]
		while(board[pos_l(position)][pos_c(position)] == 0):
			counter += 1
			position = positions_vector[counter]
		a_group.append(position)
		positions_vector, a_group = recursive_nearby_search(position, positions_vector, board, a_group)
		list_of_groups.append(a_group)

	return list_of_groups

# For a given position, tries all optionss to progress
def recursive_nearby_search(position, positions_vector, board, a_group):
	positions_vector.remove(position)
	# a cima
	if make_pos(pos_l(position)-1, pos_c(position)) in positions_vector:
		if board[pos_l(position)-1][pos_c(position)] == board[pos_l(position)][pos_c(position)]:
			new_position = make_pos(pos_l(position)-1, pos_c(position))
			a_group.append(new_position)
			recursive_nearby_search(new_position, positions_vector, board, a_group)
	# a baixo
	if make_pos(pos_l(position)+1, pos_c(position)) in positions_vector:
		if board[pos_l(position)+1][pos_c(position)] == board[pos_l(position)][pos_c(position)]:
			new_position = make_pos(pos_l(position)+1, pos_c(position))
			a_group.append(new_position)
			recursive_nearby_search(new_position, positions_vector, board, a_group)
	# a esquerda
	if make_pos(pos_l(position), pos_c(position)-1) in positions_vector:
		if board[pos_l(position)][pos_c(position)-1] == board[pos_l(position)][pos_c(position)]:
			new_position = make_pos(pos_l(position), pos_c(position)-1)
			a_group.append(new_position)
			recursive_nearby_search(new_position, positions_vector, board, a_group)
	# a direita
	if make_pos(pos_l(position), pos_c(position)+1) in positions_vector:
		if board[pos_l(position)][pos_c(position)+1] == board[pos_l(position)][pos_c(position)]:
			new_position = make_pos(pos_l(position), pos_c(position)+1)
			a_group.append(new_position)
			recursive_nearby_search(new_position, positions_vector, board, a_group)

	return positions_vector, a_group


def board_remove_group(board, group):
	#
	# A copy of the current state of the board is made, later updated and saved
	board_copy = copy.deepcopy(board)

	# First, fill the group cells with 0's
	for p in group:
		line, column = p
		board_copy[line][column] = 0

	# Second, fill the gaps in the affected columns
	# by compacting vertically from top to bottom
	for line in range(0, len(board_copy)):
		for column in range(0, len(board_copy[0])):
			if board_copy[line][column] == 0:
				for i in range(line, 0, -1):
					board_copy[i][column] = board_copy[i-1][column]
				board_copy[0][column] = 0

	# shift columns to the left if any column is empty
	#
	for i in range(len(board_copy[0])-1, -1, -1):
		if board_copy[len(board_copy)-1][i] == 0:
			for j in range(0, len(board_copy)):
				for k in range(i, len(board_copy[0])-1):
					board_copy[j][k] = board_copy[j][k+1]
				board_copy[j][len(board_copy[0])-1] = 0

	# update and save board to print
	board = board_copy
	return board

class sg_state:
	def __init__ (self, b):
		self.board = b

	def __lt__(self, other):
		return len(board_find_groups(self.board)) < len(board_find_groups(other.board))

class same_game(Problem):
	""" Models a Same Game problem as a satisfaction problem.
	A solution cannot have pieces left on the board."""

	def __init__(self, board):
		self.initial = sg_state(board)

	def actions(self, state):
		result = board_find_groups(state.board)
		# eliminate the groups with one cell
		for i in range(len(result)):
			if len(result[i]) == 1:
				result.remove(result[i])
		return result

	def result(self, state, action):
		return board_remove_group(state.board, action)

	def goal_test(self, state):
		return state.board[len(board)-1][0] == 0

	def path_cost(self, c, state1, action, state2):
		return 1

	def h(self, node):
		"""Needed for informed search."""