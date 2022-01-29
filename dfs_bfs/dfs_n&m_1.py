# backtracking
# 길을 가다가 아닌 것 같으면 왔던 길로 되돌아가 다른 경로로 진행 # 재귀로 구현 # dfs기반

# n 과 m (1)
# 1-n 사이의 자연수로 만든 길이가 m 수열 # 전체 중복 비허용 # 구성 중복 허용 # 같은 수 다중사용 비허용
n, m = list(map(int, input().split()))

answer = []

def dfs():
    if len(answer) == m:
        print(' '.join(map(str,answer)))
        return
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            dfs()
            answer.pop()

dfs()