print("================QUEUE================")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

# Membuat queue berisi data warna
warna = Queue()
warna.enqueue("Merah")
warna.enqueue("Biru")
warna.enqueue("Hijau")
warna.enqueue("Kuning")

# Mengambil dan mencetak isi queue
while not warna.is_empty():
    print("Warna:", warna.dequeue())
