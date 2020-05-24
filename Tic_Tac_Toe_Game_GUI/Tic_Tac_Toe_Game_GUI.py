import tkinter as tk
from Tic_Tac_Toe_Logic import *


class TicTacToeGameGui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.game_board = create_new_game_board()

        self.create_widgets(self.game_board)


    def cell_clicked(self, cell_coordinates):
        mark_cell(self.game_board, X_TOKEN, cell_coordinates)
        
        self.cell_buttons[cell_coordinates].configure(state="disabled")
        
        self.refresh_gui()

        winning_token = check_win(self.game_board)

        if winning_token:
            congratulate_winner(winning_token)
            self.restart_game()

        if not get_empty_cells_coordinates(self.game_board):
            print("Game over, no more valid moves")
            self.restart_game()


        computer_cell_coordinates = computer_move(self.game_board)
        self.cell_buttons[computer_cell_coordinates].configure(state="disabled")
        
        self.refresh_gui()
    
        winning_token = check_win(self.game_board)

        if winning_token:
            congratulate_winner(winning_token)
            self.restart_game()

        if get_empty_cells_coordinates(self.game_board) == None:
            print("Game over, no more valid moves")
            self.restart_game()


    def create_widgets(self, game_board):
        button_width = 15
        button_height = 10

        self.cell_1_1 = tk.Button(self, width=button_width, height=button_height, text=self.game_board[(1,1)], command = lambda: self.cell_clicked((1,1)))
        self.cell_1_2 = tk.Button(self, width=button_width, height=button_height, text=self.game_board[(1,2)], command = lambda: self.cell_clicked((1,2)))
        self.cell_1_3 = tk.Button(self, width=button_width, height=button_height, text=self.game_board[(1,3)], command = lambda: self.cell_clicked((1,3)))
        self.cell_2_1 = tk.Button(self, width=button_width, height=button_height, text=self.game_board[(2,1)], command = lambda: self.cell_clicked((2,1)))
        self.cell_2_2 = tk.Button(self, width=button_width, height=button_height, text=self.game_board[(2,2)], command = lambda: self.cell_clicked((2,2)))
        self.cell_2_3 = tk.Button(self, width=button_width, height=button_height, text=self.game_board[(2,3)], command = lambda: self.cell_clicked((2,3)))
        self.cell_3_1 = tk.Button(self, width=button_width, height=button_height, text=self.game_board[(3,1)], command = lambda: self.cell_clicked((3,1)))
        self.cell_3_2 = tk.Button(self, width=button_width, height=button_height, text=self.game_board[(3,2)], command = lambda: self.cell_clicked((3,2)))
        self.cell_3_3 = tk.Button(self, width=button_width, height=button_height, text=self.game_board[(3,3)], command = lambda: self.cell_clicked((3,3)))
        
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
                                        fg="red",
                                        command=self.restart_game)

        self.restart_button.grid(row=3, column=0, columnspan=3)

        self.quit_button = tk.Button(   self, 
                                        text="Quit", 
                                        fg="red",
                                        command=self.master.destroy)
        self.quit_button.grid(row=4, column=0, columnspan=3)


    def refresh_gui(self):
        self.cell_1_1.configure(text=self.game_board[(1,1)])
        self.cell_1_2.configure(text=self.game_board[(1,2)])
        self.cell_1_3.configure(text=self.game_board[(1,3)])
        self.cell_2_1.configure(text=self.game_board[(2,1)])
        self.cell_2_2.configure(text=self.game_board[(2,2)])
        self.cell_2_3.configure(text=self.game_board[(2,3)])
        self.cell_3_1.configure(text=self.game_board[(3,1)])
        self.cell_3_2.configure(text=self.game_board[(3,2)])
        self.cell_3_3.configure(text=self.game_board[(3,3)])


    def restart_game(self):
        restart_game(self.game_board)

        for cell_button in self.cell_buttons.values():
            cell_button.configure(state="normal")

        self.refresh_gui()


def main():
    root = tk.Tk()
    game = TicTacToeGameGui(master=root)
    game.mainloop()


if __name__ == "__main__":
    main()