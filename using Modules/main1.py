from board import display_board
from handleTurn import handle_turn
from result import check_if_game_over
from flipPlayer import flip_player
# from constant import game_still_going
#check if game is still going
game_still_going = True
game_still_going_tie = True
#who won
winner = None

current_player = "X"

def play_game():
      global current_player,winner,game_still_going,game_still_going_tie
      # display board initially
      display_board()
      # while the game is till going
      while game_still_going and game_still_going_tie:
        
          #handle turn of a player
          handle_turn(current_player)
      
        #check if game has ended
          # print(check_if_game_over(game_still_going))
          winner , check_tie ,game_still_going_tie = check_if_game_over(game_still_going)
          game_still_going = winner[1]
           
          # print("winner :",winner,",game still going",winner[1],", check for tie", check_tie,",game still going on of tie", game_still_going_tie)
        # flip  to other player 
          current_player = flip_player(current_player)


      #the game has ended , print winner or tie
      if winner[0] == "X" or winner[0] == "O":
        print(winner[0] + " won.")
      elif check_tie == True and game_still_going_tie == False :
        print("Tie.")



play_game()