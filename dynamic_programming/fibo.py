# 피보나치 수열 (재귀적)

# 그냥 재귀 > fibo(100)에도 수백억년 소요됨...
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1)+fibo(x-2)

# 메모이제이션 활용 > 0.1초 걸림
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))