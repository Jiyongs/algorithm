# Algorithm (in python)

## hash
``` python
if 값 in 리스트
```
- return 리스트 안의 값 존재 여부

``` python
zip(리스트1, 리스트2)
```
- return object( 리스트1[0], 리스트2[0] )
- object를 list, dict, tuple, set 등 으로 변환하여 사용

``` python
dict(zip(리스트1, 리스트2))
```
- return { 리스트1[0] : 리스트2[0] }

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
