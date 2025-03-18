#!/usr/bin/python3

import pytest
import unittest
from ui import input_window
import tkinter as tk


def test_input_window_successfully_created() -> None:
    
    in_win_obj = input_window.InterfaceWindow()
    in_win_obj.create_input_window()
    in_win_obj.run_window()
#end def test

# Run Testing
# In root directory, run python3 -m tests.test_ui
if __name__ == "__main__":
    test_input_window_successfully_created() 
    print("UI Testing Passed!")
# end if