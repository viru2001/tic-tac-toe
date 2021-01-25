# from ex import *

#----------Global variables--------- 

#game board
board = ["-" , "-" ,"-",
        "-" , "-" ,"-",
        "-" , "-" ,"-" ]

#check if game is still going
game_still_going = True

#who won
winner = None

#whos turn is it (X goes first)
current_player = "X"

#----------Functions ----------------
def play_game():

      # display board initially
      display_board()
      # while the game is till going
      while game_still_going:
        
          #handle turn of a player
          handle_turn(current_player)
      
        #check if game has ended
          check_if_game_over()
      
        # flip  to other player 
          flip_player()


      #the game has ended , print winner or tie
      if winner == "X" or winner == "O":
        print(winner + " won.")
      elif winner == None:
        print("Tie.")

# display board to screen
def display_board():
      print("\n")
      print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
      print("--+---+---    --+---+---")
      print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
      print("--+---+---    --+---+---")
      print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
      print("\n")

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
          position = input("Invalid Input.Enter a position between 1 to 9 : ")
          # raise invalidInput()
          
        # get index in board list
        position = int(position) - 1
        #make sure position is available on the board
        if board[position] == "-":
          valid = True
        else:
          # raise positionAlreadyFilled()
          print("You can't go there. Go again.")

#put x or o on board
      board[position] = player
#show game board
      display_board()



#check if game is over or not
def check_if_game_over():
  check_for_winner()
  check_if_tie()

# check if someone is won
def check_for_winner():
  #set up global variable
  global winner

  #check if there is a winner anywhere
  row_winner = check_rows()
  
  column_winner = check_columns()
 
  diagonal_winner = check_diagonals()

#get winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    #there was no win
    winner = None
  
#check rows for win 
def check_rows():
  global game_still_going 
# check if any rows have same value
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #if any row have match ,stop game
  if row_1 or row_2 or row_3:
    game_still_going = False

  #return the winner x or o
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
    # return none if there was no winner
    return None


#check coolumn for win
def check_columns():
  global game_still_going 
# check if any columns have same value
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #if any column have match ,stop game
  if column_1 or column_2 or column_3:
    game_still_going = False

  #return the winner x or o
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  else:
    # return none if there was no winner
    return None


 #check diagonals for win
def check_diagonals():
  global game_still_going 
# check if any diagonals have same value
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  #if any diagonal have match ,stop game
  if diagonal_1 or diagonal_2 :
    game_still_going = False

  #return the winner x or o
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  else:
    # return none if there was no winner
    return None

# check if there is a tie
def check_if_tie():
  global game_still_going

  #if board is full
  if "-" not in board:
    game_still_going = False
    return True
  #if there is no tie
  else:
    return False 

# flip the current player from X to o , or o to x
def flip_player():
  global current_player
#if current pplayer was x then change it to o
  if current_player == "X":
    current_player = "O"
    #if current pplayer was o then change it to x
  elif current_player == "O":
    current_player = "X"


#----------Start Game-----------
play_game()