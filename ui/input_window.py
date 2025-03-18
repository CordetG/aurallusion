#!/usr/bin/python3

import tkinter as tk
import tkinter.font as tkFont


class InterfaceWindow:
    
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window_width = 400
        self.window_height = 400
    # end __init__ def
    
    # Set options for creating a gui window
    def create_input_window(self):
        center_x = int(self.screen_width/2 - self.window_width/2)
        center_y = int(self.screen_height/2 - self.window_height/2)
        
        self.window.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
        self.window.configure(bg='#2e2239')
    # end def

    def display_window_title(self):
        pass
    # end def

    # Display specifications for input
    def display_specs(self):
        pass
    # end def

    def display_input_text(self):
        pass
    # end def

    # Make sure input is valid
    def input_error(self):
        pass
    # end def

    # Determine out-of-bounds values
    def input_range(self):
        pass
    # end def

    def read_input(self):
        pass
    # end def
    
    def run_window(self):
        self.window.mainloop()
    # end def