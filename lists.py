# Lists: ordered, mutable, allows duplicate elements
my_list = [1, 2, 3, 4, -1, -5]

print(my_list)
print(sorted(my_list))

"""Slicing the list 
Note: the last i.e 5th item is not printed only up to -1 is printed
"""
print(my_list[0:5])

print(my_list[::-1]) # Simple way to reverse a list

print("<------------------------>")

"""Copying list element to another list using different methods
"""
original_list = ["Nitesh", "Ram", "Unknown"]
list_copy1 = original_list  # Copy the item of the list
print(list_copy1)

list_copy1.append("Appended Item")
print(original_list)
print(list_copy1)

"""Using the copy method to copy item independently
"""
list_copy2 = original_list.copy()
list_copy2.append("Another appended Item")
print(original_list)
print(list_copy2)

"""Copy the list to another variable independently
"""
list_copy3 = [i for i in original_list]
list_copy3.append("Appended without modifying original list")
print(original_list)
print(list_copy3)

"""Removing duplicate items from the list"""
list_with_duplicate_items = [1,2,3,4,5,6,1,2]
filtered_list = list(dict.fromkeys(list_with_duplicate_items))
print(filtered_list)

"""Filtering items in the list """
list_to_filer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([item for item in list_to_filer if item % 2 == 0])

"""We can also use filter function to filter a list"""
# Filter function
def my_custom_filter(number):
    if number % 2 == 0:
        return number

filtered_list_with_custom_function =  list(filter(my_custom_filter, list_to_filer))
print(filtered_list_with_custom_function)

