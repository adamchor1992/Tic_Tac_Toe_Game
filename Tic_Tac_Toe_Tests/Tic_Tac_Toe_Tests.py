import unittest
from Tic_Tac_Toe_Common_Logic import *

ROW_COUNT = 3
COLUMN_COUNT = 3


class GameBoardTests(unittest.TestCase):
    def setUp(self):
        self.game_board = create_game_board(ROW_COUNT, COLUMN_COUNT)


    def test_function_create_game_board(self):
        self.assertEqual(len(self.game_board), 9)

        for cell_coordinates in self.game_board:
            self.assertEqual(self.game_board[cell_coordinates], NULL_TOKEN)


    def test_function_reset_game_board(self):
        self.game_board[(1,1)] = X_TOKEN
        self.game_board[(2,2)] = X_TOKEN
        self.game_board[(3,3)] = X_TOKEN

        reset_game_board(self.game_board)

        self.assertEqual(self.game_board[(1,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,3)], NULL_TOKEN)


    def test_function_get_empty_cells_coordinates_all_cells_empty(self):
        self.assertEqual(len(get_empty_cells_coordinates(self.game_board)), 9)

        self.assertEqual(self.game_board[(1,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,3)], NULL_TOKEN)


    def test_function_get_empty_cells_coordinates_6_cells_empty(self):
        self.game_board[(1,1)] = X_TOKEN
        self.game_board[(2,2)] = X_TOKEN
        self.game_board[(3,3)] = X_TOKEN

        self.assertEqual(len(get_empty_cells_coordinates(self.game_board)), 6)

        self.assertEqual(self.game_board[(1,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,2)], NULL_TOKEN)


    def test_function_mark_cell(self):
        mark_cell(self.game_board, X_TOKEN, (1,1))
        mark_cell(self.game_board, X_TOKEN, (2,2))
        mark_cell(self.game_board, X_TOKEN, (3,3))

        self.assertEqual(self.game_board[(1,1)], X_TOKEN)
        self.assertEqual(self.game_board[(2,2)], X_TOKEN)
        self.assertEqual(self.game_board[(3,3)], X_TOKEN)

        self.assertEqual(self.game_board[(1,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,2)], NULL_TOKEN)


class WinningPatternTests(unittest.TestCase):
    def setUp(self):
        self.game_board = create_game_board(ROW_COUNT, COLUMN_COUNT)


    def test_function_check_win_3x3_X_token(self):
        mark_cell(self.game_board, X_TOKEN, (1,1))
        mark_cell(self.game_board, X_TOKEN, (2,2))
        mark_cell(self.game_board, X_TOKEN, (3,3))

        self.assertEqual(check_win_3x3(self.game_board), X_TOKEN)
 

    def test_function_check_win_3x3_O_token(self):
        mark_cell(self.game_board, O_TOKEN, (1,3))
        mark_cell(self.game_board, O_TOKEN, (2,2))
        mark_cell(self.game_board, O_TOKEN, (3,1))

        self.assertEqual(check_win_3x3(self.game_board), O_TOKEN)
        

    def test_function_check_win_3x3_all_cases(self):
        mark_cell(self.game_board, O_TOKEN, (1,1))
        mark_cell(self.game_board, O_TOKEN, (1,2))
        mark_cell(self.game_board, O_TOKEN, (1,3))

        self.assertEqual(check_win_3x3(self.game_board), O_TOKEN)

        reset_game_board(self.game_board)
        
        mark_cell(self.game_board, O_TOKEN, (2,1))
        mark_cell(self.game_board, O_TOKEN, (2,2))
        mark_cell(self.game_board, O_TOKEN, (2,3))

        self.assertEqual(check_win_3x3(self.game_board), O_TOKEN)

        reset_game_board(self.game_board)

        mark_cell(self.game_board, O_TOKEN, (3,1))
        mark_cell(self.game_board, O_TOKEN, (3,2))
        mark_cell(self.game_board, O_TOKEN, (3,3))

        self.assertEqual(check_win_3x3(self.game_board), O_TOKEN)

        reset_game_board(self.game_board)

        mark_cell(self.game_board, O_TOKEN, (1,1))
        mark_cell(self.game_board, O_TOKEN, (2,1))
        mark_cell(self.game_board, O_TOKEN, (3,1))

        self.assertEqual(check_win_3x3(self.game_board), O_TOKEN)

        reset_game_board(self.game_board)

        mark_cell(self.game_board, O_TOKEN, (1,2))
        mark_cell(self.game_board, O_TOKEN, (2,2))
        mark_cell(self.game_board, O_TOKEN, (3,2))

        self.assertEqual(check_win_3x3(self.game_board), O_TOKEN)

        reset_game_board(self.game_board)

        mark_cell(self.game_board, O_TOKEN, (1,3))
        mark_cell(self.game_board, O_TOKEN, (2,3))
        mark_cell(self.game_board, O_TOKEN, (3,3))

        self.assertEqual(check_win_3x3(self.game_board), O_TOKEN)

        reset_game_board(self.game_board)

        mark_cell(self.game_board, O_TOKEN, (1,1))
        mark_cell(self.game_board, O_TOKEN, (2,2))
        mark_cell(self.game_board, O_TOKEN, (3,3))

        self.assertEqual(check_win_3x3(self.game_board), O_TOKEN)

        reset_game_board(self.game_board)

        mark_cell(self.game_board, O_TOKEN, (1,3))
        mark_cell(self.game_board, O_TOKEN, (2,2))
        mark_cell(self.game_board, O_TOKEN, (3,1))

        self.assertEqual(check_win_3x3(self.game_board), O_TOKEN)


class ComputerAiTests(unittest.TestCase):
    def setUp(self):
        self.game_board = create_game_board(ROW_COUNT, COLUMN_COUNT)


    def test_function_computer_move_win_in_next_move_case1(self):
        mark_cell(self.game_board, O_TOKEN, (1,1))
        mark_cell(self.game_board, O_TOKEN, (2,2))

        computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,3)], O_TOKEN)


    def test_function_computer_move_win_in_next_move_case2(self):
        mark_cell(self.game_board, O_TOKEN, (1,1))
        mark_cell(self.game_board, O_TOKEN, (1,2))

        computer_move(self.game_board)

        self.assertEqual(self.game_board[(1,3)], O_TOKEN)


    def test_function_computer_move_win_in_next_move_case3(self):
        mark_cell(self.game_board, O_TOKEN, (1,3))
        mark_cell(self.game_board, O_TOKEN, (2,3))

        computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,3)], O_TOKEN)


    def test_function_computer_move_avoid_lose_in_next_move_case1(self):
        mark_cell(self.game_board, X_TOKEN, (1,1))
        mark_cell(self.game_board, X_TOKEN, (2,2))

        computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,3)], O_TOKEN)


    def test_function_computer_move_avoid_lose_in_next_move_case2(self):
        mark_cell(self.game_board, X_TOKEN, (1,2))
        mark_cell(self.game_board, X_TOKEN, (2,2))

        computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,2)], O_TOKEN)


    def test_function_computer_move_avoid_lose_in_next_move_case3(self):
        mark_cell(self.game_board, X_TOKEN, (1,3))
        mark_cell(self.game_board, X_TOKEN, (2,2))

        computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,1)], O_TOKEN)


    def test_function_computer_move_select_best_non_winning_non_losing_move_case1(self):
        """First move should always be middle cell"""
        computer_move(self.game_board)

        self.assertEqual(self.game_board[(2,2)], O_TOKEN)


    def test_function_computer_move_select_best_non_winning_non_losing_move_case2(self):
        """If middle cell is not empty the next move should be left upper corner cell"""
        mark_cell(self.game_board, X_TOKEN, (2,2))

        computer_move(self.game_board)

        self.assertEqual(self.game_board[(1,1)], O_TOKEN)


    def test_function_computer_move_select_best_non_winning_non_losing_move_case3(self):
        """If middle cell all left upper/lower and right upper corner is not empty the next move should be right lower corner"""
        mark_cell(self.game_board, O_TOKEN, (1,1))
        mark_cell(self.game_board, O_TOKEN, (3,1))
        mark_cell(self.game_board, O_TOKEN, (2,3))
        mark_cell(self.game_board, X_TOKEN, (2,1))
        mark_cell(self.game_board, X_TOKEN, (2,2))
        mark_cell(self.game_board, X_TOKEN, (1,3))
        
        computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,3)], O_TOKEN)


class UtilitesTests(unittest.TestCase):
    def test_function_search_for_duplicates_no_duplicates(self):
        test_list = [(5,3), (1,3), (2,1)]

        self.assertFalse(search_for_duplicates(test_list))


    def test_function_search_for_duplicates_1_duplicate(self):
        test_list = [(2,4), (1,2), (2,1), (1,3), (2,4), (8,2)]

        self.assertTrue(search_for_duplicates(test_list))

    def test_function_search_for_duplicates_2_duplicate(self):
        test_list = [(1,4), (3,4), (1,4), (8,2), (5,2), (3,4)]

        self.assertTrue(search_for_duplicates(test_list))


if __name__ == "__main__":
    unittest.main()