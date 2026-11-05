from collections import deque

def is_bipartite(graph):
    color={}
    for node in graph:
        color[node]= -1

    for start_node in graph:
        if color[start_node]== -1:
            color[start_node]= 0
            queue = deque([start_node])

            while queue:
                u=queue.popleft()

                for v in graph[u]:
                    if color[v]== -1:
                        color[v]= 1 - color[u]
                        queue.append(v)
                    elif color[v]== color[u]:
                        return False, {}

    return True, color

graph1 = {
    'A':['B', 'D'],
    'B':['A','C'],
    'C':['B','D'],
    'D':['A','C']
}

graph2= {
    'A':['B','C'],
    'B':['A','C'],
    'C':['A','B']
}

print("Testing Graph 1:")
possible, colors = is_bipartite(graph1)
if possible:
    print("The graph is Bipartite!")
    print("Team 1:", [node for node in colors if colors[node] == 0])
    print("Team 2:", [node for node in colors if colors[node] == 1])
else:
    print("The graph is NOT Bipartite!")

print("\n-------------------\n")

print("Testing Graph 2:")
possible, colors = is_bipartite(graph2)
if possible:
    print("The graph is Bipartite!")
else:
    print("The graph is NOT Bipartite (Conflict found!)")