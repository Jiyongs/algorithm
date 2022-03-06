# 피보나치 수열 (재귀적)

# 재귀 > fibo(100)에도 수백억년 소요됨... : O(2^N)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1)+fibo(x-2)

# 메모이제이션 + 재귀 (탑다운 방식) > 0.1초 걸림 : O(N)
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

# 반복문 (보텀업 방식)
d = [0] * 100
def fibo(x):
    d[1] = 1
    d[2] = 1
    for i in range(3, x+1):
        d[i] = d[i-1]+d[i-2]
    return d[x]

print(fibo(99))

# (참고) 시스템상 재귀함수의 스택 크기가 한정되어 있을 수 있다. sys의 setrecurtionlimit() 함수로 제한을 완화할 수 있다.