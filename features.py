#!/usr/bin/env python
import re
import sys

"""
Use this module to define features.
"""

def get_feature_list():
    not_feature = re.compile('^_.*')
    to_return = []

    for i in dir(sys.modules[__name__]):
        if not not_feature.match(i):
            to_return.append(i)

    for i in ['re','sys','get_feature_list']:
        to_return.remove(i)

    return to_return

def _get_names(name):
    to_return = {}
    names = name.split(' ')
    to_return['first_name'] = names[0]
    to_return['last_name'] = names[-1]
    to_return['middle_names'] = []

    if len(names) > 1:
        to_return['middle_names'].append(names[1:-2])

    to_return['all_names'] = names
    return to_return

def _letter2int(one_char):
    return ord(one_char.lower()) - 97

def _is_vowel(one_char):
    return one_char.lower() in ['a','e','i','o','u']

def first_longer_than_last(name):
    n = _get_names(name)
    return len(n['first_name']) > len(n['last_name'])

def has_middle_name(name):
    n = _get_names(name)
    return len(n['all_names']) > 2

def first_and_last_end_same_letter(name):
    n = _get_names(name)
    return n['first_name'][-1] == n['last_name'][-1]

def first_alphabetically_before_last(name):
    n = _get_names(name)
    return _letter2int(n['first_name'][0]) < _letter2int(n['last_name'][0])

def second_letter_of_first_name_vowel(name):
    n = _get_names(name)

    if len(n['first_name']) < 2:
        return False

    return _is_vowel(n['first_name'][1])

def name_sum_is_even(name):
    sum_of_letters = 0
    for i in name:
        sum_of_letters = sum_of_letters + _letter2int(i)

    return ~ (int(sum_of_letters) % 2)

def first_name_begins_with_vowel(name):
    return _is_vowel(name[0])

def last_name_begins_with_vowel(name):
    n = _get_names(name)
    return _is_vowel(n['last_name'][0])
    pass

#def vowels_greater_than_number(name, num_of_vowels):
    #vowel_count = 0
    #for i in name:
        #if _is_vowel(i):
            #vowel_count = vowel_count + 1

def any_name_begins_with_a_vowel(name):
    n = _get_names(name)

    for i in n['all_names']:
        if _is_vowel(i[0]):
            return True

    return False
