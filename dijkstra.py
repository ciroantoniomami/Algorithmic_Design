from binheap import binheap
from graph import Edge,Graph,printGraph



def vertex_order(a, b):
  return a[1] <= b[1]


def Relax(G,Heap,u,v,w):
    #u[1] is the distance of u, G.V[v][0] is the distance of v
    if u[1] + w < G.V[v][0]:

        size = Heap._size
        for i in range(0, size):
            if Heap._A[i][0] == v:
                index = i

        Heap.decrease_key(index,(v,u[1] + w))

        G.V[v][0] = u[1] + w 
        G.V[v][1] = u[0]

def Dijkstra(G,s):
    G.V[s][0] = 0


    V = [(value,G.V[value][0]) for value in G.V.keys()]

    Heap = binheap(V,vertex_order)
    while not Heap.is_empty():
        #remove the pair of value and distance
        u = Heap.remove_minimum()

        #G.adj[u[0]] return the element of the dict which key is the value of u
        for edge in G.adj[u[0]]:

            Relax(G,Heap,u,edge[0],edge[1])








if __name__ == '__main__':
    vertices = [1,2,3,4,5,6]
    edges = [Edge(1, 2, 1), Edge(1, 3, 5), Edge(2, 6, 15), Edge(3, 4, 2),
            Edge(4, 5, 1), Edge(5, 6, 3)]
    
    graph = Graph(edges, vertices)

    printGraph(graph)
    H = Dijkstra(graph,1)
    printGraph(graph)




 



