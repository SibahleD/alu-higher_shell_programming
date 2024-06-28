#!/usr/bin/python3
from copy import deepcopy

def new_in_list(my_list, idx, element):
    total = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= total:
        return my_list
    else:
        new_list = deepcopy(my_list)
        new_list[idx] = element
        return new_list
