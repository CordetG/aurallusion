#!/usr/bin/python3

import pytest
import unittest
import pandas as pd
from utils.core_data import eval
from utils.mlsignals import tree


class TestData(unittest.TestCase):
    
    def setUp(self):
        self.data_obj = eval.TreeData(csv_file='tests/test-data.csv')
        self.none_data_obj = eval.TreeData(csv_file='tests/empty.csv')
        
        data = {
            'soundFreq': [359.61, 58.27, 587.33, 2959.96, 4315.44],
            'octave': [4, 1, 5, 7, 8],
            'note': [5, 10, 2, 6, 0],
            'r': [111, 255, 0, 140, 31],
            'g': [255, 185, 90, 0, 0],
            'b': [0, 185, 120, 240, 43]
        }
        self.df = pd.DataFrame(data)
        self.features = ['soundFreq', 'octave', 'note']
        self.target_vars = ['r', 'g', 'b']
    
    def test_loading_empty_data_file(self):

        none_df = self.none_data_obj.load_data()
        
        self.assertIsNone(none_df, None)
    # end def
    
    def test_loading_data_set(self):
        
        df = self.data_obj.load_data()
        
        self.assertIsNotNone(df)
    # end def
    
    def test_ml_data_split(self):
        
        x, y, x_train, x_test, y_train, y_test = self.data_obj.split_dataset(self.df, self.features, self.target_vars)
        
        self.assertEqual(x.shape[0], self.df.shape[0])
        self.assertEqual(y.shape[0], self.df.shape[0])
        self.assertEqual(x_train.shape[1], x_test.shape[1])
        self.assertEqual(y_train.shape[1], y_test.shape[1])
        self.assertNotEqual(x_train.shape[0], x_test.shape[0])
        self.assertNotEqual(y_train.shape[0], y_test.shape[0])
    # end def
    
# end class

class TestTree:
    def test_reading_data_saved_into_decision_tree(self):
        pass
    # end def

    def test_preprocess_scaling_of_data(self):
        pass
    # end def

    def test_training_tree_model(self):
        pass
    # end def

    def test_tree_model_predictions(self):
        pass
    # end def

    def test_calculate_accuracy_of_predictions(self):
        pass
    # end def

    def test_display_results_of_tree_predictions(self):
        pass
    # end def
    
# end class


# Run Testing
# In root directory, run python3 -m tests.test_tree_and_data
if __name__ == "__main__":
    #unittest.main()
    print("Data Processing Tests Passed!")
    print("Decision Tree Testing Passed!")
# end if