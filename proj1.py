# Projecto IA 18-19
# Grupo 88 - 78658; 

import search
import utils

# TAI content
def c_peg ():
	return "O"
def c_empty ():
	return "_"
def c_blocked ():
	return "X"
def is_empty (e):
	return e == c_empty()
def is_peg (e):
	return e == c_peg()
def is_blocked (e):
	return e == c_blocked()


# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
	return (l, c)
def pos_l (pos):
	return pos[0]
def pos_c (pos):
	return pos[1]

# TAI move
# Lista [p_initial, p_final]
def make_move (i, f):
	return [i, f]
def move_initial (move):
	return move[0]
def move_final (move):
	return move[1]

# board_moves(board): Movimentos possiveis no tabuleiro
def board_moves(board):
	new_board = board
	return new_board

# board_perform_move(board): Movimentos possiveis no tabuleiro
def board_perform_move(board, move):
	board_cpy = board
	return board_cpy




#class solitaire(Problem):
#"""Models a Solitaire problem as a satisfaction problem.
#A solution cannot have more than 1 peg left on the board."""
#def __init__(self, board):

#def actions(self, state):

#def result(self, state, action):

#def goal_test(self, state):

#def path_cost(self, c, state1, action, state2):

#def h(self, node):
#"""Needed for informed search."""









