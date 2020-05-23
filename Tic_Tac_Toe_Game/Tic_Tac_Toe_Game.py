import random
import itertools

X_TOKEN = "X"
O_TOKEN = "O"
NULL_TOKEN = ""
ROW_COUNT = 3
COLUMN_COUNT = 3
CELL_COUNT = ROW_COUNT * COLUMN_COUNT

def create_new_game_board():
    game_board = {}
    for row in range(1, ROW_COUNT + 1):
        for column in range(1, COLUMN_COUNT + 1):
            game_board[(row, column)] = NULL_TOKEN
    return game_board


def get_empty_cells_coordinates(game_board):
    empty_cells_coordinates = []
    
    for cells_coordinates in game_board:
        if game_board[cells_coordinates] == NULL_TOKEN:
            empty_cells_coordinates.append(cells_coordinates)

    return empty_cells_coordinates


def print_game_board(game_board):
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


def mark_cell(game_board, token, cell_coordinates):
    """Function marks specified cell with chosen token"""
    if cell_coordinates in game_board:
        game_board[cell_coordinates] = token
    else:
        raise ValueError("Cell coordinates do not exist") 


def player_get_next_move(empty_cells_coordinates):
    """Function gets processed input coordinates from player and checks if the cell is available"""
    while True:
        input_coordinates = input("Type your next move in form of 'x,y':")
        
        print("")

        cell_coordinates = process_and_validate_coordinates(input_coordinates)

        if cell_coordinates == None:
            continue
        else:
            if cell_coordinates in empty_cells_coordinates:
                return cell_coordinates
            else:
                print("Chosen cell is not available, try again\n")
                continue


def process_and_validate_coordinates(input_coordinates):
    """This function converts input string to 2-element tuple of coordinates if the string is valid"""
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


def check_win(game_board):
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


def congratulate_winner(token):
    print("====================================================== TOKEN {} WINS ======================================================".format(token))
   

def player_move(game_board):
    empty_cells_coordinates = get_empty_cells_coordinates(game_board)
    coordinates = player_get_next_move(empty_cells_coordinates)
    mark_cell(game_board, X_TOKEN, coordinates)
    empty_cells_coordinates.remove(coordinates)


def computer_move(game_board):
    empty_cells_coordinates = get_empty_cells_coordinates(game_board)
    coordinates = computer_get_next_move(game_board)
    mark_cell(game_board, O_TOKEN, coordinates)
    empty_cells_coordinates.remove(coordinates)


def computer_get_next_move(game_board):
    def check_win_possible_in_next_move(game_board):
        """Check if win in next move is possible, if so - choose this move"""
        empty_cells_coordinates = get_empty_cells_coordinates(game_board)
        
        for cell_coordinates in empty_cells_coordinates:
            game_board_copy = game_board.copy()
            mark_cell(game_board_copy, O_TOKEN, cell_coordinates)

        if check_win(game_board_copy) == O_TOKEN:
            return cell_coordinates

    def check_lose_possible_in_next_move(game_board):
        """Check if lose in next move is possible, if so - block this move"""
        empty_cells_coordinates = get_empty_cells_coordinates(game_board)
        
        for cell_coordinates in empty_cells_coordinates:
            game_board_copy = game_board.copy()
            mark_cell(game_board_copy, X_TOKEN, cell_coordinates)

        if check_win(game_board_copy) == X_TOKEN:
            return cell_coordinates

    def check_next_best_move(game_board):
        """Checks for best move and returns it"""
        empty_cells_coordinates = get_empty_cells_coordinates(game_board)

    coordinates_A = check_win_possible_in_next_move(game_board)
    
    coordinates_B = check_lose_possible_in_next_move(game_board)

    coordinates_C = check_next_best_move(game_board)

    if coordinates_A:
        print("Option A")
        coordinates = coordinates_A
    elif coordinates_B:
        print("Option B")
        coordinates = coordinates_B
    elif coordinates_C:
        print("Option C")
        coordinates = coordinates_C
    else:
        print("RANDOM MOVE")
        coordinates = random.choice(get_empty_cells_coordinates(game_board))

    return coordinates


def main():
    game_board = create_new_game_board()

    print_game_board(game_board)

    players = itertools.cycle(["Player", "Computer"])

    while len(get_empty_cells_coordinates(game_board)) > 0: 
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
            return
    else:
        print("Game over, no more valid moves")


if __name__ == "__main__":
    main()