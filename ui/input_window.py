#!/usr/bin/python3

import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import tkinter.messagebox as msgbox


class InterfaceWindow:
    
    def __init__(self, bg) -> None:
        self.window = tk.Tk()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window_width = 450
        self.window_height = 200
        self.input = tk.StringVar()
        self.frame = tk.Frame(self.window)
        self.bg =bg
    # end __init__ def
    
    # Set options for creating a gui window
    def create_input_window(self):
        center_x = int(self.screen_width/2 - self.window_width/2)
        center_y = int(self.screen_height/2 - self.window_height/2)
        
        self.window.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
        self.window.configure(bg=f'{self.bg}')
    # end def

    def display_window_title(self):
        self.window.title('Audio Frequency')
    # end def
    
    def copy_input(self):
        freq_input = self.input.get()
        return freq_input
    
    def submit(self):
        msg = f'Frequency: {self.input.get()} Hz'
        msgbox.showinfo(
                title='Audio Input',
                message=msg
            )

    
    def window_button(self):
        button = tk.Button(
            master=self.frame, 
            text='Submit',
            font = ('calibre',11, 'bold'), 
            activebackground='#37062e', 
            activeforeground='white',
            bg = 'black',
            fg = 'white',
            command=self.submit
        )
        button.pack(side = 'bottom', pady=10)

    # Display specifications for input
    def display_specs(self):
        label = tk.Label(
            self.window, 
            text='Enter a frequency value between 16 Hz and 7903 Hz',
            font = ('calibre',12), 
            fg='white',
            bg='#2e2239'
        )
        label.pack(pady=10)
    # end def

    def input_box(self):
        self.frame.pack(padx='5', fill='x', expand=True)
        
        input_label = tk.Label(
            self.frame, 
            text = 'Enter frequency [Hz]', 
            font = ('calibre',11),
            fg = 'white',
            bg = '#19121e'
        )
        input_label.pack(fill='x', expand=True)
        
        input_entry = ttk.Entry(self.frame, textvariable=self.input)
        input_entry.pack(fill='x', expand=True)
        input_entry.focus()

    # Make sure input is valid
    def input_error(self):
        msgbox.showerror('Error', 'Invalid Input')
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