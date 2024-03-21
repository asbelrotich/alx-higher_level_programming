#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = my_list[:]
    if idx < 0 or len(my_list) <= idx:
        return tmp
    tmp[idx] = element
    return tmp
