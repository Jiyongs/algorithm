# n명의 학생 정보가 있다. 정보는 이름과 성적으로 구분된다. 각 학생의 이름과 성적이 주어졌을 때, 성적이 낮은 순서로 학생 이름을 출력하기
# input : 1번째 줄에 학생의 수 n이 입력 (1<=n<=100000)
#         2번째 줄부터 n+1번째 줄에는 학생의 이름과 성적이 공백으로 구분되어 입력 (이름길이와 성적은 100이하의 자연수)
# ouput : 모든 학생의 이름을 성적이 낮은 순서로 출력

n = int(input())
array = []
for i in range(n):
    temp = input().split(' ')
    array.append((temp[0], int(temp[1])))

def getScore(data):
    return data[1]
result = sorted(array, key=getScore)
# 또는 람다로 할당
#result = sorted(array, key=lambda array: array[1])

print(' '.join(map(str, result)))