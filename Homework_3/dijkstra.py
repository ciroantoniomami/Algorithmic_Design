from binheap import binheap
from graph import Edge,Graph,printGraph
import time


def vertex_order(a, b):
  return a[1] <= b[1]


def Relax(G,Heap,u,v,w,distance,pred):
    
    if distance[u-1] + w < distance[v-1]:

        Heap.decrease_key(v,(v,distance[u-1] + w))

        distance[v-1] = distance[u-1] + w 
        pred[v-1] = u

def Dijkstra(G,s):
    if s not in G.vertices:
          raise RuntimeError(f'{s} is not in the Graph')
    #the distance are stored in a list, we must remember that since the index of list goes from 0 to size-1 every time we want to access the distance
    #of value i, we must access the index i-1
    distance = [float('inf') for _ in G.vertices]
    #the same for the predecessor
    pred = [None for _ in G.vertices]
    distance[s-1] = 0


    V = [(value,float('inf')) if (value != s) else (value,0) for value in G.vertices]

    Heap = binheap(V,vertex_order)

    while not Heap.is_empty():
        #remove the pair of value and distance
        u , _ = Heap.remove_minimum()


        #G.adj[u[0]] return the element of the dict which key is the value of u
        for edge in G.adj[u]:

        
            #edge[0] is the value connected with u and edge[1] the weight of the path
            Relax(G,Heap,u,edge[0],edge[1],distance,pred)
        
    return distance,pred

def contract(G,value,contracted):
    if value not in G.vertices:
          raise RuntimeError(f'{value} is not in the Graph')
    #let's find the vertices for which the value is a destination 
    source = []
    for key in G.adj.keys():
        if key not in contracted:
            for edge in G.adj[key]:
                #If dest = value
                if edge[0] == value:
                    #I store both the value of the source and weight
                    source.append((key,edge[1]))
    
    for src , weight in source:
        
        for edge in G.adj[value]:
            if edge[0] not in contracted:
                distance = edge[1]+weight
                d , _ = contraction_Dijkstra(G,src,edge[0],distance,contracted)

                #I create a new edge only if the shortcut is shorter than the shortest distance not passing from s
                if distance <= d[edge[0]-1]:
                    G.adj[src].append((edge[0],distance))
    



#A modified version of Dijkstra suitable for the contraction problem
def contraction_Dijkstra(G,s,t,shortcut,contracted):
    if s not in G.vertices or t not in G.vertices:
          raise RuntimeError(f'{s} or' +  f' {t} is not in the Graph')
    distance = [float('inf') for _ in G.vertices]

    pred = [None for _ in G.vertices]
    distance[s-1] = 0


    V = [(value,float('inf')) if (value != s) else (value,0) for value in G.vertices]
 
    Heap = binheap(V,vertex_order)

    while not Heap.is_empty():
        #remove the pair of value and distance
        u , _ = Heap.remove_minimum()

        #if I extract my destination t, then I know that I've already computed the min distance and so I can return the distance
        if u == t: return distance,pred
        
        if u not in contracted:
            #G.adj[u[0]] return the element of the dict which key is the value of u
            for edge in G.adj[u]:
                #I do not need to check for the path which pass from the vertex already contracted, indeed we already inserted the shortcut in the graph
                if edge[0] not in contracted:
                    #If I found an edge whose weight is bigger than the shortcut I already have found in the contract function I can be sure that any path from s to t 
                    #which pass from that edge is longer than my shortcut and so I can avoid computing relax (this reduce a lot the complexity)
                    if edge[1] > shortcut: break    
                    #edge[0] is the value connected with u and edge[1] the weight of the path
                    Relax(G,Heap,u,edge[0],edge[1],distance,pred)
        
    return distance,pred






def BiDijkstra(G,s,t):
    if (s not in G.vertices or t not in G.vertices):
          raise RuntimeError(f'{s} or' + f' {t} is not in the Graph')
    contracted = []
    for vertex in G.vertices:

            contracted.append(vertex)
            contract(G,vertex,contracted)
         
         

    #I allocate two new graph, in the forward will be only the edges which go from a smaller value to bigger ones, viceversa on the backward
    # moreover, in the backward graph the edges will be reversed, src will become dest and viceversa   
    forward = Graph(None,G.vertices)
    backward = Graph(None,G.vertices)

    for src in G.adj.keys():
        for edge in G.adj[src]:
            if edge[0] > src : forward.adj[src].append((edge[0],edge[1]))
            else : backward.adj[edge[0]].append((src,edge[1]))
    print("froward")

    printGraph(forward)
    print("back")
    printGraph(backward)


    #I initiate two distance list, one for the distance from s and for the distance from t
    distance_s = [float('inf') for _ in G.vertices]
    pred_s = [None for _ in G.vertices]
    distance_s[s-1] = 0
    distance_t = [float('inf') for _ in G.vertices]
    pred_t = [None for _ in G.vertices]
    distance_t[t-1] = 0



    Heap_s = binheap([(value,float('inf')) if (value != s) else (value,0) for value in G.vertices],vertex_order)
    Heap_t = binheap([(value,float('inf')) if (value != t) else (value,0) for value in G.vertices],vertex_order)

    d = float('inf') 


    while not Heap_s.is_empty() and not Heap_t.is_empty():

        u , _ = Heap_s.remove_minimum()

        v , _ = Heap_t.remove_minimum()



        for edge_s in forward.adj[u]:



            Relax(G,Heap_s,u,edge_s[0],edge_s[1],distance_s,pred_s)
            
            #I update the distance, if both s and t have a connection with edge_s[0] than the sum will be finite, otherwise infinite, if it is finite
            #we update only if it is smaller than the already existing distance
            d = min(d,distance_s[edge_s[0]-1] + distance_t[edge_s[0]-1])

        for edge_t in backward.adj[v]:


            Relax(G,Heap_t,v,edge_t[0],edge_t[1],distance_t,pred_t)

            
            d = min(d,distance_t[edge_t[0] -1] + distance_s[edge_t[0]-1])
            

    return d

        
            
    


    





if __name__ == '__main__':
    vertices = [1,2,3,4,5,6,7,8]
    edges = [Edge(1, 6, 1), Edge(5, 1, 3), Edge(1, 5, 1), Edge(5, 6, 1),
            Edge(6, 8, 1), Edge(8, 1, 1),Edge(8,7,1),Edge(7,8,1),Edge(4,8,3),Edge(4,7,1),Edge(3,4,3),Edge(3,2,1),Edge(2,3,2)]
    
    graph = Graph(edges, vertices)



    d,p = Dijkstra(graph,1)
    for i in graph.vertices:
        print(i,":",d[i-1],p[i-1])

    t0 = time.time()
    print(BiDijkstra(graph,2,6))
    printGraph(graph)
    t1 = time.time()
    print(t1-t0)





 



