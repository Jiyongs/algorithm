n = int(input())

# dp 테이블
d = [0] * 1001

# 보텀업 방식
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796.796

print(d[n])