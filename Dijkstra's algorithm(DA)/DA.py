from heapq import *
def dijkstra(graph, start):
    vnum = len(graph) # Number of vertices
    paths = {}
    cands = [(0,start,start)]
    heapify(cands) # Convert to a top heap, which is easier to find the edge with the least weight
    count = 0
    while count < vnum and cands is not None:
        print(cands)
        plen,u,vmin=heappop(cands) # Pick up the edge with the shortest cumulative path
        if paths.get(vmin) is not None: # Skip if the shortest path to vmin is already found
            continue
        paths[vmin] = plen # Save shortest path
        for next_edge in graph[vmin]:
            if not paths.get(next_edge[2]):
                heappush(cands, (plen+next_edge[0],u,next_edge[2]))
        count += 1
    return paths
graph = {'A': [(7, 'A', 'B'), (5, 'A', 'D')],
         'C': [(8, 'C', 'B'), (5, 'C', 'E')],
         'B': [(7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E')],
         'E': [(7, 'E', 'B'), (5, 'E', 'C'), (15, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G')],
         'D': [(5, 'D', 'A'), (9, 'D', 'B'), (15, 'D', 'E'), (6, 'D', 'F')],
         'G': [(9, 'G', 'E'), (11, 'G', 'F')],
         'F': [(6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G')]}

print(dijkstra(graph, 'A'))
