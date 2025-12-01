graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H", "F"],
    "F": ["G"],
    "G": [],
    "H": []
}

visited_dict = {
    "A": False,
    "B": False,
    "C": False,
    "D": False,
    "E": False,
    "F": False,
    "G": False,
    "H": False,
}

output_stack = []

def topology_sort(vertex, depth):
    print(f"{'__'*depth}At vertex: {vertex}")
    if not visited_dict[vertex]:
        visited_dict[vertex] = True
        for neighbour in graph[vertex]:
            print(f"{'__'*depth}Going to visit: {neighbour}")
            topology_sort(neighbour, depth + 1)
        print(f"{'__'*depth}Adding {vertex} to stack")
        output_stack.insert(0, vertex)
    print(f"{'__'*depth}Visited, do nothing")

for vertex in visited_dict:
    topology_sort(vertex, 0)

print(output_stack)
