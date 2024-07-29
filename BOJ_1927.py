import sys
input = sys.stdin.readline

N = int(input())
heap = ['-']


def heappush(heap, item):
    #1. 맨 뒤에 붙인다.
    heap.append(item)

    #2. 부모와 비교. 반복
    child = len(heap) - 1
    parent = child /2

    while parent and heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child] # 스왑
        child = parent
        parent = child//2


def heappop(heap):
    if len(heap) == 1: # 비어있으면
        return 0
    # 1. 루트 노드에서 뽑기
    result = heap[1]
    # 2. 맨뒤를 루트노드로 옮기기
    heap[1] = heap[-1]
    heap.pop()
    # 3. 자식 노드와 비교해서 옮길 수 있으면 스왑
    parent = 1
    child = parent * 2

    while child < len(heap) and heap[parent] > heap[child]: # 스왑조건
        # 3.1. 자식 노드 둘중에서 더 작은 곳으로 
        if child + 1 < len(heap) and heap[child +1] < heap[child]:
            child += 1

        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent*2

    return result


for _ in range(N):
    x = int(input())
    if x:
        heappush(x)
    else:
        print(heappop(x))