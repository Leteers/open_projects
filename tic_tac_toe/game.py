import random
import tic_tac_toe.database as database

class game_itself:
    move_counter = 0
    grid = list()
    game_set = ['O', 'X']

    def __init__(self) -> None:
        for i in range(3):
            self.grid.append([None, None, None])
        self.move(None)

    def move(self, prev):
        if(prev == None):
            move_counter = 1
            return(random.choice(self.game_set))
        else:
            move_counter += 1
            return(self.game_set[len(self.game_set)-self.game_set.index(prev)-1])

    def is_over(self):
        if(self.move_counter == 9 and self.check_position() == False):
            return(True)
        elif(self.check_position() in self.game_set):
            return(True)
        else:
            return(False)

    def check_position(self):
        if self.move_counter >= 5:
            for i in range(len(self.grid)):
                if(self.grid[i][0] == self.grid[i][1] == self.grid[i][2]):
                    return(self.grid[i][0])
                elif(self.grid[0][i] == self.grid[1][i] == self.grid[2][i]):
                    return(self.grid[0][i])
                elif(self.grid[0][0] == self.grid[1][1] == self.grid[2][2]):
                    return(self.grid[0][0])
                elif(self.grid[2][0] == self.grid[1][1] == self.grid[0][2]):
                    return(self.grid[2][0])
                else:
                    return(False)
        else:
            return(False)

    def add_move(self, position, simbol):
        self.grid[int((position-1)/3),((position-1)//3)]=simbol

min = 5
