my_list = [6, 4, 5, 2, 10, 19]
smallest = my_list[0]
for i in my_list:
    if i < smallest:
        smallest = i

# print(smallest)


import timeit

def printthem():
    for i in my_list:
        current_numer = i
        for j in range(6):
            if current_numer < my_list[j]:
                print(current_numer ,"is less than " , j)
            else:
                print(current_numer, "is greater than", my_list[j])

t1= timeit.Timer("printthem()", "from __main__ import printthem")
print(t1.timeit(number=1000), "milliseconds")
