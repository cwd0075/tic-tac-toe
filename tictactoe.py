# Tic Tac Toe game in Python for command line

# Function to print the Tic Tac Toe board
def print_board(board):
  print(f'{board[0]} | {board[1]} | {board[2]}')
  print('---------')
  print(f'{board[3]} | {board[4]} | {board[5]}')
  print('---------')
  print(f'{board[6]} | {board[7]} | {board[8]}')

# Function to check if a player has won the game
def check_win(board, player):
  # Check rows and columns
  for i in range(0, 3):
    if (board[i*3] == player and board[i*3+1] == player and board[i*3+2] == player) or \
       (board[i] == player and board[i+3] == player and board[i+6] == player):
      return True
  # Check diagonals
  if (board[0] == player and board[4] == player and board[8] == player) or \
     (board[2] == player and board[4] == player and board[6] == player):
    return True
  return False

# Function to check if the board is full
def is_full(board):
  return ' ' not in board

# Function to handle player input and update the board
def player_move(board, player):
  while True:
    move = input(f'Player {player}, enter your move (1-9): ')
    if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == ' ':
      board[int(move)-1] = player
      break
    else:
      print('Invalid move. Please try again.')

# Main function to run the game
def main():
  # Initialize the board with empty spaces
  board = [' '] * 9
  # Set the players and their symbols
  players = ['X', 'O']
  # Loop through the game until there is a winner or the board is full
  while not check_win(board, 'X') and not check_win(board, 'O') and not is_full(board):
    # Print the board
    print_board(board)
    # Get the move for the current player
    player_move(board, players[0])
    # Check if the current player has won
    if check_win(board, players[0]):
      print_board(board)
      print(f'Player {players[0]} wins!')
      break
    # If the board is full and no one has won, it's a draw
    if is_full(board):
      print_board(board)
      print('It\'s a draw!')
      break
    # Switch to the other player
    players.reverse()

# Run the game
if __name__ == '__main__':
  main()