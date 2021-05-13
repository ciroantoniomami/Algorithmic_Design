#!/usr/bin/python3
from typing import TypeVar,Generic,List,Union
from numbers import Number 

T = TypeVar('T')

def min_order(a:Number, b:Number) -> bool:
  return a <= b

def max_order(a:Number, b:Number) -> bool:
  return a >= b
  
class binheap(Generic[T]):
  LEFT = 0
  RIGHT = 1

  def __init__(self, A:Union[int,List[T]],total_order=None): #A may be both an int or a List 
    if total_order is None:
      self._torder = min_order
    else:
      self._torder = total_order
    
    if isinstance(A,int):
      self._size = 0
      self._A = [None]*A
    
    else:
      self._size = len(A)
      self._A = A
    
    self.position = [value-1 for value,_ in self._A]
    
    
    self._build_heap()
  
  @staticmethod #you can remove self 
  def parent(node:int) -> Union[int,None]:
      if node == 0: #on the root
        return None
      return (node-1)//2
  
  @staticmethod
  def child(node:int,side:int) -> int: #side is left or right 
    return 2*node +1 + side 

  @staticmethod
  def left(node:int) -> int:
    return 2*node+1
  
  @staticmethod
  def right(node:int) -> int:
    return 2*node+2

  def __len__(self): #override
    return self._size
  
  def is_empty(self)-> bool:
    return self._size==0
  
  def _swap_keys(self,node_a:int,node_b:int) -> None:
    tmp = self._A[node_a]
    tmp_position = self.position[self._A[node_a][0]-1]
    self.position[self._A[node_a][0]-1] = self.position[self._A[node_b][0]-1]
    self._A[node_a] = self._A[node_b]
    self.position[self._A[node_b][0]-1] = tmp_position
    self._A[node_b] = tmp
  
  def _heapify(self,node:int) -> None: #root of subtree we are dealing with, iterative version
    keep_fixing = True
    
    while keep_fixing:
      min_node = node
      for child_idx in [binheap.left(node),binheap.right(node)]:
        if (child_idx < self._size and self._torder(self._A[child_idx],self._A[min_node])): #test if index is proper index
          min_node = child_idx
        
        #min_node is the index of the minimum key 
        #among the keys of root and its children
        
      if min_node != node:
          self._swap_keys(min_node,node)
          node = min_node
      else:
          keep_fixing=False

  def remove_minimum(self) -> T: #return and remove the minimum, so the root
    if self.is_empty():
      raise RuntimeError('The heap is empty')
    
    #last index in heap 
    #in position 0 there was the root
    self._swap_keys(0,self._size-1)
    #self._A[0] = self._A[self._size-1] loosing value of the root 
    
    self._size = self._size-1 #reduce size in term of index 

    #now we correct the heapify property
    self._heapify(0)
    
    return self._A[self._size] #returning the minimum, 
    #the before was on the root but now is swapped

  def _build_heap(self) -> None: #fix heap property bottom-up
    for i in range(self.parent(self._size-1),-1,-1):
      self._heapify(i)
  
  def decrease_key(self,node:int,new_value:T)->None:
    index= self.position[node-1]
    if self._torder(self._A[index],new_value):
      raise RuntimeError(f'{new_value} is not smaller than'+f'{self._A[node]}')
    


    self._A[index]=new_value
   
    parent = binheap.parent(index)
    while (index != 0 and not self._torder(self._A[parent],self._A[index])):
      self._swap_keys(index,parent)
      index = parent
      parent = binheap.parent(index)
  
  def insert(self,value:T) -> None:
    if self._size >= len(self._A):
      raise RuntimeError('the heap is full')
    
    if self.is_empty():
      self._A[0]=value
      self._size+=1
    else:  #for sure it have a parent
        parent = binheap.parent(self._size)
        if self._torder(self._A[parent],value):
          self._A[self._size] = value
          self._size += 1
        else: 
          self._A[self._size]=self.A[parent]
          self._size+=1
          self.decrease_key(self._size-1, value)


  def __repr__(self)->str:#take an instance of the class and return a string, printed as std output 
    bt_str = ''

    #level indexing pseudocode
    next_node = 1
    up_to = 2

    while next_node <= self._size:
      level = '\t'.join(f'{v}'for v in self._A[next_node-1:up_to-1])

      if next_node == 1:
        bt_str = level
      else: 
        bt_str += f'\n{level}'

      next_node = up_to
      up_to = 2*up_to

    return bt_str



     







