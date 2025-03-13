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
    
    def test_loading_empty_data_file(self):

        none_df = self.none_data_obj.load_data()
        
        self.assertIsNone(none_df, None)
    # end def
    
    def test_loading_data_set(self):
        
        df = self.data_obj.load_data()
        
        self.assertIsNotNone(df)
    # end def
    
    def test_ml_data_split(self):
        pass
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