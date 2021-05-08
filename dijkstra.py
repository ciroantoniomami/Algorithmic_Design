from binheap import binheap
from graph import Edge,Graph,printGraph
import copy


def vertex_order(a, b):
  return a[1] <= b[1]


def Relax(G,Heap,u,v,w,distance,pred):

    if distance[u] + w < distance[v]:

        size = Heap._size
        for i in range(0, size):
            if Heap._A[i][0] == v:
                index = i

        Heap.decrease_key(index,(v,distance[u] + w))

        distance[v] = distance[u] + w 
        pred[v] = u

def Dijkstra(G,s):
    distance = {value: float('inf') for value in G.vertices}

    pred = {value: None for value in G.vertices}
    distance[s] = 0


    V = [(value,distance) for value,distance in distance.items()]

    Heap = binheap(V,vertex_order)
    while not Heap.is_empty():
        #remove the pair of value and distance
        u = Heap.remove_minimum()

        #G.adj[u[0]] return the element of the dict which key is the value of u
        for edge in G.adj[u[0]]:
        
        #u[0] will be the value removed from the heap, edge[0] is the value connected with it and edge[1] the weight of the path
            Relax(G,Heap,u[0],edge[0],edge[1],distance,pred)
        
    return distance,pred


def BiDijkstra(G,s,t):
    for vertex in G.vertices:
        G.contract(vertex)
    distance_s = {value: float('inf') for value in G.vertices}
    pred_s = {value: None for value in G.vertices}
    distance_s[s] = 0
    distance_t = {value: float('inf') for value in G.vertices}
    pred_t = {value: None for value in G.vertices}
    distance_t[t] = 0

    Heap_s = binheap([(value,distance) for value,distance in distance_s.items()],vertex_order)
    Heap_t = binheap([(value,distance) for value,distance in distance_t.items()],vertex_order)

    d = float('inf') 

    invertedGraph = InvertGraph(G)

    while not (Heap_s.is_empty() & Heap_t.is_empty()):

        u = Heap_s.remove_minimum()

        v = Heap_t.remove_minimum()

        if u[0] == v[0]:

            d = distance_s[u[0]] + distance_t[v[0]]


        for edge_s in G.adj[u[0]]:

            if edge_s[0] > u[0]:
                Relax(G,Heap_s,u[0],edge_s[0],edge_s[1],distance_s,pred_s)

        for edge_t in invertedGraph.adj[v[0]]:
    
            if edge_t[0] < v[0]:
                Relax(G,Heap_t,v[0],edge_t[0],edge_t[1],distance_t,pred_t)
            
        for edge_s in G.adj[u[0]]:
            for edge_t in invertedGraph.adj[v[0]]:

                if edge_s[0] == edge_t[0]:

                    if (distance_s[u[0]] + edge_s[1] + edge_t[1] + distance_t[v[0]]) < d:
                        d = (distance_s[u[0]] + edge_s[1] + edge_t[1] + distance_t[v[0]])
        
        return d

        
            
    




def InvertGraph(G):
    invertedGraph = Graph(None,G.vertices)

    for src in invertedGraph.vertices:

        for edge in G.adj[src]:
            invertedGraph.adj[edge[0]].append((src,edge[1]))
            #invertedGraph.adj[src].remove((edge[0],edge[1]))
    return invertedGraph

    





if __name__ == '__main__':
    vertices = [1,5,6,8,7,4,3,2]
    edges = [Edge(1, 6, 1), Edge(5, 1, 3), Edge(1, 5, 1), Edge(5, 6, 1),
            Edge(6, 8, 1), Edge(8, 1, 1),Edge(8,7,1),Edge(7,8,1),Edge(4,8,3),Edge(4,7,1),Edge(3,4,3),Edge(3,2,1),Edge(2,3,2)]
    
    graph = Graph(edges, vertices)

    #printGraph(graph)
    #d,p = Dijkstra(graph,1)
    #printGraph(graph)
    
    G2 = InvertGraph(graph)
    #printGraph(G2)

    print(BiDijkstra(graph,2,6))





 



