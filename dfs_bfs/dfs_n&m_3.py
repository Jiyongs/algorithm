
# n 과 m (3)
# 1-n 사이의 자연수로 만든 길이가 m인 수열 # 전체 중복 비허용 # 구성 중복 허용 # 같은 수 다중사용 허용
n, m = list(map(int, input().split()))

answer = []

def dfs():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        answer.append(i)
        dfs()
        answer.pop()

dfs()