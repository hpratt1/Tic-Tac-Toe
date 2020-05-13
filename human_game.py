from board import Board
from player import Player

class Human_Game: 
    
    def __init__(self):
    
        self.board = Board()
        self.player1 = Player('X', 1)
        self.player2 = Player('O', 2)
        self.turn = 1
        self.round = 1
        
    def display_board(self):
        self.board.display()
    
    def getTurn(self):
        return self.turn
    
    def switchTurn(self):
        turn = self.turn
        if turn == 1:
            self.turn = 2
        else:
            self.turn = 1
    
            
    def take_turn(self):
        turn = self.turn
        print("Player " + str(turn) + " Move: ")
        row = int(input("Row Number(0-2): "))
        col = int(input("Column Number(0-2): "))
        while (self.board.check_valid_move(row, col) == False):
            print("Invalid Entry. Try Again.")
            row = int(input("Row Number(0-2): "))
            col = int(input("Column Number(0-2): "))
        if turn == 1:
            symbol = self.player1.getSymbol()
        else: 
            symbol = self.player2.getSymbol()
        if symbol == 'X':
            
                self.board.insert_X(row, col)
        else:
                self.board.insert_O(row, col)
        self.switchTurn()

    def check_tie(self):
        return self.board.check_full_board()
    
    def check_winner(self):
        return self.board.check_winning_board()
    
    def play_game(self):
        self.display_board()
        while(self.check_winner() == False):
            self.take_turn()
            self.display_board()
            if (self.check_tie() and (self.check_winner() == False)):
                print("Game Over. The result is a tie.")
                return
        self.switchTurn()
        winner_num = self.getTurn()
        print("Player " + str(winner_num) + " Wins!")
