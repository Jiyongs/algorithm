
# n 과 m (2)
# 1-n 사이의 자연수로 만든 길이가 m인 수열 # 전체 중복 비허용 # 구성 중복 비허용 # 같은 수 다중 사용 비허용
n, m = list(map(int, input().split()))

answer = []

def dfs(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(start, n+1):
        if i not in answer:
            answer.append(i)
            dfs(i+1)
            answer.pop()

dfs(1)