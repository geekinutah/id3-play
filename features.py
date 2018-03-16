#!/usr/bin/env python
import re

"""
Use this module to define features.
"""

def get_feature_list():
    not_feature = re.compile('^_.*')
    toreturn = []

    for i in dir():
        if not not_feature.match(i) and i != 'get_feature_list':
            toreturn.append(i)

    return toreturn
def first_longer_than_last(name):
    pass

def has_middle_name(name):
    pass

def first_and_last_end_same_letter(name):
    pass

def first_alphabetically_before_last(name):
    pass

def second_letter_of_first_name_vowel(name):
    pass

def name_sum_is_even(name):
    pass

def first_name_begins_with_vowel(name):
    pass

def last_name_begins_with_vowel(name):
    pass

def vowels_greater_than_number(name, num_of_vowels):
    pass

