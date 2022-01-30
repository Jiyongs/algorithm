# 계수 정렬 # 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
# 가장 큰 데이터와 작은 데이터 간 차이가 1,000,000을 넘지 않을 때 효과적 # O(N+K) *N: 데이터 개수, K: 데이터 중 최대값 크기
# 크기 범위가 0~999999인데 0과 999999만 존재하는 데이터의 경우 공간 복잡도에서 비효율적
# 결론적으로, 데이터 크기가 한정되어 있고 데이터의 크기가 많이 중복된 경우에 유리함

# my answer
def sort(arr):
    answer = dict.fromkeys((x for x in range(len(arr))), 0)
    for a in arr:
        answer[a] += 1
    for aa in answer:
        for cnt in range(answer[aa]):
            print(aa, end=' ')

# other answer
def sort_2(arr):
    # 모든 범위를 포한하는 리스트 선언 (0으로 초기화)
    count = [0] * (max(array) + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
        for j in range(count[i]):
            print(i, end=' ')

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
sort(array)
print()
sort_2(array)