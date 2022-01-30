# 선택정렬 # 무작위로 나열된 숫자 데이터 중에서 가장 작은 것을 선택해 맨 앞의 것과 바꾸고, 그 다음 작은 것을 선택해 2번째 데이터와 바꾸는 과정을 반복
# 매번 가장 작은 것을 선택 # O(N^2) # 데이터 개수가 10,000개 이상일 때 속도가 느려짐
# 스와프 : 특정 리스트에서 두 변수의 위치를 서로 바꾸는 작업

# my answer
def sort(arr):
    answer = []
    len_arr = len(arr)
    for a in range(0, len_arr):
        answer.append(min(arr))
        for aa in answer:
            if aa in arr:
                arr.remove(aa)

    print(' '.join(map(str, answer)))

# other answer
def sort_2(arr):
    for i in range(len(arr)):
        min_index = i # 가장 작은 원소의 인덱스
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # 스와프

    print(arr)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
sort_2(array)
sort(array)
