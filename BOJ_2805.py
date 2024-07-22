import sys
input = sys.stdin.readline

def find_max_height(n, m, heights):
    low, high = 0, max(heights)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        total = sum((h - mid) for h in heights if h > mid)

        if total >= m:
            result = mid  # mid 높이로 충분한 나무를 얻을 수 있는 경우
            low = mid + 1
        else:
            high = mid - 1

    return result

# 입력 받기
N, M = map(int, input().split())
tree_heights = list(map(int, input().split()))

# 최대 높이 출력
print(find_max_height(N, M, tree_heights))
