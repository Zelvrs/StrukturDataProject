from collections import defaultdict

print("================GRAPH================")
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print("Kota:", node)
                stack.extend(self.graph[node][::-1])

# Membuat graph berisi data kota
graph = Graph()
graph.add_edge('Jakarta', 'Bandung')
graph.add_edge('Jakarta', 'Surabaya')
graph.add_edge('Bandung', 'Yogyakarta')
graph.add_edge('Yogyakarta', 'Surabaya')
graph.add_edge('Surabaya', 'Malang')

# Melakukan traversal graph dan mencetak isi kota
graph.dfs('Jakarta')
