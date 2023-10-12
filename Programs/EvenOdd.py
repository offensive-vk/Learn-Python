def Show(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    odd_numbers = [num for num in lst if num % 2 != 0]
    
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

numbers = [5, 2, 9, 1, 7]
Show(numbers)