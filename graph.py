


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight



class Graph:
    def __init__(self, edges, vertices):

        self.vertices = vertices 

        #the adjiancency list is a dictionary where the key is the src and the value are list of pairs of dest and weight
        self.adj = {}
        for i in vertices:
            self.adj[i] = []
 
        if edges is not None:
            for e in edges:

                self.adj[e.src].append((e.dest,e.weight))

    def contract(self,value):

        #let's find the vertices for which the value is a destination 
        source = []
        for key in self.adj.keys():
            for edge in self.adj[key]:
                if edge[0] == value:
                    source.append((key,edge[1]))

        
        for src , weight in source:

            for edge in self.adj[value]:
                control = True
                for ed in self.adj[src]:
                    #if there is a direct path with the same vertex i check which is the shortest path
                    if edge[0] == ed[0]:

                        control = False
                        self.adj[src].remove((ed[0],ed[1]))
                        self.adj[src].append((ed[0],min(ed[1],edge[1]+weight)))

                if control == True and edge[0]!=src:
                    self.adj[src].append((edge[0],edge[1]+weight))
            #self.adj[src].remove((value,weight))

        #self.adj.pop(value)





       
def printGraph(graph):
    for src in graph.adj.keys():

        for edge in graph.adj[src]:
            print(f"({src} —> {edge[0]}, {edge[1]}) ", end='')
        print()


 
 
if __name__ == '__main__':
 
    vertices = [1,5,6,8]
    edges = [Edge(1, 6, 1), Edge(5, 1, 3), Edge(1, 5, 1), Edge(5, 6, 1),
            Edge(6, 8, 1), Edge(8, 1, 1)]
 


 

    graph = Graph(edges, vertices)
    printGraph(graph)
    graph.contract(1)

 

    printGraph(graph)


