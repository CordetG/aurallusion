#!/usr/bin/python3

# driver to communicate between frontend & backend

from utils.core_data import eval
from utils.mlsignals import tree

def main() -> int:
    return 0

# end main

def run_ml_utils():
    
    ml_model_obj = tree.DecisionTreeModel()
    model = ml_model_obj.load_trained_data()

# end def



if __name__ == '__main__':
    pass