#!/usr/bin/python3

# core_data module --> data splitting and processing.

# The decision tree module is responsible for 
# data fitting the model to the training data, 
# making predictions, and evaluating performance.

# Responsible for the machine-learning specific tasks.

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.multioutput import MultiOutputRegressor
import matplotlib.pyplot as plot

class DecisionTreeModel:
    '''Multi-Output Decision Tree Regressor Model'''
    
    # Random state set to 100 for reproducibility
    def __init__(self, criterion='friedman_mse', random_state=100, depth=3):
        self.model = DecisionTreeRegressor(
                        criterion=criterion,
                        random_state=random_state, 
                        max_depth=depth
                    )
        
        self.multi_model = MultiOutputRegressor(self.model)
    # end __init__ def
    
    
    
#end class
