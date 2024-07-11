#문제 풀이 3가지

N = int(input())
book_ranking = dict()

for _ in range(N):
    bookname = input()
    # print(bookname)

    #조건문
    if bookname in book_ranking:
        book_ranking[bookname] += 1
    else:
        book_ranking[bookname] = 1
    # print(book_ranking)
sorted_ranking = sorted(book_ranking.items(), key= lambda x: (-x[1], x[0]))
print(sorted_ranking[0][0])


# print(sorted_ranking.keys())
# print(book_ranking)
# print(sorted_ranking)


'''
#.get 매서드 활용
book_ranking[bookname] = book_ranking.get(bookname, 0) +1

#모듈 import
from collections import defaultdict

N = int(input())

book_ranking = defaultdict(int) #정수형 dict 생성

for _ in range(N):
    # book_ranking[bookname] # defaultdict여서 없는거에 접근하면 바로 생성됨

    book_ranking[bookname] += 1
'''