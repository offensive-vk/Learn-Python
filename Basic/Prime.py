for i in range(2, 50 + 1):
    hai_Prime = True
    for j in range(2, i):
        if i % j == 0:
            hai_Prime = False
            break

    if hai_Prime:
        print(i)

