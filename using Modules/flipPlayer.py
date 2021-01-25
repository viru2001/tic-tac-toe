#whos turn is it (X goes first)


# flip the current player from X to o , or o to x
def flip_player(current_player):
#   global current_player
#if current pplayer was x then change it to o
  if current_player == "X":
    current_player = "O"
    #if current pplayer was o then change it to x
  elif current_player == "O":
    current_player = "X"

  return current_player