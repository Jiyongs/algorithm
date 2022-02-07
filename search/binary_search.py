# 이진 탐색
# 데이터가 정렬된 상태에만 사용 가능
# 시작점, 끝점, 중간점의 변수 3개를 이용하여 찾으려는 데이터와 중간점 위치의 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법
# 시간복잡도는 O(logN)
# 구현방법은 1.재귀함수 2.단순 반복문의 2가지

# 1. 재귀함수
def binary_search_recursion(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 # 연산자 '//' : 몫을 얻음
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursion(array, target, start, mid-1)
    else:
        return binary_search_recursion(array, target, mid+1, end)

# 2. 단순 반복문
def binary_search_for(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search_recursion(array, target, 0, n-1)
# result = binary_search_for(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
