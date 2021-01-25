from ex import *
from board import board,display_board
#handle a single turn of a player
def handle_turn(player):
  #get whose turn it is
      print(player + "'s turn.")
      #get position from player
      position = input("Enter a position between 1 to 9 : ")

      # Whatever the user inputs, make sure it is a valid input, and the position is still open
      valid = False
      while not valid :
        #make sure input is valid
        while position not in ["1","2","3","4","5","6","7","8","9"]:
          # position = input("Invalid Input.Enter a position between 1 to 9 : ")
          raise invalidInput()
          
        # get index in board list
        position = int(position) - 1
        #make sure position is available on the board
        if board[position] == "-":
          valid = True
        else:
          raise positionAlreadyFilled()
          # print("You can't go there. Go again.")

#put x or o on board
      board[position] = player
#show game board
      display_board()