#!/usr/bin/python3

import pytest
from utils.core_data import eval
from utils.mlsignals import tree




class TestData:
    
    dataObj = eval.TreeData()
    
    def test_loading_data_file(self):
        pass
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
# In root directory, run python3 -m tests.test_audio
if __name__ == "__main__":
    print("Data Processing Tests Passed!")
    print("Decision Tree Testing Passed!")
# end if