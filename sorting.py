from typing import TypeVar, List, Optional

T = TypeVar('T')


def partition(A:List[T],begin:int,end:int,pivot:int) -> int: 
    A[begin] , A[pivot] = A[pivot] , A[begin]

    pivot = begin
    begin = begin + 1

    while begin <= end:

        if A[begin]>A[pivot]:
            A[begin] , A[end] = A[end] , A[begin]
            end = end - 1
        else:
            begin = begin + 1
    
    A[pivot] , A[end] = A[end] , A[pivot]

    return end


def quicksort(A:List[T],begin: Optional[int] = 0 , end: Optional[int] = None) -> None:

    if end is None:
        end = len(A) - 1


    while begin < end:
        p = partition(A,begin,end,begin)
        quicksort(A,begin,p-1)
        begin = p + 1


