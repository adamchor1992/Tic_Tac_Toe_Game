from Tic_Tac_Toe_Logic import *

def print_game_board(game_board):
    """Displays game board in a text-based way

    Args:
        game_board: Dictionary representing game board

    Returns:
        None
    """
    
    print()

    for row in range(1, ROW_COUNT + 1):
        for column in range(1, COLUMN_COUNT + 1):
            print("\t{0}\t".format(game_board[(row, column)]), end = "")

            if column == COLUMN_COUNT:
                print("")
            else:
                print("|", end = "")

        if row == ROW_COUNT:
            break
        else:
            print("-------------------------------------------------")

    print()


def process_and_validate_coordinates(input_coordinates):
    """Converts input string to 2-element tuple of coordinates if the string is valid
        
    Args:
        input_coordinates: String representing cell coordinates

    Returns:
        If coordinates are valid - tuple representing the coordinates is returned, None otherwise
    """

    if len(input_coordinates) == 0:
        print("Empty coordinates, try again\n")
        return None
    
    input_coordinates = input_coordinates.split(',')

    if len(input_coordinates) != 2:
        print("Wrong number of coordinates, try again\n")
        return None

    try:
        coordinate_x = int(input_coordinates[0])
        coordinate_y = int(input_coordinates[1])
    except ValueError:
        print("Cannot convert input coordinates to numbers, try again\n")
        return None

    if coordinate_x < 1 or coordinate_x > ROW_COUNT:
        print("Wrong x coordinate, try again\n")
        return None

    if coordinate_y < 1 or coordinate_y > COLUMN_COUNT:
        print("Wrong y coordinate, try again\n")
        return None

    return (coordinate_x, coordinate_y)


def player_get_next_move(game_board):
    """Gets input coordinates from player, processes it and checks if the cell is available. 
        It does not return until proper coordinates have been typed

    Args:
        game_board: Dictionary representing game board

    Returns:
        Tuple of coordinates
    """

    while True:
        input_coordinates = input("Type your next move in form of 'x,y':")
        
        print("")

        cell_coordinates = process_and_validate_coordinates(input_coordinates)

        if cell_coordinates == None:
            continue
        else:
            if cell_coordinates in get_empty_cells_coordinates(game_board):
                return cell_coordinates
            else:
                print("Chosen cell is not available, try again\n")
                continue


def congratulate_winner(token):
    """Prints congratulations pointing out victorious token

    Args:
        token: String representing winning token

    Returns:
        None
    """

    print("====================================================== TOKEN {} WINS ======================================================".format(token))


def player_move(game_board):
    """Processes player move based on the current game board state
        
    Args:
        game_board: Dictionary representing game board

    Returns:
        Tuple representing cell coordinates
    """

    cell_coordinates = player_get_next_move(game_board)
    mark_cell(game_board, X_TOKEN, cell_coordinates)
    return cell_coordinates


def game_turn(game_board, players):
    """Function managing whole round consisting of multiple game turns. Returns when turn is over
    
    Args:
        game_board: Dictionary representing game board
        players: Cycle object representing players taking turns

    Returns:
        Winning token if any player won, None otherwise
    """

    if next(players) == "Player":
        player_move(game_board)
        print("PLAYER MOVE")
    else:
        computer_move(game_board)
        print("COMPUTER MOVE")
    
    print_game_board(game_board)
    
    winning_token = check_win(game_board)
    
    if winning_token:
        congratulate_winner(winning_token)
        return winning_token
    else:
        return None


def game_round(game_board, players):
    """Function managing whole round consisting of multiple game turns. Returns when round is over

    Args:
        game_board: Dictionary representing game board
        players: Cycle object representing players taking turns

    Returns:
        None
    """

    while get_empty_cells_coordinates(game_board):
        if game_turn(game_board, players) != None:
            return
    else:
        print("TIE, No more valid moves available")


def main():
    game_board = create_new_game_board()

    players = itertools.cycle(["Player", "Computer"])

    while True:
        print_game_board(game_board)

        game_round(game_board, players)

        user_input = input("Type anything to continue, Type quit to exit program: ")

        if user_input == "quit":
            break
        else:
            reset_game_board(game_board)


if __name__ == "__main__":
    main()