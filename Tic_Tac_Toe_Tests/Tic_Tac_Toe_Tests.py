import unittest
from Tic_Tac_Toe_Game import *


class TicTacToeTests(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_function_create_new_game_board(self):
        game_board = create_new_game_board()

        self.assertEqual(len(game_board), CELL_COUNT)


    def test_function_generate_empty_cells_coordinates(self):
        game_board = create_new_game_board()
        empty_cells_coordinates = generate_empty_cells_coordinates()

        self.assertEqual(len(empty_cells_coordinates), CELL_COUNT)

        for coordinates in empty_cells_coordinates:
            self.assertEqual(game_board[coordinates], NULL_TOKEN)


    def test_function_mark_cell(self):
        game_board = create_new_game_board()
        empty_cells_coordinates = generate_empty_cells_coordinates()

        mark_cell(game_board, X_TOKEN, (1,1))
        mark_cell(game_board, X_TOKEN, (2,2))
        mark_cell(game_board, X_TOKEN, (3,3))

        self.assertEqual(game_board[(1,1)], X_TOKEN)
        self.assertEqual(game_board[(2,2)], X_TOKEN)
        self.assertEqual(game_board[(3,3)], X_TOKEN)

        self.assertEqual(game_board[(1,2)], NULL_TOKEN)
        self.assertEqual(game_board[(1,3)], NULL_TOKEN)
        self.assertEqual(game_board[(2,1)], NULL_TOKEN)
        self.assertEqual(game_board[(2,3)], NULL_TOKEN)
        self.assertEqual(game_board[(3,1)], NULL_TOKEN)
        self.assertEqual(game_board[(3,2)], NULL_TOKEN)


    def test_function_check_win_X_token(self):
        game_board = create_new_game_board()
        empty_cells_coordinates = generate_empty_cells_coordinates()

        mark_cell(game_board, X_TOKEN, (1,1))
        mark_cell(game_board, X_TOKEN, (2,2))
        mark_cell(game_board, X_TOKEN, (3,3))

        self.assertEqual(check_win(game_board), X_TOKEN)
 

    def test_function_check_win_O_token(self):
        game_board = create_new_game_board()
        empty_cells_coordinates = generate_empty_cells_coordinates()

        mark_cell(game_board, O_TOKEN, (1,1))
        mark_cell(game_board, O_TOKEN, (2,2))
        mark_cell(game_board, O_TOKEN, (3,3))

        self.assertEqual(check_win(game_board), O_TOKEN)
        

    def test_function_computer_move_win_in_next_move(self):
        game_board = create_new_game_board()
        empty_cells_coordinates = generate_empty_cells_coordinates()

        mark_cell(game_board, O_TOKEN, (1,1))
        mark_cell(game_board, O_TOKEN, (2,2))

        computer_move(game_board, empty_cells_coordinates)

        self.assertEqual(game_board[(3,3)], O_TOKEN)


    def test_function_computer_move_lose_in_next_move(self):
        game_board = create_new_game_board()
        empty_cells_coordinates = generate_empty_cells_coordinates()

        mark_cell(game_board, X_TOKEN, (1,3))
        mark_cell(game_board, X_TOKEN, (2,2))

        computer_move(game_board, empty_cells_coordinates)

        self.assertEqual(game_board[(3,1)], O_TOKEN)


unittest.main()