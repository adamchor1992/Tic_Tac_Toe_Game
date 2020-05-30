from Tic_Tac_Toe_Common_Logic import *

ROW_COUNT = 3
COLUMN_COUNT = 3


class Game():
    def __init__(self):
        self._game_board = create_game_board(ROW_COUNT, COLUMN_COUNT)
        self._players = itertools.cycle(["Player", "Computer"])


    def player_move(self):
        """Processes player move based on the current game board state
        
        Args:
            None

        Returns:
            Tuple representing cell coordinates
        """

        cell_coordinates = self.player_get_next_move()
        mark_cell(self._game_board, X_TOKEN, cell_coordinates)

        return cell_coordinates


    def congratulate_winner(self, token):
        """Prints congratulations pointing out victorious token

        Args:
            token: String representing winning token

        Returns:
            None
        """

        print("====================================================== TOKEN {} WINS ======================================================".format(token))


    def process_and_validate_coordinates(self, input_coordinates):
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


    def player_get_next_move(self):
        """Gets input coordinates from player, processes it and checks if the cell is available. 
            It does not return until proper coordinates have been typed

        Args:
            None

        Returns:
            Tuple of coordinates
        """

        while True:
            input_coordinates = input("Type your next move in form of 'x,y':")
        
            print("")

            cell_coordinates = self.process_and_validate_coordinates(input_coordinates)

            if cell_coordinates == None:
                continue
            else:
                if cell_coordinates in get_empty_cells_coordinates(self._game_board):
                    return cell_coordinates
                else:
                    print("Chosen cell is not available, try again\n")
                    continue


    def game_turn(self):
        """Function managing whole round consisting of multiple game turns. Returns when turn is over
    
        Args:
            None

        Returns:
            Winning token if any player won, None otherwise
        """

        if next(self._players) == "Player":
            self.player_move()
            print("PLAYER MOVE")
        else:
            computer_move(self._game_board)
            print("COMPUTER MOVE")
    
        self.display_game_board()
    
        winning_token = check_win_3x3(self._game_board)
    
        if winning_token:
            self.congratulate_winner(winning_token)
            return winning_token
        else:
            return None


    def game_round(self):
        """Function managing whole round consisting of multiple game turns. Returns when round is over

        Args:
            None

        Returns:
            None
        """

        while get_empty_cells_coordinates(self._game_board):
            if self.game_turn() != None:
                return
        else:
            print("TIE, No more valid moves available")


    def display_game_board(self):
        """Displays game board in a text-based way

        Args:
            None

        Returns:
            None
        """
    
        print()

        for row in range(1, ROW_COUNT + 1):
            for column in range(1, COLUMN_COUNT + 1):
                print("\t{0}\t".format(self._game_board[(row, column)]), end = "")

                if column == COLUMN_COUNT:
                    print("")
                else:
                    print("|", end = "")

            if row == ROW_COUNT:
                break
            else:
                print(COLUMN_COUNT * "----------------")

        print()


    def restart_game(self):
        """Restarts game by reseting game board

        Args:
            None

        Returns:
            None
        """

        reset_game_board(self._game_board)


    def user_restart_game_dialog(self):
        """Asks user if the game shall be restarted

        Args:
            None

        Returns:
            True if user wishes to restart game, False otherwise
        """

        user_input = input("Type anything to continue, Type quit to exit program: ")
        
        if user_input == "quit":
            return False
        else:
            return True
    

def main():
    game = Game()

    while True:
        game.display_game_board()

        game.game_round()

        if game.user_restart_game_dialog() == True:
            game.restart_game()
        else:
            break


if __name__ == "__main__":
    main()