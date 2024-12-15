# A hybrid queue that can insert and remove element from any end.

class Dequeue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_front(self, item):
        return self.items.append(item)
    def add_rear(self, item):
        return self.items.insert(0, item)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def peek_front(self):
        return self.items[0]
    def peek_rare(self):
        return self.items[len(self.items) - 1]
