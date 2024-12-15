class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == [] #returns true if the self.item is empty
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
#Parenthesis checker
def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string):
        if symbol_string[index] == ")":
            # print("Found: ", symbol_string[index])
            if s.peek() == "(":
                # print("Popping : ",s.peek())
                s.pop()
                # print(s.items)
            else:
                balanced = False
                break
            index += 1
        else:
            # print("Pushing : ", symbol_string[index])
            s.push(symbol_string[index])
            index += 1
    if s.items == []:
        return balanced
    return False

#print(par_checker('((()))'))
#print(par_checker('(()'))
