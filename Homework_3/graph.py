

#A class for edges, properties are source, destination and weight of the edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight



class Graph:
    def __init__(self, edges, nodes):

        self.V = nodes 

        #the adjiancency list is a dictionary where the key is the src and the value are list of pairs of dest and weight
        self.adj = {}
        for i in nodes:
            self.adj[i] = []
 
        if edges is not None:
            for e in edges:

                self.adj[e.src].append((e.dest,e.weight))




       
def printGraph(graph):
    for src in graph.adj.keys():

        for edge in graph.adj[src]:
            print(f"({src} —> {edge[0]}, {edge[1]}) ", end='')
        print()


 
 
if __name__ == '__main__':
 
    vertices = [1,2,3,4,5,6]
    edges = [Edge(1, 2, 1), Edge(1, 3, 5), Edge(2, 6, 15), Edge(3, 4, 2),
            Edge(4, 5, 1), Edge(5, 6, 3)]
 


 

    graph = Graph(edges, vertices)
    printGraph(graph)


 




