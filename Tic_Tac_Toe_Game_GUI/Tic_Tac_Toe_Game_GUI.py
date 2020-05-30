import tkinter as tk
import tkinter.messagebox
from Tic_Tac_Toe_Common_Logic import *
import PIL.Image
import PIL.ImageTk
from functools import partial


ROW_COUNT = 5
COLUMN_COUNT = 5

game_board_size = ROW_COUNT * COLUMN_COUNT

if game_board_size == 9:
    check_win = check_win_3x3
elif game_board_size == 25:
    check_win = check_win_5x5
else:
    assert false, "Invalid game board"


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

        print("Cell clicked: {}".format(cell_coordinates))

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

        button_width = 100
        button_height = 100

        path_empty_cell_image = "images/empty_cell.jpg"
        path_x_cell_image = "images/x_cell.jpg"
        path_o_cell_image = "images/o_cell.jpg"

        self.empty_cell_image = PIL.ImageTk.PhotoImage(PIL.Image.open(path_empty_cell_image))
        self.x_cell_image = PIL.ImageTk.PhotoImage(PIL.Image.open(path_x_cell_image))
        self.o_cell_image = PIL.ImageTk.PhotoImage(PIL.Image.open(path_o_cell_image))

        self.cell_buttons = {}

        for cell_coordinates in self._game_board:
            self.cell_buttons[cell_coordinates] = tk.Button(self, 
                                                            width=button_width, 
                                                            height=button_height, 
                                                            image = self.empty_cell_image, 
                                                            command = partial(self.cell_clicked, cell_coordinates))

            self.cell_buttons[cell_coordinates].grid(row=cell_coordinates[0]-1, column=cell_coordinates[1]-1)

        self.restart_button = tk.Button(self, 
                                        text="Restart", 
                                        fg="black",
                                        command=self.restart_game)

        self.restart_button.grid(row=ROW_COUNT, column=0, columnspan=COLUMN_COUNT)

        self.quit_button = tk.Button(self, 
                                     text="Quit", 
                                     fg="red",
                                     command=self._master.destroy)
        
        self.quit_button.grid(row=ROW_COUNT+1, column=0, columnspan=COLUMN_COUNT)


    def refresh_gui(self):
        """Refreshes graphical interface by setting each button text according to game board state
        
        Args:
            None

        Returns:
            None
        """

        for cell_coordinates in self.cell_buttons:
            if self._game_board[cell_coordinates] == NULL_TOKEN:
                self.cell_buttons[cell_coordinates].configure(image=self.empty_cell_image)
            elif self._game_board[cell_coordinates] == X_TOKEN:
                self.cell_buttons[cell_coordinates].configure(image=self.x_cell_image)
            elif self._game_board[cell_coordinates] == O_TOKEN:
                self.cell_buttons[cell_coordinates].configure(image=self.o_cell_image)


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

        winning_token = check_win(self._game_board)
    
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