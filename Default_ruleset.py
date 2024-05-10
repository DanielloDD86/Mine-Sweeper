from random import randint
import Stack as S

class TILE:

    def __init__(self):
        """-2 initial tile - temporary,-1 = mined, 0 = Empty, 1-8 = no of mines near"""
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
        self.running = True
        self.__size = size
        self.__n_mines = n_mines
        self.__board = self.board_maker()
        self.mine_placer(n_mines)
        self.number_placer()
        self.__temp_board = self.__board
        self.first_tile((5,4))
        #self.solvable = self.solver()
        self.print_board()

    def get_board(self):
        return self.__board

    def board_maker(self):
        board = []
        for y in range(self.__size[1]):
            layer = []
            for x in range(self.__size[0]):
                layer.append(TILE())
            board.append(layer)
        return board

    def mine_placer(self,n_mines):
        total_tiles = self.__size[0]*self.__size[1]
        mines_placed = 0
        while mines_placed < n_mines:
            chosen = randint(0,total_tiles-1)
            chosen_cord = (chosen//self.__size[1],chosen%self.__size[1])
            if self.__board[chosen_cord[1]][chosen_cord[0]].get_mines() != -1 and self.__board[chosen_cord[1]][chosen_cord[0]].get_mines() != -2:
                self.__board[chosen_cord[1]][chosen_cord[0]].set_mines(-1)
                mines_placed += 1

    def number_placer(self):
        for y,row in enumerate(self.__board):
            for x, item in enumerate(row):
                if item.get_mines() != -1:
                    no_mines = 0
                    for i in range(-1,2):
                        for o in range(-1,2):
                            if i == 0 and o == 0:
                                pass
                            elif y+i < 0 or y+i > self.__size[1]-1:
                                pass
                            elif x+o < 0 or x+o > self.__size[0]-1:
                                pass
                            else:
                                if self.__board[y+i][x+o].get_mines() == -1:
                                    no_mines += 1
                    item.set_mines(no_mines)

    def first_tile(self,guess):
        if self.__board[guess[1]][guess[0]].get_mines() == -1:
            self.__board[guess[1]][guess[0]].set_mines(-2)
            self.mine_placer(1)
            self.number_placer()
        self.guess(guess)

    def guess(self,guess):
        result = self.__board[guess[1]][guess[0]].reveal()
        if result == True:
            self.running = False
        else:
            stack = S.Stack(18446744073709551615)
            stack.push((self.__board[guess[1]][guess[0]],guess))
            visited = []
            discovered = [self.__board[guess[1]][guess[0]]]
            while stack.is_empty() == False:
                #print(stack)
                node = stack.peek()
                stack.pop()
                
                for i in range(-1,2):
                    for o in range(-1,2):
                        if i == 0 and o == 0:
                            pass
                        elif node[1][1]+i < 0 or node[1][1]+i > self.__size[1]-1:
                            pass
                        elif node[1][0]+o < 0 or node[1][0]+o > self.__size[0]-1:
                            pass
                        else:
                            print(self.__board[node[1][1]+i][node[1][0]+o].get_mines())
                            if self.__board[node[1][1]+i][node[1][0]+o].get_mines() != -1:
                                self.__board[node[1][1]+i][node[1][0]+o].reveal()
                            if self.__board[node[1][1]+i][node[1][0]+o] not in discovered and self.__board[node[1][1]+i][node[1][0]+o].get_mines() == 0:
                                discovered.append(self.__board[node[1][1]+i][node[1][0]+o])
                                stack.push((self.__board[node[1][1]+i][node[1][0]+o],(node[1][0]+o,node[1][1]+i)))
                visited.append(node[0])


        


                            
    def solver(self):
        moves_in_turn = 1
        while moves_in_turn != 0:
            moves_in_turn = 0
            for y,row in enumerate(self.__board):
                for x, item in enumerate(row):
                    if item.get_reveal() == True:
                        no_mines_found = 0
                        mystery_tiles = 0
                        no_mines = item.get_mines()
                        for i in range(-1,2):
                            for o in range(-1,2):
                                if i == 0 and o == 0:
                                    pass
                                elif y+i < 0 or y+i > self.__size[1]-1:
                                    pass
                                elif x+o < 0 or x+o > self.__size[0]-1:
                                    pass
                                else:
                                    if self.__board[y+i][x+o].get_flag() == True:
                                        no_mines_found += 1
                                    elif self.__board[y+i][x+o].get_reveal() == False:
                                        mystery_tiles +=1
                        if no_mines_found < no_mines:
                            if no_mines - no_mines_found == mystery_tiles:
                                for i in range(-1,2):
                                    for o in range(-1,2):
                                        if i == 0 and o == 0:
                                            pass
                                        elif y+i < 0 or y+i > self.__size[1]-1:
                                            pass
                                        elif x+o < 0 or x+o > self.__size[0]-1:
                                            pass
                                        else:
                                            if self.__board[y+i][x+o].get_flag() == False and self.__board[y+i][x+o].get_reveal() == False:
                                                self.__board[y+i][x+o].reveal()
                                                moves_in_turn+=1


        return True


    def print_board(self):
        for y in self.__board:
            for x in y:
                print("(",x.get_mines(),",",x.get_reveal(),end="),")
            print()
                

#e = GAME((10,8),5)

