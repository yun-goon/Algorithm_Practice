import sys
input = sys.stdin.readline

def palin_check(word): # 회문인지 아닌지 확인
    l, r = 0, len(word) -1 

    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
            continue
        else:
            return False
    return True
# 끝까지 다 돌면 회문임    

T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    flag = False

    for i in range(k):
        for j in range(k):
            if i ==j: #같은 인덱스에서 뽑혔으면
                continue # 생략

            password = words[i] + words[j]
            if palin_check(password):
                print(password)
                flag = True
                break
        if flag == True:
            break
    else:
        print(0)

'''
2중 for 문 종료시키기
빠밤

1. flag 이용하기
flag 로 탈출!
- for 문이 중첩될수록 힘들다!

2. exit(0)

이건 실행계속 실행 해야하면 문제 발생

3. 함수처리!
2중for 문을 함수처리


'''


import sys
input = sys.stdin.readline



def palin_find():
    for i in range(k):
        for j in range(k):
            if i ==j: #같은 인덱스에서 뽑혔으면
                continue # 생략

            password = words[i] + words[j]
            if palin_check(password):
                print(password)
                return
    print(0)
def palin_check(word): # 회문인지 아닌지 확인
    l, r = 0, len(word) -1 

    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
            continue
        else:
            return False
    return True
# 끝까지 다 돌면 회문임    

T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    palin_find()

