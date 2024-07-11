test = int(input())

def fibo(N):
    if N == 1 or N ==0:
        return N
    return fibo(N-1) + fibo(N-2)

print(fibo(test))