#!/usr/bin/python3
def element_at(my_list, idx):
    b = len(my_list)
    if idx < 0:
        return None
    elif idx > b:
        return None
    else:
        return my_list[idx]
