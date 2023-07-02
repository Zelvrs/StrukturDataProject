print("================LINKED LIST================")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print("Data:", current.data)
            current = current.next

# Membuat linked list berisi data makanan
makanan = LinkedList()
makanan.add_node("Nasi Goreng")
makanan.add_node("Sate Ayam")
makanan.add_node("Gado-Gado")
makanan.add_node("Bakso")
makanan.add_node("Mie Ayam")

# Melakukan traversal linked list dan mencetak isi makanan
makanan.display()
