# 화폐단위(k)가 적은 금액부터 큰 금액까지 확인하며, 차례대로 목표금액(i)을 만들 수 있는 최소한의 화폐 개수(a_i)를 찾기
# 점화식
#   - a_i-k 를 만들 방법이 존재하는 경우, a_i = min(a_i, a_i-k+1)
#   - a_i-k 를 만들 방법이 없는 경우, a_i = 10001 (*m 크기 제한이 10000이라, 불가능한 수로 10001을 설정)

# 정수 n, m 입력받기
n, m = map(int, input().split())
# n개의 화폐단위 정보 입력받기
arr = []
for i in range(n):
    arr.append(int(input()))

# dp 테이블
d = [10001] * (m+1)

# 보텀업 방식
d[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        # a_i-k 를 만들 방법이 존재하는 경우
        if d[j-arr[i]] != 10001:
            d[j] = min(d[j], d[j-arr[i]] + 1)

# a_i-k 를 만들 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else:
    print(d[m])