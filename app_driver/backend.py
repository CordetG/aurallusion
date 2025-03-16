#!/usr/bin/python3

# driver for backend method interactions

from utils.core_data import eval
from utils.mlsignals import tree

def run_ml_utils():
    
    ml_data_obj = eval.TreeData()
    df = ml_data_obj.load_data()
    features = ['soundFreq', 'octave', 'note']
    target_vars = ['r', 'g', 'b']
    x, y, x_train, x_test, y_train, y_test = ml_data_obj.split_dataset(df, features, target_vars)
    
    ml_model_obj = tree.DecisionTreeModel()
    ml_model_obj.read_data(x_train, y_train, x_test, y_test)
    
    ml_model_obj.preprocess_data()
    ml_model_obj.train()
    ml_model_obj.test()
    ml_model_obj.calculate_accuracy()
    
    ml_model_obj.display_results()
    ml_model_obj.plot_data()


if __name__ == "__main__":
    run_ml_utils()