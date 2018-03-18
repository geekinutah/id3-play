#!/usr/bin/env python

from id3_tree import get_entropy
from pprint import pprint
from prettytable import PrettyTable
import features
import re

##Config vars##
training_file = 'training.data'
test_file = 'test.data'
parse_regex = '^([\+|\-]) (.*)$'
##/Config##


def parse(filename):
    """ Dict of Data """
    to_return = {}
    f = open(filename,'r')
    for line in f.readlines():
        m = re.match(parse_regex, line)
        result = m.groups()
        if result[0] == '+':
            to_return[result[1]] = True
        else:
            to_return[result[1]] = False

    return to_return

if __name__ == '__main__':
    pprint("Finding Entropies")
    training_data = parse(training_file)
    x = PrettyTable()
    x.field_names = ['feature_name', 'entropy']

    for f in features.get_feature_list():
        x.add_row([f, get_entropy(f, training_data)])

    print(x)
