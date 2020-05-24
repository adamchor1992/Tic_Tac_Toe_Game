from Tic_Tac_Toe_Logic import *


def main():
    game_board = create_new_game_board()

    players = itertools.cycle(["Player", "Computer"])

    while True:
        print_game_board(game_board)

        while get_empty_cells_coordinates(game_board): 
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
                break
        else:
            print("Game over, no more valid moves")

        user_input = input("Type anything to continue, Type quit to exit program: ")

        if user_input == "quit":
            break
        else:
            restart_game(game_board)


if __name__ == "__main__":
    main()