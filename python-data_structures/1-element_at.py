#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        else:
            return my_list[idx]
def access_value():
    a = [2,4,6,8,10]
    print(element_at(a, -1))
access_value()
