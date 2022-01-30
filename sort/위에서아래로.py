# 수열을 내림차순으로 정렬하기
# input : 1번째 줄에 수열 내 숫자 개수 n이 주어짐 (1<=n<=500)
#         2번째 줄부터 n+1번째 줄까지 n개의 수가 입력됨. (자연수 / 1<=수<=100000)
# ouput : 주어진 수열이 내림차순 정렬된 결과를 공백으로 구분하여 출력

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

result = sorted(array, reverse=True)
print(' '.join(map(str, result)))