#!/usr/bin/python3

import pandas as pd
from sklearn.model_selection import train_test_split

# saves frequency input from ui or input from backend
def save_input():
    pass
# end def

# TODO: Move from sound.py
# pass an equation for producing samples
# returns array of sample values
def generate_wave_samples():
    pass


class TreeData:
    
    def __init__(self, csv_file='./audio_color_data.csv'):
        self.data = csv_file
    
    def load_data(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.csv_file)
            
            return df
            
        except pd.errors.EmptyDataError:
            print(f"Error: The file '{self.csv_file}' is empty or cannot be read.")
            
        return None
    # end def


    # features/target = 1d array -> x/y = 2d array
    def split_dataset(self, data_frame, features, target_vars):
        
        x = data_frame[features]
        y = data_frame[target_vars]
        
        x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.1, random_state=100)
        
        return x, y, x_train, x_test, y_train, y_test 
    # end def

# end class