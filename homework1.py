#!/usr/bin/env python

from cross_validate import get_sets
from id3_tree import get_tree
import features

##Config vars##
training_file = 'training.data'
test_file = 'test.data'
parse_regex = '^ ([\+|\-] (.*)$'
##/Config##


def parse(filename, feature_list):
    """ Dict of Data """
    f = open(filename,'r').readlines()
    for l in f:
        pass

if __name__ == 'main':
    training_data = parse(training_file)
    test_data = parse(test_file)
    k_folds = get_sets(training_data)
    for fold in k_folds:
        get_tree(fold.training_data,features.get_feature_list())
