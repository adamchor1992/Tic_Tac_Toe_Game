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

        for cell_coordinates in game_board:
            self.assertEqual(game_board[cell_coordinates], NULL_TOKEN)


    def test_function_get_empty_cells_coordinates_all_cells_empty(self):
        game_board = create_new_game_board()

        self.assertEqual(len(get_empty_cells_coordinates(game_board)), CELL_COUNT)

        for cell_coordinates in get_empty_cells_coordinates(game_board):
            self.assertEqual(game_board[cell_coordinates], NULL_TOKEN)


    def test_function_get_empty_cells_coordinates_6_cells_empty(self):
        game_board = create_new_game_board()
        
        game_board[(1,1)] = X_TOKEN
        game_board[(2,2)] = X_TOKEN
        game_board[(3,3)] = X_TOKEN

        self.assertEqual(len(get_empty_cells_coordinates(game_board)), 6)

        self.assertEqual(game_board[(1,2)], NULL_TOKEN)
        self.assertEqual(game_board[(1,3)], NULL_TOKEN)
        self.assertEqual(game_board[(2,1)], NULL_TOKEN)
        self.assertEqual(game_board[(2,3)], NULL_TOKEN)
        self.assertEqual(game_board[(3,1)], NULL_TOKEN)
        self.assertEqual(game_board[(3,2)], NULL_TOKEN)


    def test_function_mark_cell(self):
        game_board = create_new_game_board()

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

        mark_cell(game_board, X_TOKEN, (1,1))
        mark_cell(game_board, X_TOKEN, (2,2))
        mark_cell(game_board, X_TOKEN, (3,3))

        self.assertEqual(check_win(game_board), X_TOKEN)
 

    def test_function_check_win_O_token(self):
        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,3))
        mark_cell(game_board, O_TOKEN, (2,2))
        mark_cell(game_board, O_TOKEN, (3,1))

        self.assertEqual(check_win(game_board), O_TOKEN)
        

    def test_function_check_win_all_cases(self):
        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,1))
        mark_cell(game_board, O_TOKEN, (1,2))
        mark_cell(game_board, O_TOKEN, (1,3))

        self.assertEqual(check_win(game_board), O_TOKEN)

        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (2,1))
        mark_cell(game_board, O_TOKEN, (2,2))
        mark_cell(game_board, O_TOKEN, (2,3))

        self.assertEqual(check_win(game_board), O_TOKEN)

        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (3,1))
        mark_cell(game_board, O_TOKEN, (3,2))
        mark_cell(game_board, O_TOKEN, (3,3))

        self.assertEqual(check_win(game_board), O_TOKEN)

        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,1))
        mark_cell(game_board, O_TOKEN, (2,1))
        mark_cell(game_board, O_TOKEN, (3,1))

        self.assertEqual(check_win(game_board), O_TOKEN)

        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,2))
        mark_cell(game_board, O_TOKEN, (2,2))
        mark_cell(game_board, O_TOKEN, (3,2))

        self.assertEqual(check_win(game_board), O_TOKEN)

        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,3))
        mark_cell(game_board, O_TOKEN, (2,3))
        mark_cell(game_board, O_TOKEN, (3,3))

        self.assertEqual(check_win(game_board), O_TOKEN)

        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,1))
        mark_cell(game_board, O_TOKEN, (2,2))
        mark_cell(game_board, O_TOKEN, (3,3))

        self.assertEqual(check_win(game_board), O_TOKEN)

        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,3))
        mark_cell(game_board, O_TOKEN, (2,2))
        mark_cell(game_board, O_TOKEN, (3,1))

        self.assertEqual(check_win(game_board), O_TOKEN)


    def test_function_computer_move_win_in_next_move_case1(self):
        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,1))
        mark_cell(game_board, O_TOKEN, (2,2))

        computer_move(game_board)

        self.assertEqual(game_board[(3,3)], O_TOKEN)


    def test_function_computer_move_win_in_next_move_case2(self):
        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,1))
        mark_cell(game_board, O_TOKEN, (1,2))

        computer_move(game_board)

        self.assertEqual(game_board[(1,3)], O_TOKEN)


    def test_function_computer_move_win_in_next_move_case3(self):
        game_board = create_new_game_board()

        mark_cell(game_board, O_TOKEN, (1,3))
        mark_cell(game_board, O_TOKEN, (2,3))

        computer_move(game_board)

        self.assertEqual(game_board[(3,3)], O_TOKEN)


    def test_function_computer_move_avoid_lose_in_next_move_case1(self):
        game_board = create_new_game_board()

        mark_cell(game_board, X_TOKEN, (1,1))
        mark_cell(game_board, X_TOKEN, (2,2))

        computer_move(game_board)

        self.assertEqual(game_board[(3,3)], O_TOKEN)

    def test_function_computer_move_avoid_lose_in_next_move_case2(self):
        game_board = create_new_game_board()

        mark_cell(game_board, X_TOKEN, (1,2))
        mark_cell(game_board, X_TOKEN, (2,2))

        computer_move(game_board)

        self.assertEqual(game_board[(3,2)], O_TOKEN)

    def test_function_computer_move_avoid_lose_in_next_move_case3(self):
        game_board = create_new_game_board()

        mark_cell(game_board, X_TOKEN, (1,3))
        mark_cell(game_board, X_TOKEN, (2,2))

        computer_move(game_board)

        self.assertEqual(game_board[(3,1)], O_TOKEN)


unittest.main()