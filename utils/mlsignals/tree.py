#!/usr/bin/python3

# core_data module --> data splitting and processing.

# The decision tree module is responsible for 
# data fitting the model to the training data, 
# making predictions, and evaluating performance.

# Responsible for the machine-learning specific tasks.

from sklearn.tree import DecisionTreeRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

class DecisionTreeModel:
    '''Multi-Output Decision Tree Regressor Model'''
    
    def __init__(
            self, 
            x_train=None, y_train=None,
            x_test=None, y_test=None,
            scaled_model=None,
            criterion='friedman_mse', random_state=93, depth=None,
            predictions=None, mse=None
        ):
        
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.scaled_data: Pipeline = scaled_model
        self.model = DecisionTreeRegressor(
                        criterion=criterion,
                        random_state=random_state, 
                        max_depth=depth
                    ) 
        self.multi_model = MultiOutputRegressor(self.model)
        self.predictions = predictions
        self.mse = mse
    # end __init__ def
    
    # Create new instance of the decision tree
    def new_model(
            self, 
            new_criterion, 
            new_rand, 
            new_depth
        ):
        
        return DecisionTreeModel(
                criterion=new_criterion,
                random_state=new_rand,
                depth=new_depth
            )
    # end def
    
    # Scales the data prior to training the model
    def preprocess_data(self) -> Pipeline:
        
        self.scaled_data = Pipeline(steps=[
                        ('scaler', StandardScaler()),
                        ('regressor', self.multi_model)
                    ])
    # end def
    
    def read_data(
            self, 
            x_train, 
            y_train, 
            x_test, 
            y_test
        ) -> None:
        
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
    # end def
    
    # fitted data
    def train(self) -> None:
        
        self.scaled_data.fit(self.x_train, self.y_train)
    # end def
    
    # predict after fitting data
    def test(self) -> None:
        
        self.predictions = self.scaled_data.predict(self.x_test)
        self.predictions = np.round(self.predictions).astype(np.uint8)
    # end def
        
    def calculate_accuracy(self) -> None:
        
        self.mse = mean_squared_error(self.y_test, self.predictions)
    # end def
    
    def display_results(self) -> None:
        
        print(f'Mean Squared Error (MSE) for RGB prediction: {self.mse}')
        
        self.plot_data()
    # end def
    
    def plot_data(self) -> None:
        # TODO: Find a better graph to display results & move to core_data/eval
        
        # Some matplotlib syntax help from chatGPT
        plt.figure(figsize=(12, 6))

        # x-axes = 'r','g','b' values between 0-255
        # y-axes = frequency of certain values occur
        plt.subplot(1, 2, 1)
        plt.hist(self.y_test.to_numpy().ravel(), bins=50, color='blue', alpha=0.5, label="Actual")
        plt.hist(self.predictions.ravel(), bins=50, color='red', alpha=0.5, label="Predicted")
        plt.legend()
        plt.title("Distribution of Actual vs Predicted Values")

        plt.subplot(1, 2, 2)
        # Check the delta (difference between actual and predicted)
        deltas = self.y_test - self.predictions
        plt.hist(deltas.to_numpy().ravel(), bins=50, color='green', alpha=0.7)
        plt.title("Deltas (Actual - Predicted)")

        plt.tight_layout()
        plt.show()      
    # end def
    
#end class
