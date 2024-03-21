#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        small_string = my_string.translate({ord("c"): None})
        capital_string = small_string.translate({ord("C"): None})
        return capital_string
    return my_string
