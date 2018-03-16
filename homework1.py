#!/usr/bin/env python3

from cross_validate import get_sets
from id3_tree import get_tree

##Config vars##
training_file = 'training.data'
test_file = 'test.data'
parse_regex = '^ ([\+|\-] (.*)$'


def parse(filename):
    pass

if __name__ == 'main':
    training_data = parse(training_file)
    test_data = parse(test_file)
    k_folds = get_sets(training_data)
    for fold in k_folds:
        get_tree(fold.training_data)
