import ai
from move import Move

class Piece:

    WHITE = "W"
    BLACK = "B"

    def __init__(self, x, y, color, piece_type, value):
        self.x = x
        self.y = y
        self.color = color
        self.piece_type = piece_type
        self.value = value

    #this function returns all the possible diagonal moves for the peice in question.
    #this should therefore only be used for the bishop and queen since they are the only peices
    #that can move diagonally
    def get_possible_diagonal_moves(self, board):
        moves = []

        for i in range(1, 8):
            if(not board.in_bounds(self.x+i, self.y+i)):
                break
            
            piece =  board.get_piece(self.x+i, self.y+i)
            moves.append(self.get_move(board, self.x+i, self.y+i))
            if (piece!=0):
                break
            
        for i in range(1, 8):
            if(not board.in_bounds(self.x+i, self.y-i)):
                break

            piece = board.get_piece(self.x+i, self.y-i)
            moves.append(self.get_move(board, self.x+i, self.y-i))
            if(piece!=0):
                break
        
        for i in range(1, 8):
            if (not board.in_bounds(self.x-i, self.y-i)):
                break

            piece = board.get_piece(self.x-i, self.y-i)
            moves.append(self.get_move(board, self.x-i, self.y-i))
            if(piece != 0):
                break

        for i in range(1, 8):
            if (not board.in_bounds(self.x-i, self.y+i)):
                break

            piece = board.get_piece(self.x-i, self.y+i)
            moves.append(self.get_move(board, self.x-i, self.y+i))
            if(piece != 0):
                break
        
        return self.remove_null_from_list(moves)


    #returns all the possible horizontal moves
    #for rooks and queens only
    def get_possible_horizontal_moves(self, board):

        moves = []

        #towards the right of the piece
        for i in range (1, 8 - self.x):
            piece = board.get_piece(self.x + i, self.y)
            moves.append(self.get_move(board, self.x+i, self.y))
            if(piece!=0):
                break

        #towards the left of the piece
        for i in range (1, self.x + 1):
            piece = board.get_piece(self.x - i, self.y)
            moves.append(self.get_move(board, self.x-i, self.y))
            if(piece != 0):
                break
        
        #downward direction from the piece
        for i in range (1, 8-self.y):
            piece = board.get_piece(self.x, self.y + i)
            moves.append(self.get_move(board, self.x, self.y+i))
            if(piece != 0):
                break

        #upward direction from the piece
        for i in range (1, self.y + 1):
            piece = board.get_piece(self.x, self.y - i)
            moves.append(self.get_move(board, self.x, self.y-i))
            if(piece != 0):
                break

        return self.remove_null_from_list(moves)

    #this function returns a Move object with (xfrom, yfrom) set to the current location of the piece
    #(xto, yto) is set to the given position. If move is not valid 0 is returned
    #a move is not valid if it is out of bounds, or a piece of same color is eaten
    def get_move(self, board, xto, yto):

        move = 0
        if(board.in_bounds(xto, yto)):
            piece = board.get_piece(xto, yto)
            if(piece != 0):
                if(piece.color != self.color):
                    move = Move(self.x, self.y, xto, yto)
            else:
                move = Move(self.x, self.y, xto, yto)
        return move

    #returns the list of moves with all the zeroes removed
    def remove_null_from_list(self, l):
        return [move for move in l if move != 0]
        
    def to_string(self):
        return self.color + self.piece_type + " "
        
class Rook(Piece):

    PIECE_TYPE = "R"
    VALUE = 500

    def __init__(self, x, y, color):
        super(Rook, self).__init__(x, y, color, self.PIECE_TYPE, self.VALUE)

    def get_possible_moves(self, board):
        return self.get_possible_horizontal_moves(board)
    
    def clone(self):
        return Rook(self.x, self.y, self.color)


class Knight(Piece):

    PIECE_TYPE = "N"
    VALUE = 320

    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color, self.PIECE_TYPE, self.VALUE)

    #we are going to get all the possible moves by calling get_move method of the parent class
    def get_possible_moves(self, board):
        moves = []

        moves.append(self.get_move(board, self.x+2, self.y+1))
        moves.append(self.get_move(board, self.x-1, self.y+2))
        moves.append(self.get_move(board, self.x-2, self.y+1))
        moves.append(self.get_move(board, self.x+1, self.y-2))
        moves.append(self.get_move(board, self.x+2, self.y-1))
        moves.append(self.get_move(board, self.x+1, self.y+2))
        moves.append(self.get_move(board, self.x-2, self.y-1))
        moves.append(self.get_move(board, self.x-1, self.y-2))

        return self.remove_null_from_list(moves)
    
    def clone(self):
        return Knight(self.x, self.y, self.color)
    
class Bishop(Piece):

    PIECE_TYPE = "B"
    VALUE = 330

    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color, self.PIECE_TYPE, self.VALUE)
    
    def get_possible_moves(self, board):
        return self.get_possible_diagonal_moves(board)

    def clone(self):
        return Bishop(self.x, self.y, self.color)
    

class Queen(Piece):

    PIECE_TYPE = "Q"
    VALUE = 900

    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color, self.PIECE_TYPE, self.VALUE)

    def get_possible_moves(self, board):
        diagonal = self.get_possible_diagonal_moves(board)
        horizontal = self.get_possible_horizontal_moves(board)
        return horizontal+diagonal

    def clone(self):
        return Queen(self.x, self.y, self.color)
    
class King(Piece):

    PIECE_TYPE = "K"
    VALUE = 20000
    
    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color, self.PIECE_TYPE, self.VALUE)

    def get_possible_moves(self, board):
        moves = []

        moves.append(self.get_move(board, self.x, self.y+1))
        moves.append(self.get_move(board, self.x+1, self.y+1))
        moves.append(self.get_move(board, self.x-1, self.y))
        moves.append(self.get_move(board, self.x-1, self.y+1))
        moves.append(self.get_move(board, self.x+1, self.y))
        moves.append(self.get_move(board, self.x-1, self.y-1))
        moves.append(self.get_move(board, self.x, self.y-1))
        moves.append(self.get_move(board, self.x+1, self.y-1))

        moves.append(self.get_castle_kingside_move(board))
        moves.append(self.get_castle_queenside_move(board))

        return self.remove_null_from_list(moves)

    #function for checking castle kingside
    def get_castle_kingside_move(self, board):
        #is the rook in question valid?
        piece_in_corner = board.get_piece(self.x+3, self.y)
        if (piece_in_corner == 0 or piece_in_corner != Rook.PIECE_TYPE):
            return 0

        #if the rook in corner is not the same color as the king we cannot castle
        if (piece_in_corner.color != self.color):
            return 0
        
        #if king has moved we cannot castle
        if (self.color == Piece.BLACK and board.black_king_moved):
            return 0

        if (self.color == Piece.WHITE and board.white_king_moved):
            return 0

        #if there are pieces in between the king and rook we cannot castle
        if(board.get_piece(self.x+1, self.y) != 0 or board.get_piece(self.x+2, self.y) != 0):
            return 0

        return Move(self.x, self.y, self.x+2, self.y)
        
    def get_castle_queenside_move(self, board):

        #are we looking at the valid rook?
        piece_in_corner = board.get_piece(self.x-4, self.y)
        if(piece_in_corner == 0 or piece_in_corner.piece_type != Rook.PIECE_TYPE):
            return 0
        
        #if the rook in the corner is not our rook we cannot castle
        if(piece_in_corner.color != self.color):
            return 0
        
        #if the king has moved we cannot castle
        if(self.color == Piece.WHITE and board.white_king_moved):
            return 0
        if(self.color == Piece.BLACK and board.black_king_moved):
            return 0
        
        #if there are pieces in between we cannot castle
        if(board.get_piece(self.x-1, self.y) != 0 and board.get_piece(self.x-2, self.y) != 0 and board.get_piece(self.x-3, self.y) != 0):
            return 0
        
        return Move(self.x, self.y, self.x-2, self.y)


    def clone(self):
        return King(self.x, self.y , self.color)



class Pawn(Piece):

    PIECE_TYPE = "P"
    VALUE = 100

    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color, self.PIECE_TYPE, self.VALUE)

    def is_starting_position(self):
        if (self.color == Piece.BLACK):
            return self.y == 1
        else:
            return self.y == 8-2
    
    def get_possible_moves(self, board):
        moves = []

        #direction the pawn can move in 
        direction = -1
        if (self.color == Piece.BLACK):
            direction = 1
        
        #the general 1 step forward move
        if (board.get_piece(self.x, self.y + direction) == 0):
            moves.append(self.get_move(board, self.x, self.y + direction))

        #the pawn can take 2 steps as the first move
        if (self.is_starting_position() and board.get_piece(self.x, self.y+direction) == 0 and board.get_piece(self.x, self.y+ direction*2)==0):
            moves.append(Move(self.x, self.y, self.x, self.y + direction*2))
        
        #Eating pieces
        piece = board.get_piece(self.x + 1, self.y + direction)
        if (piece != 0):
            moves.append(self.get_move(board, self.x+1, self.y + direction))

        piece = board.get_piece(self.x - 1, self.y + direction)
        if (piece != 0):
            moves.append(self.get_move(board, self.x-1, self.y + direction))

        return self.remove_null_from_list(moves)

    def clone(self):
        return Pawn(self.x, self.y, self.color)