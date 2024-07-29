from collections import deque

def last_card_remaining(N):
    queue = deque(range(1, N+1))
    
    while len(queue) > 1:
        queue.popleft()  # 제일 위 카드를 버린다.
        queue.append(queue.popleft())  # 그 다음 카드를 뒤로 옮긴다.
    
    return queue[0]

N = int(input())
print(last_card_remaining(N))
