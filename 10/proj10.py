    ###########################################################
    #  Computer Project #10
    #
    #  Algorithm
    #    function to convert letter-number position to row-column indices
    #       get letter and number from position
    #       get row number from location of letter in LETTERS
    #       get column number from position
    #    function to convert row-column indices to letter-number position
    #       get row letter as index of row in LETTERS
    #       get column number from index
    #    function to initialize the game board
    #       gets the location of the middle of the board
    #       places two white and two black pieces in the middle diagonally
    #    function to count the number of black and white pieces on the board.
    #       for loops for every row and column of board
    #           gets piece at a position
    #           if piece exists and is a color, add to the color count
    #    function to find all capturing streaks if a piece is placed at position
    #       checks every row in north direction
    #           gets piece from row, col if piece exists
    #               if piece is opponent's, append to list
    #               else, terminated streak with color
    #           if piece does not exist, terminate without finding color
    #       list = 0 if streak not terminated with color piece
    #       in dictionary, key is north, value is sorted list of pieces
    #       repeats process for other 7 directions
    #    function to create dictionary of cells a piece can capture if placed
    #       for loops for every row and column of board
    #           checks if space is empty
    #               gets list of cells that can be captured from get_all_streaks
    #               does not save non-capturing cells in dictionary
    #               adds sorted list to dictionary, key is position
    #    function to get list of positions that capture cells sorted by \
    #       number of captures
    #       gets dictionary of streaks from get_all_capturing_cells
    #       makes list of number of cells that can be captured and board \
    #           position from dictionary
    #       sorts list based on length of capturing streaks
    #    function to flip all captured pieces
    #       raise ValueError if position outside of board
    #       raise ValueError if row, column is already occupied
    #       call get_all_streaks for dictionary of streaks
    #       raise ValueError if position does not capture any pieces
    #       flips captured pieces from dictionary of streaks
    #    function to determine if game is finished
    #       gets list of possible moves for white and black piece
    #       if no possible moves for either piece, game finished
    #       if board is full, game is finished
    #    function to get current winner
    #       gets number of white and black pieces from count_pieces
    #       color with more pieces wins
    #    function to determine color of player and opponent
    #       inputs for color
    #       while loop for input to either be 'black' or 'white'
    #       opponent color is opposite the player color
    #       prints colors of players
    #    function of the main mechanism of the human vs human game play
    #       calls on the appropriate functions to play the game
    #    function to test the program
    #       calls on board.place for multiple pieces
    ###########################################################      

import reversi
import string
LETTERS = string.ascii_lowercase

"""
Program to enforce the rules of the game of Reversi.
"""

def indexify(position):      
    """
    Convert letter-number position to row-column indices.
    position: string of letter-number to convert to tuple of row-column
    Returns tuple of row-column indices.
    """  
    
    position_letter = position[:1]  #row letter
    position_number = position[1:]  #column number
    position_row = LETTERS.find(position_letter) #get row number from LETTERS
    position_column = int(position_number) - 1  #column number

    return position_row,position_column  #row, column tuple
    

def deindexify(row, col):      
    """
    Convert row-column indices to letter-number position.
    row: number to convert to letter of row
    columm: number to convert to number of column
    Returns string of letter-number position.
    """
    position_letter = LETTERS[row]   #index of row in LETTERS is row letter 
    position_number = int(col) + 1   #column number
    
    return position_letter + str(position_number)   #string of row,column
    
def initialize(board):
    """
    Places two white and two black pieces in the middle of the board.
    board: game board
    """
    index = (board.length // 2 ) -1     
    #place the pieces in the middle of the board
    
    #call on board.place to place piece at row,column
    #color of piece from reversi.Piece
    board.place(index,index,reversi.Piece("white"))
    board.place(index,index+1,reversi.Piece("black"))
    board.place(index+1, index, reversi.Piece("black"))
    board.place(index+1, index+1, reversi.Piece("white"))
                
    
def count_pieces(board):                                
    """
    Counts the number of black and white pieces currently on the board.
    board: game board
    Returns tuple of count of black and white pieces
    """
            
    black_count = 0
    white_count = 0
    for i in range(board.length):           #for every row
        for j in range(board.length):       #for every column
            piece = board.get(i,j)          
            #Gets the piece located at the position indexed by the row-column value.
            
            #Make sure piece exists, not None
            if piece and piece.color() == 'black': 
                black_count += 1
            elif piece and piece.color() == 'white':
                white_count += 1
    return black_count, white_count         
    #tuple of count of black and white pieces
    
def get_all_streaks(board, row, col, piece_arg):
    """
    Finds all capturing streaks if a piece is placed on the row, col position.
    board: game board
    row: position row
    col: position column
    piece_arg: game piece
    Returns dictionary of all capturing streaks in all 8 directions
    """
    streaks = {'e': None, 'w': None, 'n': None, 's': None, \
               'ne': None, 'nw': None, 'se': None, 'sw': None}
    
    color = piece_arg.color()
    other_color = 'white' if color == 'black' else 'black'
    # north
    L = []
    c = col
    for r in range(row-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['n'] = sorted(L)

#    # east
    L = []
    c = col
    r = row
    for c in range(col+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['e'] = sorted(L)
 
#    # south
    L = []
    c = col
    r = row
    for r in range(row+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['s'] = sorted(L)

#    # west
    L = []
    c = col
    r = row
    for c in range(col-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['w'] = sorted(L)

#    # northeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row-1,-1,-1):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['ne'] = sorted(L)
        
#    # southeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row+1,board.length):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['se'] = sorted(L)
                
#    # southwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row+1,board.length):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['sw'] = sorted(L)
    
#    # northwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row-1,-1,-1):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['nw'] = sorted(L)
            
    return streaks

def get_all_capturing_cells(board, piece):                  
    """
    Creates a dictionary of the cells a piece can capture if placed.
    board: game board
    piece: game piece
    Returns dictionary of position tuples and list of cells it can capture
    """

    streaks_dict = {}
    for i in range(board.length):       #for every row
        for j in range(board.length):   #for every column
            poss_streaks_list = []
            other_piece = board.get(i,j)
            if other_piece is None:     
                #Can only place piece if not already one at i,j
                #None means the space is empty
                poss_streaks_dict = get_all_streaks(board, i, j, piece)
                for v in poss_streaks_dict.values():
                    poss_streaks_list.extend(v)     
                    #list of cells that can be captured
                if len(poss_streaks_list) == 0:   
                #do not save non-capturing cells in dictionary
                    continue
                poss_streaks_list = sorted(poss_streaks_list)
                streaks_dict[(i,j)] = poss_streaks_list
                #key is position of piece, value is list of cells that cn be captured
               
    return streaks_dict

def get_hint(board, piece):  
    """
    Creates list of positions that capture cells sorted by number of captures.
    board: game board
    piece: game piece
    Returns sorted list of board positions
    """
    
    position_list = []
    streaks_dict = get_all_capturing_cells(board,piece) 
    #streaks for empty position
    for k,v in streaks_dict.items():
        position_list.append([len(v), deindexify(k[0],k[1])])
        #list of number of cells that can be captured and board position
    position_list.sort(reverse = True)
    #sort based on length of capturing streaks
    
    return [data[1] for data in position_list]
    #list of board positions
    
def place_and_flip(board, row, col, piece):        
    """     
    Flips all captured pieces.
    board: game board
    row: position row
    col: position column
    piece: game piece
    """
    streaks_list = []
    color = piece.color()
    
    if row > board.length or col > board.length: 
        #If the position is outside the board
        raise ValueError("Can't place {:s} at '{:s}', invalid position. \
        Type 'hint' to get suggestions.".format(color,deindexify(row,col)))
    
    new_piece = board.get(row,col)
    if new_piece is not None:
        #If the row, column is already occupied
        raise ValueError("Can't place {:s} at '{:s}', already occupied. \
        Type 'hint' to get suggestions.".format(color,deindexify(row,col)))

    streaks_dict = get_all_streaks(board,row,col,piece)

    for v in streaks_dict.values():
        streaks_list.extend(v)
        #pieces captured by position
    if len(streaks_list) == 0:
        #If the position does not capture any pieces
        raise ValueError ("Can't place {:s} at '{:s}', it's not a capture. \
        Type 'hint' to get suggestions.".format(color,deindexify(row,col)))
    
    board.place(row,col,reversi.Piece(color))
    for v in streaks_dict.values():
        for piece in v:
            board.place(piece[0], piece[1], reversi.Piece(color))
            #Flips captured pieces

def is_game_finished(board):                                       
    """
    Determines if game is finished.
    board: game board
    Returns a Boolean True/False
    """
    
    white_moves = get_all_capturing_cells(board, reversi.Piece("white")) 
    #list of possible moves for white piece
    black_moves = get_all_capturing_cells(board, reversi.Piece("black"))
    #list of possible moves for black piece
    if len(white_moves) == 0 and len(black_moves) == 0:     
        #no possible moves for either piece means game finished
        return True
    else:
        return board.is_full()  #if full, game finished
            
def get_winner(board):                                              
    """
    Gets the current winner.
    board: game board
    Returns string of winner or if draw
    """
    black_count, white_count = count_pieces(board)
    #number of black and white pieces
    #color with more pieces wins
    if black_count > white_count:
        return "black"
    elif white_count > black_count:
        return "white"
    elif black_count == white_count:
        return "draw"
    
def choose_color():
    """
    Gets color of player and opponent pieces.
    Returns tuple of color variables
    """
    color = input("Pick a color: ")
    
    while color != "black" and color != "white":
        #color input must be black or white
        print ("Wrong color, type only 'black' or 'white', try again.")
        color = input("Pick a color: ")

    #opponent is the opposite color
    if color == "black":            
        opponent_color = "white"
    else:
        opponent_color = "black"

    
    print ("You are '{:s}' and your opponent is '{:s}'."\
           .format(color, opponent_color))
    return color, opponent_color
    #returns tuple of piece color and opponent piece color

def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    """
    
    banner = """
     _____                         _ 
    |  __ \                       (_)
    | |__) |_____   _____ _ __ ___ _ 
    |  _  // _ \ \ / / _ \ '__/ __| |
    | | \ \  __/\ V /  __/ |  \__ \ |
    |_|  \_\___| \_/ \___|_|  |___/_|
    
    Developed by The Students Inc.
    CSE231 Spring Semester 2018
    Michigan State University
    East Lansing, MI 48824, USA.
    """

    prompt = "[{:s}'s turn] :> "
    print(banner)
   
    # Choose the color here
    (my_color, opponent_color) = choose_color()
    
    # Take a board of size 8x8
    # Prompt for board size
    size = input("Input a board size: ")
    board = reversi.Board(int(size))
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'white' else opponent_color
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)    
            
            # Get a piece according to turn
            piece = reversi.Piece(turn)

            # Get the command from user using input
            command = input(prompt.format(turn)).lower()
            
            # Now decide on different commands
            if command == 'exit':
                break
            elif command == 'hint':
                print("\tHint: " + ", ".join(get_hint(board, piece)))
            elif command == 'pass':
                hint = get_hint(board, piece)
                if len(hint) == 0:
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
                    print("\tHanded over to \'{:s}\'.".format(turn))
                else:
                    print("\tCan't hand over to opponent, you have moves," + \
                          " type \'hint\'.")
            else:
                    (row, col) = indexify(command)
                    place_and_flip(board, row, col, piece)
                    print("\t{:s} played {:s}.".format(turn, command))
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)    
    winner = get_winner(board)
    if winner != 'draw':
        diff = abs(piece_count[0] - piece_count[1])
        print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
    else:
        print("This game ends in a draw.")
    # --- end of game play ---

def figure_1(board):
    """
    You can use this function to test your program
    """
    board.place(0,0,reversi.Piece('black'))
    board.place(0,3,reversi.Piece('black'))
    board.place(0,4,reversi.Piece('white'))
    board.place(0,5,reversi.Piece('white'))
    board.place(0,6,reversi.Piece('white'))
    board.place(1,1,reversi.Piece('white'))
    board.place(1,3,reversi.Piece('white'))
    board.place(1,5,reversi.Piece('white'))
    board.place(1,6,reversi.Piece('white'))
    board.place(1,7,reversi.Piece('white'))
    board.place(2,2,reversi.Piece('white'))
    board.place(2,3,reversi.Piece('black'))
    board.place(2,4,reversi.Piece('white'))
    board.place(2,5,reversi.Piece('white'))
    board.place(2,7,reversi.Piece('white'))
    board.place(3,0,reversi.Piece('black'))
    board.place(3,1,reversi.Piece('white'))
    board.place(3,2,reversi.Piece('white'))
    board.place(3,4,reversi.Piece('white'))
    board.place(3,5,reversi.Piece('white'))
    board.place(3,6,reversi.Piece('black'))
    board.place(3,7,reversi.Piece('black'))
    board.place(4,0,reversi.Piece('white'))
    board.place(4,2,reversi.Piece('white'))
    board.place(4,4,reversi.Piece('white'))
    board.place(5,0,reversi.Piece('black'))
    board.place(5,2,reversi.Piece('black'))
    board.place(5,3,reversi.Piece('white'))
    board.place(5,5,reversi.Piece('black'))
    board.place(6,0,reversi.Piece('black'))
    board.place(6,1,reversi.Piece('black'))
    board.place(6,3,reversi.Piece('white'))
    board.place(6,6,reversi.Piece('white'))
    board.place(7,1,reversi.Piece('black'))
    board.place(7,2,reversi.Piece('white'))
    board.place(7,3,reversi.Piece('black'))
    board.place(7,7,reversi.Piece('black'))
    
if __name__ == "__main__":
    game_play_human()
    
