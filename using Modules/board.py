#game board
board = ["-" , "-" ,"-",
        "-" , "-" ,"-",
        "-" , "-" ,"-" ]

 # display board to screen
def display_board():
      print("\n")
      print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
      print("--+---+---    --+---+---")
      print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
      print("--+---+---    --+---+---")
      print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
      print("\n")