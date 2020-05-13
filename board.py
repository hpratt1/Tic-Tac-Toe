class Board:
    def __init__(self):
        self.layout = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    
    def display(self):
        print()
        for row in self.layout:
            print(row[0], row[1], row[2])
        print()
    
    def insert_X(self, row, col):
        self.layout[row][col] = 'X'
    
    def insert_O(self, row, col):
        self.layout[row][col] = 'O'
        
    def check_valid_move(self, row, col):
        layout = self.layout
        if (row >= 0) and (row <= 2) and (col >= 0) and (col <= 2):
            if (layout[row][col] == '-'):
                return True
            else:
                return False
        else:
            return False

    def check_full_board(self):
        if ('-' not in self.layout[0]) and ('-' not in self.layout[1]) and ('-' not in self.layout[2]):
            return True
        else:
            return False
    
    def check_winning_board(self):
        layout = self.layout
        for i in range(3):
            if (layout[i][0] != '-') and (layout[i][0] == layout[i][1]) and (layout[i][1] == layout[i][2]):
                return True
            if (layout[0][i] != '-') and (layout[0][i] == layout[1][i]) and (layout[1][i] == layout[2][i]):
                return True
        if (layout[0][0] != '-') and (layout[0][0] == layout[1][1]) and (layout[1][1] == layout[2][2]):
            return True
        elif (layout[0][2] != '-') and (layout[0][2] == layout[1][1]) and (layout[1][1] == layout[2][0]):
            return True
        else:
            return False

