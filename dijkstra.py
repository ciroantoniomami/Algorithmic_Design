from binheap import binheap
from graph import Edge,Graph,printGraph
import time


def vertex_order(a, b):
  return a[1] <= b[1]


def Relax(G,Heap,u,v,w,distance,pred):
    
    if distance[u] + w < distance[v]:

        Heap.decrease_key(v,(v,distance[u] + w))

        distance[v] = distance[u] + w 
        pred[v] = u

def Dijkstra(G,s,t = None,shortcut = None):
    distance = {value: float('inf') for value in G.vertices}

    pred = {value: None for value in G.vertices}
    distance[s] = 0


    V = [(value,distance) for value,distance in distance.items()]

    Heap = binheap(V,vertex_order)

    while not Heap.is_empty():
        #remove the pair of value and distance
        u , _ = Heap.remove_minimum()


        if u == t: return distance,pred

        #G.adj[u[0]] return the element of the dict which key is the value of u
        for edge in G.adj[u]:

            if t is not None: 
                if edge[1] > shortcut: break

        
            #edge[0] is the value connected with u and edge[1] the weight of the path
            Relax(G,Heap,u,edge[0],edge[1],distance,pred)
        
    return distance,pred

def contract(G,value):

    #let's find the vertices for which the value is a destination 
    source = []
    for key in G.adj.keys():
        for edge in G.adj[key]:
            if edge[0] == value:
                source.append((key,edge[1]))
    
    for src , weight in source:
        
        for edge in G.adj[value]:

            distance = edge[1]+weight
            d , _ = Dijkstra(G,src,edge[0],distance)
            
            
            if distance <= d[edge[0]]:
                G.adj[src].append((edge[0],distance))
    






def BiDijkstra(G,s,t):
    for vertex in G.vertices:

         contract(G,vertex)

    #I allocate two new graph, in the forward will be only the edges which go from a smaller value to bigger ones, viceversa on the backward   
    forward = Graph(None,G.vertices)
    backward = Graph(None,G.vertices)

    for src in G.adj.keys():
        for edge in G.adj[src]:
            if edge[0] > src : forward.adj[src].append((edge[0],edge[1]))
            else : backward.adj[edge[0]].append((src,edge[1]))
        


    #I initiate two distance dicionary, one for the distance from s and for the distance from t
    distance_s = {value: float('inf') for value in G.vertices}
    pred_s = {value: None for value in G.vertices}
    distance_s[s] = 0
    distance_t = {value: float('inf') for value in G.vertices}
    pred_t = {value: None for value in G.vertices}
    distance_t[t] = 0



    Heap_s = binheap([(value,distance) for value,distance in distance_s.items()],vertex_order)
    Heap_t = binheap([(value,distance) for value,distance in distance_t.items()],vertex_order)

    d = float('inf') 


    while not (Heap_s.is_empty() & Heap_t.is_empty()):

        u , u_dist = Heap_s.remove_minimum()

        v , v_dist = Heap_t.remove_minimum()

        #If the backward path and the forward path arrive at the same verte we must stop and return the distance

        if u == v:

            d = distance_s[u] + distance_t[v]


        for edge_s in forward.adj[u]:



            Relax(G,Heap_s,u,edge_s[0],edge_s[1],distance_s,pred_s)
            
            #It could happen that we never arrive at a situation were u==v because s and t are connected by a vertex which is 
            d = min(d,distance_s[u] + edge_s[1] + distance_t[edge_s[0]])

        for edge_t in backward.adj[v]:


            Relax(G,Heap_t,v,edge_t[0],edge_t[1],distance_t,pred_t)
            d = min(d,distance_t[v] + edge_t[1] + distance_s[edge_t[0]])
            

        return d

        
            
    


    





if __name__ == '__main__':
    vertices = [1,2,3,4,5,6,7,8]
    edges = [Edge(1, 6, 1), Edge(5, 1, 3), Edge(1, 5, 1), Edge(5, 6, 1),
            Edge(6, 8, 1), Edge(8, 1, 1),Edge(8,7,1),Edge(7,8,1),Edge(4,8,3),Edge(4,7,1),Edge(3,4,3),Edge(3,2,1),Edge(2,3,2)]
    
    graph = Graph(edges, vertices)

    distance = {value: float('inf') for value in graph.vertices}

    pred = {value: None for value in graph.vertices}



    V = [(value,distance) for value,distance in distance.items()]

    Heap = binheap(V,vertex_order)

    #print(Heap)
    #Heap.decrease_key(4,(4,5))
    #print(Heap)
    #Heap.decrease_key(3,(3,6))
    #print(Heap)
    #Heap.remove_minimum()
    #Heap.decrease_key(3,(3,2))
    #print(Heap)
    #Heap.remove_minimum()
    #print(Heap) 
    #Heap.decrease_key(6,(6,2))
    #print(Heap)
    #Heap.remove_minimum()
    #print(Heap)
    d,p = Dijkstra(graph,1)
    print(d)

    t0 = time.time()

    print(BiDijkstra(graph,7,5))
    t1 = time.time()
    print(t1-t0)





 



