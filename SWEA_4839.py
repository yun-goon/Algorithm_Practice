
'''
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.
'''

def b_s(l, r, cnt, target_page):
    c = int((l+ r)/2) 
    cnt +=1
    if c == target_page:
        return cnt
    elif c > target_page: # r 갱신
        return b_s(l,c,cnt, target_page)
    elif c < target_page: # l 갱신
        return b_s(c, r, cnt,target_page)

T = int(input())

for i in range(1, T+1):
    l = 1
    P, Pa, Pb = map(int, input().split())
    r = P
    cnt1, cnt2 = 0, 0
    cnt1= b_s(1, P, 0, Pa)
    cnt2 = b_s(1, P, 0, Pb)
    if cnt1 < cnt2:
        print(f"#{i} A")
    elif cnt1 > cnt2:
        print(f"#{i} B")
    elif cnt1 == cnt2:
        print(f"#{i} 0")


'''
3항 연산자
ans = 0 if A == b else 'A' if B> A else 'B'

'''