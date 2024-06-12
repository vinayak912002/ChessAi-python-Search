import board, pieces
from move import Move

def get_user_move():
    print("Example Move: D2 D4")
    move_str = input("your move : ")
    move_str = move_str.replace(" ", "")#remove all the spaces from the user input

    try:
        xfrom = letter_to_xpos(move_str[0:1])
        yfrom = 8 - int(move_str[1:2])
        xto = letter_to_xpos(move_str[2:3])
        yto = 8 - int(move_str[3:4])
        return Move(xfrom, yfrom, xto, yto)
    except ValueError:
        print("Invalid format. Example A2 A4")
        return get_user_move()
    
#checking for the validity of the move
def get_valid_user_move(board):
    while True:
        move = get_user_move()
        valid = False
        possible_moves = board.get_possible_moves(pieces.Piece.WHITE)
        
        #if there are no possible moves
        if(not possible_moves):
            return 0
        
        for possible_move in possible_moves:
            if move.equals(possible_move):
                valid = True
                break  

        if (valid):
            break
        else:
            print("invalid move")
    return move

#function for converting letter to x position on the chess board
def letter_to_xpos(letter):
    match letter:

        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 2
        case "D":
            return 3
        case "E":
            return 4
        case "F":
            return 5
        case "G":
            return 6
        case "H":
            return 7
        case _:
            raise ValueError("Invalid Letter")


#Entry point

board = board.Board.new()
print(board.to_string())

while(True):
    white_move = get_valid_user_move(board)
    if (white_move == 0):
        if (board.is_check(piece.Piece.WHITE)):
            print("Checkmate Black wins")
            break
        else:
            print("stalemate")
            break
        
    board.perform_move(white_move)
    print("player 1 move "+ white_move.to_string())
    print(board.to_string())

    black_move = get_valid_user_move(board)
    if (black_move == 0):
        if (board.is_check(piece.Piece.BLACK)):
            print("Checkmate white wins")
            break
        else:
            print("stalemate")
            break
        
    board.perform_move(black_move)

    print("player 2 move "+ black_move.to_string())
    print(board.to_string())
