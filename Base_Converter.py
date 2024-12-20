from stack import Stack


def base_converter(number, base):
    # this is used to index and store the value later 
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while number > 0:
        rem = number % base
        rem_stack.push(rem)
        number = number // base
    
    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string

print(base_converter(233, 2))
print(base_converter(25, 16))
print(base_converter(25, 26))
