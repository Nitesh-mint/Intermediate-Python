from stack import Stack

def divide_by_2(dec_number):
    rem_stack= Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        # //(floor division) returns the largest integer less than or equal to the result.
        dec_number = dec_number // 2
    
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())
    
    return bin_string
print(divide_by_2(233))
