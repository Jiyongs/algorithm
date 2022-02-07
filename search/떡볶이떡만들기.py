# 떡볶이 떡의 높이 h가 주어졌을 때, 떡을 1번만 절단할 수 있다.
# 높이가 h보다 높은 떡은 윗부분이 잘리고, 낮은 떡은 잘리지 않는다.
# 잘려나간 떡의 총 길이만큼 손님에게 제공한다.
# 손님이 요청한 길이가 총 m일 때, 적어도 m 만큼의 떡을 얻기 위해 절단기에 설정해야 하는 높이의 최댓값을 구하라.

# +) 떡 높이의 총합은 항상 m 이상이다.
# +) 떡 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

n, m = map(int, input().split())
dduck_highs = list(map(int, input().split()))

# my answer
# 순차 탐색 방법이라, 절단기의 높이가 최대 10억까지의 정수이므로 최악의 경우 시간 초과될 가능성이 있다.
max_h = max(dduck_highs)-1
sum_h = 0
while sum_h != m:
    for dduck_h in dduck_highs:
        slice_h = dduck_h - max_h
        if slice_h > 0:
            sum_h += slice_h
    if sum_h != m:
        sum_h = 0
        max_h -= 1

print(max_h)

# book's answer
# 이진 탐색 문제이자, 파라메트리 서치 유형의 문제이다.
# 파라메트리 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
# 우선, 절단기 높이의 최대 값은 가장 높은 떡의 높이로 설정한다.
# 1. 시작점은 0, 끝점은 19로 설정하고, 이의 중간점인 9를 절단기 높이라고 설정했을 때 얻는 떡의 길이는 25cm 이다.
# 2. 25>6(필요한 길이)이므로, 시작점을 증가시켜서 1을 반복한다.
# 3. 절단하여 얻는 떡의 길이가 6cm가 될 때까지 반복한다.
def binary_solution(dduck_highs, target, start, end):
    result = 0
    while start <= end:
        sum_h = 0
        mid = (start + end) // 2
        for dduck_h in dduck_highs:
            if dduck_h > mid:
                sum_h += dduck_h - mid
        if sum_h < target: # 떡의 길이가 부족한 경우
            end = mid - 1
        else: # 떡의 길이가 충분한 경우
            result = mid # target과 완전 동일하지 않을 경우를 대비하여, result 기록
            start = mid + 1
    return result

dduck_highs.sort()
print(binary_solution(dduck_highs, m, 0, dduck_highs[n-1]))