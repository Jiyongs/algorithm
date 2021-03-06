# Algorithm (in python)

## hash
``` python
if 값 in 리스트
```
- return 리스트 안의 값 존재 여부

``` python
zip(리스트1, 리스트2)
```
- return object( 리스트1[0], 리스트2[0], ... )
- object를 list, dict, tuple, set 등 으로 변환하여 사용

``` python
dict(zip(리스트1, 리스트2))
```
- return { 리스트1[0] : 리스트2[0], ... }

``` python
sorted(딕셔너리.items(), key=(lambda x: x[0]), reverse=True)
```
- 딕셔너리의 key 값으로 내림차순하여 정렬 후 [(키, 값)] 형태로 반환
- 딕셔너리의 value 값으로 정렬하려면, key=(lambda x: x[1]) 로 변경

``` python
변수 = 값1 if 조건문 else 값2
```
- 조건문이 true면 값1 false면 값2 를 변수에 대입

``` python
from collections import Counter
Counter(리스트)
```
- return Counter({값1:건수, 값2:건수, ...})
- 리스트 값들의 고유 값(set(리스트)) 별 건수를 반환

``` python
for a, b in [["a", "b"]]:
    print(a, b)
```
- 이중리스트 안의 값 개수("a","b" : 2개)만큼 a,b 에 받아 옴
- 이중리스트 안의 값 개수가 모두 같아야 함
- 이중리스트 안의 값 개수와 for문 다음에 오는 변수 개수가 같아야 함

``` python
from itertools import combinations
combinations((리스트),조합개수)
```
- return 리스트 내 값으로 만들어지는 모든 조합 (순서고려 x, 중복 제거)

``` python
문자열1.startswith(문자열2)
```
- return 문자열1이 문자열2로 시작하는지의 여부

``` python
변수 in 리스트
변수 in 딕셔너리
```
- element 존재 검사 시, list보다 set이나 dict 이 빠름

## dfs/bfs
- dfs/bfs 사용 구분
- dfs/bfs
   - 그래프의 모든 정점을 방문하는 것이 중요한 문제에 둘 다 사용 가능
   - 그래프가 너무 크면 dfs, 크지 않고 검색시작지점 ~ 목적지 간 거리가 가까우면 bfs 가 효율적
- dfs
   - [구현 소스](https://github.com/Jiyongs/algorithm/blob/master/dfs_bfs/dfs_stack.py)
   - 최단거리로 갈 수 있는 경로의 개수
   - 목적지에 도착할 수 있는지 여부
   - 경로마다 제한 조건이 있는 문제
- bfs
   - [구현 소스](https://github.com/Jiyongs/algorithm/blob/master/dfs_bfs/bfs_queue.py)
   - 최단거리/경로
   - 가중치가 같을 때 최소비용/횟수

## sort
- 선택 정렬
  - [구현 소스](https://github.com/Jiyongs/algorithm/blob/master/sort/selection_sort.py)
  - 무작위로 나열된 숫자 데이터 중 가장 작은 것을 선택해 맨 앞의 것과 바꾸고, 그 다음 작은 것을 선택해 2번째 데이터와 바꾸는 과정을 반복
  - 매번 가장 작은 것을 선택
  - 데이터 개수가 10,000개 이상일 때 속도가 느려짐
  - O(N^2)
- 삽입 정렬
  - [구현 소스](https://github.com/Jiyongs/algorithm/blob/master/sort/insertion_sort.py)
  - 삽입할 대상의 값들이 이미 정렬되어 있다는 가정하에 특정 값을 적절한 위치에 삽입
  - 데이터가 거의 정렬되어 있는 경우에 효과적
  - 최선 : O(N) / 최악 : O(N^2)
- 퀵 정렬
  - [구현 소스](https://github.com/Jiyongs/algorithm/blob/master/sort/quick_sort.py)
  - 기준 값(피벗)을 정한 후 다음 큰 수와 작은 수를 교환하여 리스트를 반으로 나누는 방식
  - 데이터가 무작위로 섞인 경우 효과적이며, 데이터가 이미 정렬되어 있는 경우 느림
  - 평균 : O(NlogN) / 최악 : O(N^2)
- 계수 정렬
  - [구현 소스](https://github.com/Jiyongs/algorithm/blob/master/sort/count_sort.py)
  - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
  - 가장 큰 데이터와 작은 데이터 간 차이가 1,000,000을 넘지 않을 때 효과적
  - 크기 범위가 0~999999인데 0과 999999만 존재하는 데이터의 경우 공간 복잡도에서 비효율적
  - 결론적으로, 데이터 크기가 한정되어 있고 데이터의 크기가 많이 중복된 경우에 유리함
  - O(N+K) *N: 데이터 개수, K: 데이터 중 최대값 크기
- 파이썬의 sorted()
  - [구현 소스](https://github.com/Jiyongs/algorithm/blob/master/sort/python_sort.py)
  - 파이썬의 기본 정렬 라이브러리 함수
  - 퀵 정렬과 비슷한 병합정렬 기반이며 최악의 경우에도 O(NlogN)을 보장
  
## search
- 순차 탐색
  - [구현 소스](https://github.com/Jiyongs/algorithm/blob/master/search/sequential_search.py)
  - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
  - 정렬되지 않은 리스트에서 데이터를 찾을 때 사용
  - 최악의 경우 O(N)
- 이진 탐색
  - [구현 소스](https://github.com/Jiyongs/algorithm/blob/master/search/binary_search.py)
  - 시작점, 끝점, 중간점의 변수 3개를 이용하여 찾으려는 데이터와 중간점 위치의 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법
  - 데이터가 정렬된 상태에만 사용 가능
  - O(logN)
- 이진 탐색 구현 시 주의사항
  - 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이라 입력 데이터가 너무 많은 경우, input()은 시간초과 가능성 있음.   
    따라서, sys 라이브러리의 readline()을 사용하는 게 낫다.   
    readline() 사용 후에 rstrip()을 호출해야 엔터로 인한 줄 바꿈 기호가 제거된다.
    ``` python
    # 문자열 1개 입력받기
    import sys
    input_data = sys.stdin.readline().rstrip()
    ```
    
## 다이나믹 프로그래밍 
- 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 해결하는 알고리즘
- 다이나믹 프로그래밍 기법을 사용할 수 있는 조건
  ```
  1. 큰 문제를 작은 문제로 나눌 수 있다.
  2. 작은 문제에서 구한 답은 그것을 포함하는 큰 문제에서도 동일하다.
  ```
- 구현 방법
  - 메모이제이션 (= 캐싱) : 한 번 구한 결과를 메모리에 저장해두고 같은 식을 다시 호출할 때 저장된 값을 사용하는 기법

## 최단경로
- 가장 짧은 경로 또는 거리를 찾는 알고리즘
- 최단 거리가 가장 짧은 노드를 찾을 때 순차탐색이 아닌, heap 구조를 사용하자
  ```
  heap
  - 우선순위 큐를 구현하기 위해 사용하는 자료구조
  - 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제한다.
  - python 에서는 PriorityQueue 또는 heapq를 제공하는데, heapq가 더 빠르다.
  - heapq는 기본적으로 최소 힙 구조 (기준 값이 가장 낮은 데이터부터 삭제)를 이용한다.
  - heapq를 최대 힙으로 사용하려면, 우선순위 기준 값에 음수(-) 값을 붙였다가, 값을 꺼내서 사용할 때 다시 음수(-) 값을 붙여서 사용하자.
  ```
- [다익스트라 알고리즘](https://github.com/Jiyongs/algorithm/blob/master/shortest_path/dijkstra_improved.py)
- [플로이드 워셜 알고리즘](https://github.com/Jiyongs/algorithm/blob/master/shortest_path/floyd_warchall.py)
