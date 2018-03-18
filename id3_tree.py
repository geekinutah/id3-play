#!/usr/bin/env python
from treelib import Node, Tree
import math
import features

def get_tree(data):
    '''
       Take data, get a decision tree based on the id3 algorithm.
    '''
    pass

def get_entropy(feature, data):
    yes = 0
    no = 0
    for k in data.keys():
        if getattr(features, feature)(k):
            if data[k]:
                yes = yes + 1
            else:
                no = no + 1

    avg_yes = float(yes) / (len(data))
    avg_no = float(no) / (len(data))
    return abs( (avg_yes * math.log(avg_yes,2) ) - (avg_no * math.log(avg_no,2)) )

def  get_information_gain():
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
        Node()

