from board import board

#check if game is over or not
def check_if_game_over(game_still_going):
  winner = check_for_winner(game_still_going)
  check_tie,game_still_going_tie = check_if_tie(game_still_going)
  return winner,check_tie,game_still_going_tie

# check if someone is won
def check_for_winner(game_still_going):
  #check if there is a winner anywhere
  row_winner,game_still_going = check_rows(game_still_going)
  
  column_winner,game_still_going = check_columns(game_still_going)
 
  diagonal_winner,game_still_going = check_diagonals(game_still_going)

#get winner
  if row_winner:
    winner = row_winner,game_still_going
  elif column_winner:
    winner = column_winner,game_still_going
  elif diagonal_winner:
    winner = diagonal_winner,game_still_going
  else:
    #there was no win
    winner = None,game_still_going
  
  return winner
  
#check rows for win 
def check_rows(game_still_going):
# check if any rows have same value
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #if any row have match ,stop game
  if row_1 or row_2 or row_3:
    game_still_going = False

  #return the winner x or o
  if row_1:
    return board[0],game_still_going
  elif row_2:
    return board[3],game_still_going
  elif row_3:
    return board[6],game_still_going
  else:
    # return none if there was no winner
    return None,game_still_going


#check coolumn for win
def check_columns(game_still_going):

# check if any columns have same value
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #if any column have match ,stop game
  if column_1 or column_2 or column_3:
    game_still_going = False

  #return the winner x or o
  if column_1:
    return board[0],game_still_going
  elif column_2:
    return board[1],game_still_going
  elif column_3:
    return board[2],game_still_going
  else:
    # return none if there was no winner
    return None,game_still_going


 #check diagonals for win
def check_diagonals(game_still_going):

# check if any diagonals have same value
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  #if any diagonal have match ,stop game
  if diagonal_1 or diagonal_2 :
    game_still_going = False

  #return the winner x or o
  if diagonal_1:
    return board[0],game_still_going
  elif diagonal_2:
    return board[2],game_still_going
  else:
    # return none if there was no winner
    return None,game_still_going

# check if there is a tie
def check_if_tie(game_still_going):

  #if board is full
  if "-" not in board:
    game_still_going = False
    return True,game_still_going
  #if there is no tie
  else:
    return False,game_still_going