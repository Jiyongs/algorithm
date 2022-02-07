# 부품이 n개 있다.
# 각 부품은 정수 형태의 고유번호를 가진다.
# 손님이 m개 종류의 부품을 대량 구매하겠다며 견적서를 요청했다.
# 손님이 문의한 부품이 모두 있는지 확인하는 코드를 작성해보자.

n = int(input())
stocks = list(map(int, input().split()))
m = int(input())
requests = list(map(int, input().split()))

# 이진 탐색
answer = []
def solution(stocks, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if stocks[mid] == target:
            answer.append("yes")
            return
        elif stocks[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    answer.append("no")

stocks.sort()
for r in requests:
    solution(stocks, r, 0, n-1)
print(' '.join(map(str, answer)))

# 계수 정렬
array = [0] * 1000001
for i in stocks:
    array[int(i)] = 1
for r in requests:
    if array[r] == 1:
        print("yes", end = " ")
    else:
        print("no", end = " ")

# 집합 자료형
for r in requests:
    if r in stocks:
        print("yes", end = " ")
    else:
        print("no", end = " ")
