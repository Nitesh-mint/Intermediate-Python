from Node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp
    def size(self):
        count = 0
        current = self.head 
        while current != None:
            count += 1 
            current = current.get_next()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                fount = True
            else:
                current = current.get_next()
            return found

