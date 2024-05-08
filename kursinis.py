import os
import time

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10  
        self.player = 1
        self.Game = self.Running = 0  
        self.Mark = 'X'
        self.Draw = -1
        self.Win = 1 

    def DrawBoard(self):
        print(" %c | %c | %c " % (self.board[1], self.board[2], self.board[3]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[4], self.board[5], self.board[6]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[7], self.board[8], self.board[9]))
        print(" | | ")

    def CheckPosition(self, x):
        return self.board[x] == ' '

    def CheckWin(self):
        if self.board[1] == self.board[2] == self.board[3] != ' ' or \
           self.board[4] == self.board[5] == self.board[6] != ' ' or \
           self.board[7] == self.board[8] == self.board[9] != ' ' or \
           self.board[1] == self.board[4] == self.board[7] != ' ' or \
           self.board[2] == self.board[5] == self.board[8] != ' ' or \
           self.board[3] == self.board[6] == self.board[9] != ' ' or \
           self.board[1] == self.board[5] == self.board[9] != ' ' or \
           self.board[3] == self.board[5] == self.board[7] != ' ':
            return self.Win
        elif all(cell != ' ' for cell in self.board[1:]):
            return self.Draw
        else:
            return self.Running


    def StartGame(self):
        print("Tic-Tac-Toe Game")
        print("Player 1 [X] --- Player 2 [O]\n")
        print("Please Wait...")
        time.sleep(3)

        while self.Game == self.Running:
            os.system('cls')
            self.DrawBoard()

            if self.player % 2 != 0:
                print("Player 1's chance")
                self.Mark = 'X'
            else:
                print("Player 2's chance")
                self.Mark = 'O'

            while True:
                choice = input("Enter the position between [1-9] where you want to mark: ")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= 9:
                        if self.CheckPosition(choice):
                            break
                        else:
                            print("This position is already taken! Choose again.")
                    else:
                        print("Please enter a number between 1 and 9!")
                else:
                    print("Invalid input! Please enter a number.")

            self.board[choice] = self.Mark
            self.player += 1
            self.Game = self.CheckWin()

            os.system('cls')
            self.DrawBoard()

            if self.Game == self.Draw:
                print("Game Draw")
            elif self.Game == self.Win:
                self.player -= 1
                if self.player % 2 != 0:
                    print("Player 1 Won")
                else:
                    print("Player 2 Won")

class TicTacToeWithLogging:
    def __init__(self, tic_tac_toe):
        self.tic_tac_toe = tic_tac_toe

    def StartGame(self):
        print("Starting Tic Tac Toe game...")
        self.tic_tac_toe.StartGame()
        print("Tic Tac Toe game finished.")

if __name__ == "__main__":
    game = TicTacToe()
    game_with_logging = TicTacToeWithLogging(game)
    game_with_logging.StartGame()
