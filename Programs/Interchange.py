def interchange(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]

    return lst

l = [33, 56, 89 , 11, 99]
print(interchange(l))

# Swap in list
def swap_elements(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]

l = [33, 56, 89, 11, 99]
swap_elements(l, 0, -1)
print(l)