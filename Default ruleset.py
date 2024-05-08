from random import randint

class TILE:

    def __init__(self):
        """-1 = mined, 0 = Empty, 1-8 = no of mines near"""
        self.__mines = 0
        self.__revealed = False
        self.__flagged = False

    def get_mines(self):
        return self.__mines
    
    def set_mines(self,mines):
        self.__mines = mines

    def flag(self):
        self.__flagged = not self.__flagged

    def get_flag(self):
        return self.__flagged

    def reveal(self):
        self.__revealed = True
        if self.__mines == -1:
            return True
        return False
    
    def get_reveal(self):
        return self.__revealed
    
class GAME:

    def __init__(self,size,n_mines):
        self.__size = size
        self.__n_mines = n_mines
        self.__board = self.board_maker(size)
        self.mine_placer(size,n_mines)
        self.number_placer(size)
        self.print_board()

    def get_board(self):
        return self.__board

    def board_maker(self,size):
        board = []
        for y in range(size[1]):
            layer = []
            for x in range(size[0]):
                layer.append(TILE())
            board.append(layer)
        return board

    def mine_placer(self,size,n_mines):
        total_tiles = size[0]*size[1]
        mines_placed = 0
        while mines_placed < n_mines:
            chosen = randint(0,total_tiles-1)
            chosen_cord = (chosen//size[1],chosen%size[1])
            if self.__board[chosen_cord[1]][chosen_cord[0]].get_mines() != -1:
                self.__board[chosen_cord[1]][chosen_cord[0]].set_mines(-1)
                mines_placed += 1

    def number_placer(self,size):
        for y,row in enumerate(self.__board):
            for x, item in enumerate(row):
                if item.get_mines() != -1:
                    no_mines = 0
                    for i in range(-1,2):
                        for o in range(-1,2):
                            if i == 0 and o == 0:
                                pass
                            elif y+i < 0 or y+i > size[1]-1:
                                pass
                            elif x+o < 0 or x+o > size[0]-1:
                                pass
                            else:
                                if self.__board[y+i][x+o].get_mines() == -1:
                                    no_mines += 1
                    item.set_mines(no_mines)
                            



    def print_board(self):
        for y in self.__board:
            for x in y:
                print(x.get_mines()," ,",end="")
            print()
                

e = GAME((10,8),20)

