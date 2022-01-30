# 두 개의 배열 a와 b는 n개의 원소로 구성되며, 모두 자연수이다. 최대 k번의 바꿔치기 연산이 가능한데, 배열 a 원소와 배열 b 원소를 하나씩 서로 바꾸는 것을 의미한다.
# 최종목표는 배열 a의 모든 원소의 합이 최대가 되는 것이다. 이때, 최대로 만들 수 있는 배열 a의 원소 합을 출력하기

n = 5
k = 3
a = [1,2,5,5,3]
b = [5,5,6,6,5]

a_sort = sorted(a)
b_sort_r = sorted(b, reverse=True)

for i in range(k):
    if a_sort[i] < b_sort_r[i]:
        a_sort[i] = b_sort_r[i]
    else:
        break

print(sum(a_sort))