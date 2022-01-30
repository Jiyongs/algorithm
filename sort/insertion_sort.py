# 삽입 정렬 # 삽입할 대상의 값들이 이미 정렬되어 있다는 가정하에 특정 값을 적절한 위치에 삽입한다
# 데이터가 거의 정렬되어 있는 경우에 효과적 # 최선 : O(N) / 최악 : O(N^2)

def sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1): # i부터 0까지 1씩 감소
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j] # 왼쪽으로 한 칸씩 이동
            else:
                break
    print(' '.join(map(str, arr)))

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
sort(array)

'''
i=1 vs j=1
i=2 vs j=2, j=1
i=3 vs j=3, j=2, j=1
    if arr[3] < arr[2]: // 0 vs 9
        arr[3], arr[2] = arr[3-1], arr[3]   // [5, 7, 0, 9]
    if arr[2] < arr[1]: // 0 vs 7
        arr[2], arr[1] = arr[2-1], arr[2]   // [5, 0, 7, 9]
    if arr[1] < arr[0]: // 0 vs 5
        arr[1], arr[0] = arr[1-1], arr[1]   // [0, 5, 7, 9]
    else:
        break
'''

'''
init                                                                   / 7
5 vs 7                                                                 / 5, 7
9 vs 5, 9 vs 7                                                         / 5, 7, 9
0 vs 5                                                                 / 0, 5, 7, 9
3 vs 0, 3 vs 5                                                         / 0, 3, 5, 7, 9
1 vs 0, 1 vs 3                                                         / 0, 1, 3, 5, 7, 9
6 vs 0, 6 vs 1, 6 vs 3, 6 vs 5, 6 vs 7                                 / 0, 1, 3, 5, 6, 7, 9
2 vs 0, 2 vs 1, 2 vs 3                                                 / 0, 1, 2, 3, 5, 6, 7, 9
4 vs 0, 4 vs 1, 4 vs 2, 4 vs 3, 4 vs 5                                 / 0, 1, 2, 3, 4, 5, 6, 7, 9
8 vs 0, 8 vs 1, 8 vs 2, 8 vs 3, 8 vs 4, 8 vs 5, 8 vs 6, 8 vs 7, 8 vs 9 / 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
'''