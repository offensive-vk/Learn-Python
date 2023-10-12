def interchange(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]

    return lst

l = [33, 56, 89 , 11, 99]
print(interchange(l))
