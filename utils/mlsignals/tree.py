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
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
import matplotlib.pyplot as plt

class DecisionTreeModel:
    '''Regression Decision Tree Model'''
    
    # Random state set to 100 for reproducibility
    def __init__(self, random_state=100):
        self.model = DecisionTreeRegressor(random_state=random_state)
    # end def
    
#end class
