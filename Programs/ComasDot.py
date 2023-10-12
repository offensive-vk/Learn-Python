def swap_comas_and_dots(string):
    swapped_string = ""
    for char in string:
        if char == ",":
            swapped_string += "."
        elif char == ".":
            swapped_string += ","
        else:
            swapped_string += char
    return swapped_string


s = "Hello, World!"
swapped_s = swap_comas_and_dots(s)
print(swapped_s)
