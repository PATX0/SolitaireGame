#! /usr/bin/python3
# Grupo 56 - Tiago Soares 78658; Goncalo Correia 83897;
# Projecto 1 IA 18-19

from search import *
from copy import *
import time

# _____________________________________________________________________________________________________

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


# TAI board
def getContent(board, pos):
	return board[pos_l(pos)][pos_c(pos)]

def setContent(board, pos, content):
	board[pos_l(pos)][pos_c(pos)] = content
	return board

def removePegRight(board, pos, content):
	board[pos_l(pos)][pos_c(pos)+1] = content
	return board

def removePegLeft(board, pos, content):
	board[pos_l(pos)][pos_c(pos)-1] = content
	return board

def removePegUp(board, pos, content):
	board[pos_l(pos)-1][pos_c(pos)] = content
	return board

def removePegDown(board, pos, content):
	board[pos_l(pos)+1][pos_c(pos)] = content
	return board

# _____________________________________________________________________________________________________

# board_moves(board): Movimentos possiveis no tabuleiro
def board_moves(board):
	n_l = len(board)
	n_c = len(board[0])
	moves = []
	positions = map_positions_board(n_l, n_c, board) #lista de posicoes do board
	for pos in positions:
		l = pos_l(pos)
		c = pos_c(pos)
		if is_empty(board[l][c]): 
			neigh = getNeighbours(pos, board) #lista de vizinhos de pos com dist = 2
			for i in range(0, len(neigh)):
				aux_l = pos_l(neigh[i])
				aux_c = pos_c(neigh[i])
				if is_peg(board[aux_l][aux_c]):
					if aux_l < l:	#verifica se a peca a mover esta a esquerda da posicao vazia 
						if is_peg(board[l-1][c]): #verifica se a posicao entre ambas e uma peca valida
							moves.append(make_move(neigh[i], pos))

					if aux_l > l:	#verifica se a peca a mover esta a direita da posicao vazia
						if is_peg(board[l+1][c]):
							moves.append(make_move(neigh[i], pos))

					if aux_c < c:	#verifica se a peca a mover esta acima da posicao vazia
						if is_peg(board[l][c-1]):
							moves.append(make_move(neigh[i], pos))

					if aux_c > c: #verifica se a posicao a mover esta abaixo da posicao vazia
						if is_peg(board[l][c+1]):
							moves.append(make_move(neigh[i], pos))

	return moves


# board_perform_move(board): executa move no board, retirando a posicao entre move initial e final
def board_perform_move(board, move):
	boardcopy = deepcopy(board)
	moves = board_moves(board)
	#nr da linha e coluna das posicoes de move
	linit = pos_l(move_initial(move))
	lfinal = pos_l(move_final(move))
	cinit = pos_c(move_initial(move))
	cfinal = pos_c(move_final(move))
	if move in moves: #move valido
		if linit < lfinal: #verifica se o move e de cima para baixo
			boardcopy[linit+1][cinit] = c_empty() #remove peca abaixo da peca inicial
		
		if linit > lfinal: #verifica se o move e de baixo para cima
			boardcopy[linit-1][cinit] = c_empty() 

		if cinit < cfinal: #verifica se o move e da esquerda para a direita
			boardcopy[linit][cinit+1] = c_empty() 
	
		if cinit > cfinal: #verifica se o move e da direita para a esquerda
			boardcopy[linit][cinit-1] = c_empty() 
	         
		setContent(boardcopy, move_initial(move), c_empty())
		setContent(boardcopy, move_final(move), c_peg())
	else: #se move nao for valido 
		return board

	return boardcopy

# _____________________________________________________________________________________________________
# funcoes auxiliares

#def check_return_empty(list_pos, board):
#	res = []
#	for i in range(0, len(list_pos)):
#		l = pos_l(list_pos[i])
#		c = pos_c(list_pos[i])
#		if is_empty(board[l][c]):
#			res.append(list_pos[i])
#	return res
	
def countPegs(board):	#conta numero de pecas
	count = 0
	nr_l = len(board)
	nr_c = len(board[0])
	for l in range(0, nr_l):
		for c in range(0, nr_c):
			if is_peg(board[l][c]):
				count += 1
	return count

def countEmpty(board):	#conta posicoes vazias
	count = 0
	nr_l = len(board)
	nr_c = len(board[0])
	for l in range(0, nr_l):
		for c in range(0, nr_c):
			if is_empty(board[l][c]):
				count += 1
	return count

def getNeighbours(pos, board): #retorna lista com vizinhos a distancia = 2 para as 4 direcoes
	n_ls = len(board)
	n_cs = len(board[0])   
	l = pos_l(pos)
	c = pos_c(pos)
	res = []
	if l > 1: 	#garante que 2 posicoes a esquerda e uma posicao valida	
		res.append(make_pos(l-2, c))
	if l < n_ls-2:
		res.append(make_pos(l+2, c))    
	if c > 1:	#garante que 2 posicoes a baixo e uma posicao valida
		res.append(make_pos(l, c-2))
	if c < n_cs-2:
		res.append(make_pos(l, c+2))
	
	return sorted(res)



def map_positions_board(n_l, n_c, board):
	list_pos = []
	# generate the mapping of the board as positions in list_pos
	for l in range(0, n_l):
		for c in range(0, n_c):
			position = make_pos(l, c)
			list_pos.append(position)
	return list_pos


# _____________________________________________________________________________________________________
# classes

class sol_state:

	def __init__(self, board):
		self.board = board

	def __lt__(self, other):
		return countEmpty(self.board) < countEmpty(other.board)


class solitaire(Problem):
#Models a Solitaire problem as a satisfaction problem.
#A solution cannot have more than 1 peg left on the board.
	def __init__(self, board):
		self.initial = sol_state(board)

	def actions(self, state):
		moves = board_moves(state.board)
		#for move in moves:
		#	board_perform_move(state.board, move)
		return moves

	def result(self, state, action): #executar move(action) no estado e devolver o novo estado
		res = board_perform_move(state.board, action)
		return sol_state(res)
		
	def goal_test(self, state): #state e solucao se so tiver 1 peca
		return countPegs(state.board) == 1

	def path_cost(self, c, state1, action, state2):
		return c+1


#heuristicas para procura, recolher varias informacoes relevantes para melhorar a performance da procura(distancia, vizinhos, pos vazias...)
#	def h(self, node): 
#"""Needed for informed search."""
		#moves = board_moves(node.state.board)
		

# _____________________________________________________________________________________________________
# execution



