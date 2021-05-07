


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight



class Graph:
    def __init__(self, edges, vertices):
        
        #a dictionary where the key is the value of the node and the value are pairs of distance from the src and the predecessor
        self.V = {value: [float('inf'),None] for value in vertices}

        #the adjiancency list is a dictionary where the key is the src and the value are list of pairs of dest and weight
        self.adj = {}
        for i in vertices:
            self.adj[i] = []
 

        for e in edges:
            
            self.adj[e.src].append((e.dest,e.weight))

       
def printGraph(graph):
    for src in graph.adj.keys():

        for edge in graph.adj[src]:
            print(f"({src} —> {edge[0]}, {edge[1]}) ", end='')
        print()

    print(graph.V)
 
 
if __name__ == '__main__':
 
    vertices = [0,1,2,3,4,5]
    edges = [Edge(0, 1, 6), Edge(1, 2, 7), Edge(2, 0, 5), Edge(2, 1, 4),
            Edge(3, 2, 10), Edge(4, 5, 1), Edge(5, 4, 3)]
 

    N = 6
 

    graph = Graph(edges, vertices)
 

    printGraph(graph)

    c = graph.V[2]
    print(c[0])
