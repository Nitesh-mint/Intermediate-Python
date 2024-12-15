#Using dequeue datastructure to solove palindrome
from dequeue import Dequeue

def palindrome_checker(word):
    char_deque = Dequeue()

    for char in word:
        char_deque.add_rear(char.lower())
    still_equal = True
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first!=last:
            still_equal = False
    return still_equal

print(palindrome_checker("Mom"))
