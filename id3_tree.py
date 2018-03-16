#!/usr/bin/env python
from treelib import Node, Tree

def get_tree(data):
    '''
       Take data, get a decision tree based on the id3 algorithm.
    '''
    pass

class id3_tree(Tree):
    '''
       id3_tree should be able to output several things:
           * Show a trace of how decision tree was built
           ** Show entropy step
           ** Show information gain step
           * Show a representation of the tree
           * A classifier that can take data and give a classification

       functional methods:
           * Modify tree based on hyper-parameters
           ** Depth

       in addition some utility methods might be nice:
           * take representation of decision tree, build object

    '''
    def __init__(self):
        super(id3_tree, self).__init__()
