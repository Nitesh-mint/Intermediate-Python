#import Queue dataStructure
from queue import Queue 

def hot_potato(names_list, num): #names are players, num is the value how many times a round will last 
    circle = Queue()
    for name in names_list:
        circle.enqueue(name)

    while circle.size() > 1:
        for i in range(num):
            circle.enqueue(circle.dequeue())
        circle.dequeue()

    return circle.dequeue()

print(hot_potato(["Nitesh", "Ritika", "Kumar", "Shiva", "Adesh"],7))
