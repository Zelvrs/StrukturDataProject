print("================STACK================")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

# Membuat stack berisi data buah
buah = Stack()
buah.push("Apel")
buah.push("Jeruk")
buah.push("Mangga")
buah.push("Pisang")

# Mengambil dan mencetak isi stack
while not buah.is_empty():
    print("Buah:", buah.pop())
