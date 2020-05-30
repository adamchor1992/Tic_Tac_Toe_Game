import tkinter as tk
import tkinter.messagebox
from Tic_Tac_Toe_Common_Logic import *

ROW_COUNT = 5
COLUMN_COUNT = 5


class TicTacToeGameGui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self._master = master
        self.pack()

        self._game_board = create_game_board(ROW_COUNT, COLUMN_COUNT)

        self.create_widgets()

        self._players = itertools.cycle(["Player", "Computer"])

        self._click_flag = tk.BooleanVar(value=False)


    def cell_clicked(self, cell_coordinates):
        """Cell buttons callback

        Args:
            cell_coordinates: Coordinates related to which button/cell was clicked

        Returns:
            None
        """

        print("Cell clicked")

        self._click_flag.set(True)

        mark_cell(self._game_board, X_TOKEN, cell_coordinates)
        self.cell_buttons[cell_coordinates].configure(state="disabled")


    def create_widgets(self):
        """Builds game graphical user interface

        Args:
            None

        Returns:
            None
        """

        button_width = 15
        button_height = 10

        self.cell_1_1 = tk.Button(self, width=button_width, height=button_height, text=self._game_board[(1,1)], command = lambda: self.cell_clicked((1,1)))
        self.cell_1_2 = tk.Button(self, width=button_width, height=button_height, text=self._game_board[(1,2)], command = lambda: self.cell_clicked((1,2)))
        self.cell_1_3 = tk.Button(self, width=button_width, height=button_height, text=self._game_board[(1,3)], command = lambda: self.cell_clicked((1,3)))
        self.cell_2_1 = tk.Button(self, width=button_width, height=button_height, text=self._game_board[(2,1)], command = lambda: self.cell_clicked((2,1)))
        self.cell_2_2 = tk.Button(self, width=button_width, height=button_height, text=self._game_board[(2,2)], command = lambda: self.cell_clicked((2,2)))
        self.cell_2_3 = tk.Button(self, width=button_width, height=button_height, text=self._game_board[(2,3)], command = lambda: self.cell_clicked((2,3)))
        self.cell_3_1 = tk.Button(self, width=button_width, height=button_height, text=self._game_board[(3,1)], command = lambda: self.cell_clicked((3,1)))
        self.cell_3_2 = tk.Button(self, width=button_width, height=button_height, text=self._game_board[(3,2)], command = lambda: self.cell_clicked((3,2)))
        self.cell_3_3 = tk.Button(self, width=button_width, height=button_height, text=self._game_board[(3,3)], command = lambda: self.cell_clicked((3,3)))
        
        self.cell_buttons = {}

        self.cell_buttons[(1,1)] = self.cell_1_1
        self.cell_buttons[(1,2)] = self.cell_1_2
        self.cell_buttons[(1,3)] = self.cell_1_3
        self.cell_buttons[(2,1)] = self.cell_2_1
        self.cell_buttons[(2,2)] = self.cell_2_2
        self.cell_buttons[(2,3)] = self.cell_2_3
        self.cell_buttons[(3,1)] = self.cell_3_1
        self.cell_buttons[(3,2)] = self.cell_3_2
        self.cell_buttons[(3,3)] = self.cell_3_3

        self.cell_1_1.grid(row=0,column=0)
        self.cell_1_2.grid(row=0,column=1)
        self.cell_1_3.grid(row=0,column=2)
        self.cell_2_1.grid(row=1,column=0)
        self.cell_2_2.grid(row=1,column=1)
        self.cell_2_3.grid(row=1,column=2)
        self.cell_3_1.grid(row=2,column=0)
        self.cell_3_2.grid(row=2,column=1)
        self.cell_3_3.grid(row=2,column=2)

        self.restart_button = tk.Button(self, 
                                        text="Restart", 
                                        fg="black",
                                        command=self.restart_game)

        self.restart_button.grid(row=3, column=0, columnspan=3)

        self.quit_button = tk.Button(self, 
                                     text="Quit", 
                                     fg="red",
                                     command=self._master.destroy)
        
        self.quit_button.grid(row=4, column=0, columnspan=3)


    def refresh_gui(self):
        """Refreshes graphical interface by setting each button text according to game board state
        
        Args:
            None

        Returns:
            None
        """

        self.cell_1_1.configure(text=self._game_board[(1,1)])
        self.cell_1_2.configure(text=self._game_board[(1,2)])
        self.cell_1_3.configure(text=self._game_board[(1,3)])
        self.cell_2_1.configure(text=self._game_board[(2,1)])
        self.cell_2_2.configure(text=self._game_board[(2,2)])
        self.cell_2_3.configure(text=self._game_board[(2,3)])
        self.cell_3_1.configure(text=self._game_board[(3,1)])
        self.cell_3_2.configure(text=self._game_board[(3,2)])
        self.cell_3_3.configure(text=self._game_board[(3,3)])


    def restart_game(self):
        """Restarts game which effectively means reseting game board and activating again all cells
        
        Args:
            None

        Returns:
            None
        """
        reset_game_board(self._game_board)

        for cell_button in self.cell_buttons.values():
            cell_button.configure(state="normal")

        self.refresh_gui()


    def congratulate_winner(self, token):
        """Prints congratulations pointing out victorious token

        Args:
            token: String representing winning token

        Returns:
            None
        """

        tkinter.messagebox.showinfo("Information", "TOKEN {} WINS".format(token))


    def game_round(self):
        """Method managing whole round consisting of multiple game turns. Returns when round is over

        Args:
            None

        Returns:
            None
        """
        while get_empty_cells_coordinates(self._game_board):
            if self.game_turn() != None:
                return
        else:
            tkinter.messagebox.showinfo("TIE", "No more valid moves")


    def game_turn(self):
        """Method managing whole round consisting of multiple game turns. Returns when turn is over
    
        Args:
            None

        Returns:
            None
        """
        if next(self._players) == "Player":
            self._master.wait_variable(self._click_flag)
            print("PLAYER MOVE")
        else:
            computer_cell_coordinates = computer_move(self._game_board)
            self.cell_buttons[computer_cell_coordinates].configure(state="disabled")
            print("COMPUTER MOVE")
    
        self.refresh_gui()

        winning_token = check_win_3x3(self._game_board)
    
        if winning_token:
            self.congratulate_winner(winning_token)
            return winning_token
        else:
            return None


def main():
    root = tk.Tk()
    root.title("Tic Tac Toe")

    game = TicTacToeGameGui(master=root)

    while True:
        game.game_round()
        game.restart_game()
    

if __name__ == "__main__":
    main()