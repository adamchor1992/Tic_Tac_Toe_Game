import random
import itertools

X_TOKEN = "X" # PLAYER TOKEN
O_TOKEN = "O" # COMPUTER TOKEN
NULL_TOKEN = ""
ROW_COUNT = 3
COLUMN_COUNT = 3
CELL_COUNT = ROW_COUNT * COLUMN_COUNT


def create_game_board():
    """Creates new game board in form of tuple:string dictionary  {(x,y):TOKEN}
    
    Args: 
        None

    Returns:
        Dictionary representing game board
    """

    game_board = {}
    for row in range(1, ROW_COUNT + 1):
        for column in range(1, COLUMN_COUNT + 1):
            game_board[(row, column)] = NULL_TOKEN
    return game_board


def reset_game_board(game_board):
    """Resets game board by assigning NULL tokens to all dictionary values

    Args:
        game_board: Dictionary representing game board

    Returns:
        None
    """
    
    for cell_coordinates in game_board:
        game_board[cell_coordinates] = NULL_TOKEN


def get_empty_cells_coordinates(game_board):
    """Extracts empty cells coordinates from dictionary representing game board

    Args:
        game_board: Dictionary representing game board

    Returns:
        List of coordinates of empty cells
    """
    
    empty_cells_coordinates = []
    
    for cells_coordinates in game_board:
        if game_board[cells_coordinates] == NULL_TOKEN:
            empty_cells_coordinates.append(cells_coordinates)

    return empty_cells_coordinates


def mark_cell(game_board, token, cell_coordinates):
    """Marks specified cell with chosen token. Raises ValueError if specified coordinates do not exist in game board

    Args:
        game_board: Dictionary representing game board
        token: String representing game token
        cell_coordinates: Tuple of coordinates

    Returns:
        None
    """

    if cell_coordinates in game_board:
        game_board[cell_coordinates] = token
    else:
        raise ValueError("Cell coordinates do not exist") 


def check_win(game_board):
    """Checks if pattern of tokens on a game board matches any of the winning patterns

    Args:
        game_board: Dictionary representing game board

    Returns:
        String representing winning token, None otherwise
    """

    tokens = (X_TOKEN, O_TOKEN)

    for token in tokens:
        if game_board[(1,1)] == token and game_board[(1,2)] == token and game_board[(1,3)] == token:
            return token
        elif game_board[(2,1)] == token and game_board[2,2] == token and game_board[2,3] == token:
            return token
        elif game_board[(3,1)] == token and game_board[(3,2)] == token and game_board[(3,3)] == token:
            return token
        elif game_board[(1,1)] == token and game_board[(2,1)] == token and game_board[(3,1)] == token:
            return token
        elif game_board[(1,2)] == token and game_board[(2,2)] == token and game_board[(3,2)] == token:
            return token
        elif game_board[(1,3)] == token and game_board[(2,3)] == token and game_board[(3,3)] == token:
            return token
        elif game_board[(1,1)] == token and game_board[(2,2)] == token and game_board[(3,3)] == token:
            return token
        elif game_board[(1,3)] == token and game_board[(2,2)] == token and game_board[(3,1)] == token:
            return token

    return None


def computer_move(game_board):
    """Processes computer move based on the current game board state
        
    Args:
        game_board: Dictionary representing game board

    Returns:
        Tuple representing cell coordinates

    """

    cell_coordinates = computer_calculate_next_move(game_board)
    mark_cell(game_board, O_TOKEN, cell_coordinates)
    return cell_coordinates


def computer_calculate_next_move(game_board):
    """Figures out computer's next move

    Args:
        game_board: Dictionary representing game board

    Returns:
        Cell coordinates of next move

    """

    cell_coordinates = check_win_possible_in_next_move(game_board)
    
    if cell_coordinates:
        print("Option A - going for win")
        return cell_coordinates
    else:
        cell_coordinates = check_lose_possible_in_next_move(game_board)
        
        if cell_coordinates:
            print("Option B - avoiding lose")
            return cell_coordinates
        else:
            cell_coordinates = check_next_best_move(game_board)
            
            if cell_coordinates:
                print("Option C - choosing non-winning and non-blocking lose best move: ({x},{y})".format(x=cell_coordinates[0], y=cell_coordinates[1]))
                return cell_coordinates
            else:
                assert False, print("================= NO MOVE CHOSEN - CRITICAL ERROR =================")


def check_win_possible_in_next_move(game_board):
    """Check if win in next move is possible, if so - choose this move

    Args:
        game_board: Dictionary representing game board

    Returns:
        Cell coordinates of next move

    """

    for cell_coordinates in get_empty_cells_coordinates(game_board):
        game_board_copy = game_board.copy()
        mark_cell(game_board_copy, O_TOKEN, cell_coordinates)

        if check_win(game_board_copy) == O_TOKEN:
            return cell_coordinates

    return None


def check_lose_possible_in_next_move(game_board):
    """Check if lose in next move is possible, if so - block this move

    Args:
        game_board: Dictionary representing game board

    Returns:
        Cell coordinates of next move

    """

    for cell_coordinates in get_empty_cells_coordinates(game_board):
        game_board_copy = game_board.copy()
        mark_cell(game_board_copy, X_TOKEN, cell_coordinates)
    
        if check_win(game_board_copy) == X_TOKEN:
            return cell_coordinates

    return None


def check_next_best_move(game_board):
    """Check for best move and choose it

    Args:
        game_board: Dictionary representing game board

    Returns:
        Cell coordinates of next move

    """

    # First select middle cell, then corners and then other cells. It is crucial that this list 
    # contains all possible cells coordinates and it must not contain duplicates
    move_priorities = [(2,2), (1,1), (1,3), (3,1), (3,3), (2,1), (1,2), (3,2), (2,3)]

    if search_for_duplicates(move_priorities) == True:
        raise ValueError("Duplicates not allowed")

    assert len(move_priorities) == CELL_COUNT, "List of move priorities must contain all possible cells coordinates, no more and no less"

    empty_cells_coordinates = get_empty_cells_coordinates(game_board)

    for cell_coordinates in move_priorities:
        if cell_coordinates in empty_cells_coordinates:
            return cell_coordinates

    return None


def search_for_duplicates(searched_list):
    """Searches list for duplicates

    Args:
        searched_list: List to be searched

    Returns:
        True if duplicate found, False otherwise
        
    """
    
    distinct_list = []

    for element in searched_list:
        if element not in distinct_list:
            distinct_list.append(element)
        else:
            return True

    return False