'''
Shambhu Thapa 10677794

Othello.py

'''

class Othello:

	directions=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

	def __init__(self,rows,columns,turn,top_left_corner,board):
		"default constructor"
		self.__rows = rows
		self.__columns = columns
		self.__turn = turn
		self.__top_left_corner = top_left_corner
		self.__board = board
		#self.__winning_criteria = winning_criteria

	def get_rows(self):
		"returns number of rows in board"
		return self.__rows

	def get_columns(self):
		"returns number of columns in board"
		return self.__columns

	def print_board(self):
		"prints the board"
		for i in range(0,len(self.__board)):
			for j in range(0,len(self.__board[0])):
				print(self.__board[i][j], end=' ')
			print("")




        def _game_board(self):
                if(self.__top_left_corner()== 'W'):
                        opposite = 'B'
                else:
                        opposite = 'W'
                board = []

                for i in range(self.__rows):
                        board.append([''] * self.__columns)
                board[int(self.__rows/2)-1][int(self.__columns/2)-1]=self.__top_left_corner
                board[int((self.__rows/2))][int((self.__columns/2))]=self.__top_left_corner
                board[int(self.__rows/2)-1][int(self.__columns/2)]=opposite
                board[int((self.__row/2))][int((self.__columns/2)-1)]=opposite

                self._board=board

                
                

	def get_opposite_of(self,color):
		"return opposite color value, here B & W are opposites"
		if color == "B":
			return "W"
		else:
			return "B"

	def get_count(self, color):
		"returns number of cells occupied by the specific colured disc"
		count = 0
		for i in range(0,self.__rows):
			for j in range(0,self.__columns):
				if self.__board[i][j] == color:
					count += 1
		return count



	 def _require_valid_row_number(self,row):
                if type(row)!= int or not self._is_valid_row_number(row):
                     raise ValueError('row_number must be int between 0 and {}'.format(len(board)))

        def _is_valid_row_number(self,row) -> bool:
                '''Returns True if the given column number is valid; returns False otherwise'''
                return 0 <= row < len(self._board)


	def in_bound(self, i, j):
		"checks if the index belongs to the array or it has gone out of range from either side"
		if((i >=0 and i < len(self.__board)) and (j >=0 and j < len(self.__board[0]))):
			return True
		else:
			return False

	def get_Moves(self,i,j):
		"Checks if a move can be made to this cell given by i,j for the current player given by turn variable"
		valid_boxes = []
		for a,b in self.directions:
			x,y = i,j
			x += a
			y += b
			if(self.in_bound(x,y) and self.__board[x][y] == self.get_opposite_of(self.__turn)):
				x += a
				y += b

				while (self.in_bound(x,y) and (self.__board[x][y] == self.get_opposite_of(self.__turn))):
					x+=a
					y+=b

				if (self.in_bound(x,y) and self.__board[x][y] == self.__turn):
					while True:
						x -= a
						y -= b
						valid_boxes.append([x,y])
						if x==i and y==j:
							break
		return valid_boxes


	def get_winner(self):
		"returns the winner based on winning criteria"
		if(self.__winning_criteria == ">"):
			if (self.get_count("B") > self.get_count("W")):
				return "B"
			elif (self.get_count("B") == self.get_count("W")):
				return "NONE"
			else:
				return "W"
		else:
			if (self.get_count("B") < self.get_count("W")):
				return "B"
			elif (self.get_count("B") == self.get_count("W")):
				return "NONE"
			else:
				return "W"

	def is_empty(self):
		"tells if the board is empty or not"
		for x in range(0,len(self.__board)):
			for y in range(0,len(self.__board[0])):
				if self.__board[x][y] == ".":
					return True
				continue
		return False

	def switch_turn(self):
		"change the turn value to be the opposite of current value"
		self.__turn = self.get_opposite_of(self.__turn)

	def get_turn(self):
		"return whose current turn it is"
		return self.__turn

	def move(self, moves):
		"make a move(change the board with new piece and other players discs colour chnage too) post entry of valid move"
		for p,q in moves:
			self.__board[p][q] = self.__turn