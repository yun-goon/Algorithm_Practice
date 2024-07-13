T = int(input())

def check_palin(word):
    l, r = 0, M-1

    while l< r:
        if word[l] != word[r]:
            return False
        else:
            l += 1
            r -= 1
    return True



def find_palin(board):
    for line in board:
        for i in range(N-M+1):
            word = line[i:i+M]
            if check_palin(word):
                # print(f"#{tc} {word}")
                return word
    return False


for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    if find_palin(board):
        print(f"#{tc} {find_palin(board)}")
        continue

    rotated_board = [''.join(line) for line in zip(*board)] # 앤 리스트로 만듦
    
    # rotated_board = list(zip(*board)) : #앤 튜플로 돼있음
    print(f"#{tc} {find_palin(rotated_board)}")

