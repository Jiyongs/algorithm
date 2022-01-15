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
    - 최단거리로 갈 수 있는 경로의 개수
    - 목적지에 도착할 수 있는지 여부
    - 경로마다 제한 조건이 있는 문제
- bfs
    - 최단거리/경로
    - 가중치가 같을 때 최소비용/횟수