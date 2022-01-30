# sorted()는 파이썬의 기본 정렬 라이브러리 함수 # 퀵 정렬과 비슷한 병합정렬 기반이며 최악의 경우에도 O(NlogN)을 보장함
# list와 dict 에서 사용 가능하며, list를 리턴한다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 정렬된 리스트를 반환
result = sorted(array)
print(result)
print(array)

# 리스트 내부 원소를 바로 정렬
array.sort()
print(array)

# 딕셔너리 key를 통한 정렬
array = [('바나나', 2), ('사과', 5), ('당근', 3)]
result = sorted(array)
print(result)

# sorted 인자로 key를 지정하여 정렬
# 딕셔너리의 1번째 데이터를 키로 주기 위한 함수
def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)