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

class DecisionTreeModel:
    '''Multi-Output Decision Tree Regressor Model'''
    
    # Random state set to 100 for reproducibility
    def __init__(
            self, 
            x_train=None, y_train=None,
            x_test=None, y_test=None,
            scaled_model=None,
            criterion='friedman_mse', random_state=100, depth=3,
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
    def new_model(self, new_criterion, new_rand, new_depth):
        
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
    
    def read_data(self, x_train, y_train, x_test, y_test):
        
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
    # end def
    
    def train(self):
        
        self.scaled_model.fit(self.x_train, self.y_train)
    # end def
    
    def test(self):
        
        self.predictions = self.scaled_model.predict(self.x_test)
    # end def
        
    def calculate_accuracy(self):
        
        self.mse = mean_squared_error(self.y_test, self.predictions)
    # end def
    
    def display_results(self):
        
        print('Predictions for RGB values on test data:')
        print(self.predictions)
        
        print(f'Mean Squared Error (MSE) for RGB prediction: {self.mse}')
    # end def
    
#end class
