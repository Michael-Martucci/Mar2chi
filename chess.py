# create chessboard
def create_board():
  return [[' ' for _ in range(8)] for _ in range(8)]

# Function to setup chess pieces on the board
def setup_pieces(board):
  for i in range(8):
    board[1][i] = 'P'  # Pawn for white
    board[6][i] = 'p'  # Pawn for black
    board[0][0] = 'R'
    board[0][7] = 'R'
    board[7][0] = 'r'
    board[7][7] = 'r'
    board[0][1] = 'N'
    board[0][6] = 'N'
    board[7][1] = 'n'
    board[7][6] = 'n'
    board[0][2] = 'B'
    board[0][5] = 'B'
    board[7][2] = 'b'
    board[7][5] = 'b'
    board[0][4] = 'Q'
    board[7][4] = 'q'
    board[0][3] = 'K'
    board[7][3] = 'k'
def print_board(board):
  print("  a b c d e f g h")
  print("+-----------------+")
  row_number = 8
  for row in board:
    print(f"{row_number}|{'|'.join(row)}|")
    row_number -= 1
    print("+-----------------+")
def main():
  chessboard = create_board()
  setup_pieces(chessboard)
  print_board(chessboard)
if __name__ == "__main__":
  main()
  
