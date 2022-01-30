# 퀵 정렬 # 기준 값(피벗)을 정한 후 다음 큰 수와 작은 수를 교환하여 리스트를 반으로 나누는 방식
# 값 들을 3파트로 나뉘어 생각  > 1파트: 1번째 값을 피벗으로 한 후, 피벗의 다음번째 왼쪽부터 피벗보다 큰 수(max)를 선택, 오른쪽끝부터 피벗보다 작은 수(min)를 선택하여 max와 min을 서로 스와핑. 이를 max와 min의 인덱스가 만날 때까지 반복.
#                               => 피벗을 기준으로 왼쪽은 피벗보다 작은 수, 오른쪽은 피벗보다 큰 수 들로만 구성됨
#                       > 2파트: 피벗의 왼쪽 값들에서, 1번째 값을 피벗으로 한 후, 1파트의 과정을 반복.
#                       > 3파트: 피벗의 오른쪽 값들에서, 1번째 값을 피벗으로 한 후, 1파트의 과정을 반복.
#                       > 1,2,3 파트를 모두 완료하면 결론적으로 정렬된 결과를 얻을 수 있음
# 평균 : O(NlogN) / 최악 : O(N^2) # 데이터가 무작위로 섞인 경우 효과적 # 데이터가 이미 정렬되어 있는 경우 느림

def sort(arr, start, end):
    if start >= end: # 원소가 1개일 때 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    sort(arr, start, right-1)
    sort(arr, right+1, end)

def sort_2(arr):
    # 리스트가 1개 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return sort_2(left_side) + [pivot] + sort_2(right_side)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
sort(array, 0, len(array)-1)
print(array)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(sort_2(array))