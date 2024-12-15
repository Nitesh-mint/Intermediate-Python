# Tuple: ordered, immutable and allows multiple values
"""Tuple is efficient and faster than list"""

my_tuple = ("Nitesh", "Raya", 3 , 5, 5)
print(my_tuple)

# Removing duplicate items from the tuple
filtered_tuple = tuple(dict.fromkeys(my_tuple))
print(filtered_tuple)

"""Tuple needs , after an element if only one element is present in the tuple."""
one_element_wrong_tuple = (5) # This is recognized not as tuple
one_element_correct_tuple = (5,)
print(type(one_element_wrong_tuple))
print(type(one_element_correct_tuple))

"""Selecting elements with specific orders """
print(my_tuple[::2]) # Print all the elements starting with 0 - last index with jum step of 2

# writing a comment
