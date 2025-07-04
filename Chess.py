import os
import time

clear = lambda: os.system('cls')

class Piece:
    def __init__(self, owner, position):
        self.owner = owner
        self.position = position

class King(Piece):
    def move(self, board, destination):
        if abs(destination[0] - self.position[0]) <= 1 and abs(destination[1] - self.position[1]) <= 1:
            return True
        return False

class Queen(Piece):
    def move(self, board, destination):
        if (destination[0] == self.position[0] or destination[1] == self.position[1] or
            abs(destination[0] - self.position[0]) == abs(destination[1] - self.position[1])):
            return True
        return False

class Rook(Piece):
    def move(self, board, destination):
        if destination[0] == self.position[0] or destination[1] == self.position[1]:
            return True
        return False

class Bishop(Piece):
    def move(self, board, destination):
        if abs(destination[0] - self.position[0]) == abs(destination[1] - self.position[1]):
            return True
        return False

class Knight(Piece):
    def move(self, board, destination):
        if (abs(destination[0] - self.position[0]) == 2 and abs(destination[1] - self.position[1]) == 1 or
            abs(destination[0] - self.position[0]) == 1 and abs(destination[1] - self.position[1]) == 2):
            return True
        return False

class Pawn(Piece):
    def __init__(self, owner, position):
        super().__init__(owner, position)
        self.first_move = True

    def move(self, board, destination):
        direction = 1 if self.owner == 'white' else -1

        # One-square move
        if self.position[1] + direction == destination[1] and self.position[0] == destination[0]:
            if board[destination[1]][destination[0]] is None:
                self.first_move = False
                return True

        # Two-square move (in the first move)
        if self.first_move and self.position[1] + 2 * direction == destination[1] and self.position[0] == destination[0]:
            if board[destination[1]][destination[0]] is None and board[self.position[1] + direction][self.position[0]] is None:
                self.first_move = False
                return True

        # Capture enemy
        if abs(destination[0] - self.position[0]) == 1 and self.position[1] + direction == destination[1]:
            if board[destination[1]][destination[0]] is not None and board[destination[1]][destination[0]].owner != self.owner:
                self.first_move = False
                return True

        return False

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        self.board[0][4] = King('white', (4, 0))
        self.board[7][4] = King('black', (4, 7))

        self.board[0][3] = Queen('white', (3, 0))
        self.board[7][3] = Queen('black', (3, 7))

        self.board[0][0] = Rook('white', (0, 0))
        self.board[0][7] = Rook('white', (7, 0))
        self.board[7][0] = Rook('black', (0, 7))
        self.board[7][7] = Rook('black', (7, 7))

        self.board[0][2] = Bishop('white', (2, 0))
        self.board[0][5] = Bishop('white', (5, 0))
        self.board[7][2] = Bishop('black', (2, 7))
        self.board[7][5] = Bishop('black', (5, 7))

        self.board[0][1] = Knight('white', (1, 0))
        self.board[0][6] = Knight('white', (6, 0))
        self.board[7][1] = Knight('black', (1, 7))
        self.board[7][6] = Knight('black', (6, 7))

        for i in range(8):
            self.board[1][i] = Pawn('white', (i, 1))
            self.board[6][i] = Pawn('black', (i, 6))

def board_display(board):
    print("    a  b  c  d  e  f  g  h")
    print("  ##########################")
    for i in range(8):
        print(f"{8-i} # ", end="")
        for j in range(8):
            piece = board.board[i][j]
            if piece:
                if piece.owner == "white":
                    print(f"{piece.__class__.__name__[0]}1 ", end="")
                elif piece.owner == "black":
                    print(f"{piece.__class__.__name__[0]}2 ", end="")
            else:
                print(" . ", end="")
        print(f"# {8-i}")
    print("  ##########################")
    print("    a  b  c  d  e  f  g  h")

def convert_input_to_coords(input_str):
    if len(input_str) != 2 or input_str[0].lower() not in "abcdefgh" or not input_str[1].isdigit():
        return None
    col_convert = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    col = col_convert[input_str[0].lower()]
    row = 8 - int(input_str[1])
    if 0 <= col < 8 and 0 <= row < 8:
        return (col, row)
    return None

def validation(board, piece, destination, current_player):
    def in_board(coord):
        return 0 <= coord[0] < 8 and 0 <= coord[1] < 8

    def piece_at_position(coord):
        if in_board(coord):
            return board[coord[1]][coord[0]]
        return None

    if not in_board(destination):
        return False, "Destination out of the board"

    if not piece:
        return False, "No piece at the source."

    if piece.owner != current_player:
        return False, "Can't move opponent's piece"

    if not piece.move(board, destination):
        return False, "Invalid move for this piece"

    dest_piece = piece_at_position(destination)
    if dest_piece and dest_piece.owner == current_player:
        return False, "Can't move to a square occupied by your own piece"

    # Check path
    if isinstance(piece, (Rook, Bishop, Queen, Pawn, King)):
        step_x = (destination[0] - piece.position[0]) // (1, abs(destination[0] - piece.position[0]))
        step_y = (destination[1] - piece.position[1]) // (1, abs(destination[1] - piece.position[1]))
        current = (piece.position[0] + step_x, piece.position[1] + step_y)
        while current != destination:
            if piece_at_position(current) is not None:
                return False, "Path is blocked"
            current = (current[0] + step_x, current[1] + step_y)

    # Knight exception
    if isinstance(piece, Knight):
        return True, ""

    return True, ""

def game_loop():
    board = Board()
    current_player = 'white'

    while True:
        clear()
        board_display(board)
        print(f"Player {1 if current_player == 'white' else 2}'s turn ({current_player})")

        source = input("Enter Source Position: ")
        dest = input("Enter Destination Position: ")

        # Input to coordinates
        source_coord = convert_input_to_coords(source)
        dest_coord = convert_input_to_coords(dest)

        # Ensure valid input
        if not source_coord or not dest_coord:
            print("Invalid input. Please use the format 'e2'.")
            time.sleep(4)
            continue

        # Ensure the source piece is selected
        piece = board.board[source_coord[1]][source_coord[0]]

        # Make sure destination is not same as source
        if source_coord == dest_coord:
            print("Invalid. Destination can't be the same as the source.")
            time.sleep(4)
            continue

        # Ensure the piece at the source is not None
        if not piece:
            print("Invalid. No piece at the source.")
            time.sleep(4)
            continue

        # Validation
        valid_move, message = validation(board.board, piece, dest_coord, current_player)
        if not valid_move:
            print(f"Invalid move: {message}")
            time.sleep(4)
            continue

        # Move the piece
        board.board[dest_coord[1]][dest_coord[0]] = piece
        board.board[source_coord[1]][source_coord[0]] = None
        piece.position = dest_coord
        
        # End game if king is captured
        target_piece = board.board[dest_coord[1]][dest_coord[0]]
        if target_piece and isinstance(target_piece, King):
            board.kings_alive[target_piece.owner] = False
            print(f"{target_piece.owner.capitalize()} king has been captured.\n{target_piece.owner.capitalize()} won! Game over.")
            break

        # Switch player
        current_player = 'black' if current_player == 'white' else 'white'

if __name__ == "__main__":
    game_loop()