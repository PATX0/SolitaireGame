#! /usr/bin/python3
# Grupo 88 - Tiago Soares 78658; Goncalo Correia 83897;
# Projecto 1 IA 18-19

from search import *
from copy import *


# ______________________________________________________________________________

# TAI content

def c_peg():
	return "O"

def c_empty():
	return "_"

def c_blocked():
	return "X"

def is_peg(e):
	return e == c_peg()

def is_empty(e):
	return e == c_empty()

def is_blocked(e):
	return e == c_blocked()


# TAI pos
# Tuplo (l, c)
def make_pos(l, c):
	return (l, c)

def pos_l(pos):
	return pos[0]

def pos_c(pos):
	return pos[1]

# TAI move
# Lista [p_initial, p_final]
def make_move(i, f):
	return [i, f]
def move_initial(move):
	return move[0]
def move_final(move):
	return move[1]

# board_moves(board): Movimentos possiveis no tabuleiro
def board_moves(board):
	n_l = len(board)
	n_c = len(board[0])
	list_pos = []
	# generate the mapping of the board as positions in list_pos
	for l in range(0, n_l):
		for c in range(0, n_c):
			position = make_pos(l, c)
			list_pos.append(position)
	return list_pos

# board_perform_move(board): Movimentos possiveis no tabuleiro
def board_perform_move(board, move):
	board_cpy = deepcopy(board)
	return board_cpy


def countPegs(board):
	count = 0
	nr_l = len(board)
	nr_c = len(board[0])
	for l in range(0, nr_l):
		for c in range(0, nr_c):
			if is_peg(board[l][c]):
				count += 1
	return count

def countEmpty(board):
	count = 0
	nr_l = len(board)
	nr_c = len(board[0])
	for l in range(0, nr_l):
		for c in range(0, nr_c):
			if is_empty(board[l][c]):
				count += 1
	return count


class sol_state:

	def __init__(self, board):
		self.board = board

	def __lt__(self, other):
		return len(board_moves(self.board)) > len(board_moves(other.board))

class solitaire(Problem):
#Models a Solitaire problem as a satisfaction problem.
#A solution cannot have more than 1 peg left on the board.
	def __init__(self, board):
		self.initial = sol_state(board)

	#def actions(self, state):
	#	result = board_moves(state.board)

	def result(self, state, action): #executar move(action) no estado e devolver o novo estado
		return board_perfome_move(state.board, action)

	def goal_test(self, state): #state e solucao se so tiver 1 peca
		return countPegs(state.board) == 1

	def path_cost(self, c, state1, action, state2):
		return c+1


#heuristicas para procura, recolher varias informacoes relevantes para melhorar a performance da procura(distancia, vizinhos, pos vazias...)
	#def h(self, node): 
#"""Needed for informed search."""
	#state = node.state
	
#board = [["O","O","O","X"], ["O","O","O","O"], ["O","_","O","_"], ["O","O","O","O"]]
#board = [[c_peg(), c_peg(), c_peg(), c_blocked()], [c_peg(), c_peg(), c_peg(), c_peg()], [c_peg(), c_empty(), c_peg(), c_empty()], [c_peg(), c_peg(), c_peg(), c_peg()]]

#game = solitaire(board)
#p = InstrumentedProblem(game)
#resultD = depth_first_tree_search(p)
#resultG = greedy_best_first_graph_search(p, p.h)
#resultA = astar_search(p)

#resultD.solution()
#resultD.path()









