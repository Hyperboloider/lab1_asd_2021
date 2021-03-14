from termcolor import colored

def input_matrix():
    size = int(input('Matrix size: '))
    matrix = []
    print("input matrix:")
    for _ in range(size):
        row = [int(i) for i in input().split()]
        matrix.append(row)
    print()
    return matrix

def hamilton(graph, current, seen = None, path = None):
    if path == None:                                               #first call creates auxiliary structures
        seen = [False] * len(graph)
        path = [current,]
    else:
        path.append(current)
        print("-".join([str(i + 1) for i in path]))
    if len(path) == len(graph):
        if graph[path[0]][path[-1]] == 1:                          #the head and the tail of the path have common edge
            print(colored("->".join([str(i + 1) for i in path]) + f"->{path[0] + 1}", "green"))
            return True
        else:
            path.pop()
            return False
    seen[current] = True
    for next_node in range(len(graph)):
        if graph[current][next_node] == 1 and not seen[next_node]: #the node has common edge with the current one and is not included into the current path
            if hamilton(graph, next_node, seen, path):
                return True
    seen[current] = False
    path.pop()
    return False

start = int(input('Strart node: ')) - 1
graph = input_matrix()
hamilton(graph, start)