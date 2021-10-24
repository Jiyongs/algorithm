# Algorithm 
####(in python)

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
```
dict(zip(리스트1, 리스트2))
```
- return { 리스트1[0] : 리스트2[0] }

```
sorted(딕셔너리.items(), key=(lambda x: x[0]), reverse=True)
```
- 딕셔너리의 key 값으로 내림차순하여 정렬 후 [(키, 값)] 형태로 반환
- 딕셔너리의 value 값으로 정렬하려면, key=(lambda x: x[1]) 로 변경

```
변수 = 값1 if 조건문 else 값2
```
- 조건문이 true면 값1 false면 값2 를 변수에 대입

```
from collections import Counter
Counter(리스트)
```
- return Counter({값1:건수, 값2:건수, ...})
- 리스트 값들의 고유 값(set(리스트)) 별 건수를 반환