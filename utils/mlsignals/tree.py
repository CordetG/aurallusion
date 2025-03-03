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
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

class DecisionTreeModel:
    '''Multi-Output Decision Tree Regressor Model'''
    
    # Random state set to 100 for reproducibility
    def __init__(
            self, 
            x_train=None, y_train=None,
            x_test=None, y_test=None,
            criterion='friedman_mse', random_state=100, depth=3,
        ):
        
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        
        self.model = DecisionTreeRegressor(
                        criterion=criterion,
                        random_state=random_state, 
                        max_depth=depth
                    )
        
        self.multi_model = MultiOutputRegressor(self.model)
    # end __init__ def
    
    # Create new instance of the decision tree
    def new_model(self, new_criterion, new_rand, new_depth):
        
        return DecisionTreeModel(
                    criterion=new_criterion,
                    random_state=new_rand,
                    depth=new_depth
                )
    # end def
    
    # Scales the data prior to training the model
    def preprocess_data(self) -> Pipeline:
        
        scaled_data = Pipeline(steps=[
                        ('scaler', StandardScaler()),
                        ('regressor', self.multi_model)
                    ])
        
        return scaled_data
    # end def
    
    def read_data(self, x_train, y_train, x_test, y_test):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
    # end def
    
    def train(self, scaled_model):
        scaled_model.fit(self.x_train, self.y_train)
    # end def
        
#end class
