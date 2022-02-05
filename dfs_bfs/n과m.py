# backtracking
# 길을 가다가 아닌 것 같으면 왔던 길로 되돌아가 다른 경로로 진행 # 재귀로 구현 # dfs기반

# n 과 m
# 1-n 사이의 자연수로 만든 길이가 m 수열 만들기

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = []

# n 과 m (1)
# 모든 경우의 수 # 같은 수 다중사용 안 함
def dfs_1():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            dfs_1()
            answer.pop()

# dfs_1()

# n 과 m (2)
# 구성이 겹치지 않는 모든 경우의 수 # 같은 수 다중사용 안 함
def dfs_2(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(start, n+1):
        if i not in answer:
            answer.append(i)
            dfs_2(i+1)
            answer.pop()

# dfs_2(1)

# n 과 m (3)
# 모든 경우의 수 # 같은 수 다중사용 가능
def dfs_3():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        answer.append(i)
        dfs_3()
        answer.pop()

# dfs_2()

# n 과 m (4)
# 모든 경우의 수 # 같은 수 다중사용 가능 # 비내림차순
def dfs_4(before):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        if before <= i:
            answer.append(i)
            dfs_4(i)
            answer.pop()

# dfs_4(1)

# n 과 m (5)
# 무작위로 주어진 n가지 자연수로 구성된 길이가 m인 수열  # 모든 경우의 수 # 같은 수 다중사용 안 함 # 오름차순
# 시간초과
def dfs_5_timeout():
    if(len(answer) == m):
        print(' '.join(map(str, answer)))
        return
    for i in range(1, max(numbers)+1):
        if i in numbers:
            if i not in answer:
                answer.append(i)
                dfs_5_timeout()
                answer.pop()

# dfs_5_timeout()

# 시간통과
numbers.sort()
visited = [False] * n
def dfs_5(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(numbers[i])
            dfs_5(depth+1, n, m)
            answer.pop()
            visited[i] = False

# dfs_5(0, n, m)

# n 과 m (6)
# 무작위로 주어진 n가지 자연수로 구성된 길이가 m인 수열  # 구성이 겹치지 않는 경우의 수 # 같은 수 다중사용 안 함 # 오름차순
numbers.sort()
visited = [False] * n
def dfs_6(depth, n, m, start):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            answer.append(numbers[i])
            dfs_6(depth+1, n, m, i+1)
            answer.pop()
            visited[i] = False

# dfs_6(0, n, m, 0)

# n 과 m (7)
# 무작위로 주어진 n가지 자연수로 구성된 길이가 m인 수열 # 모든 경우의 수 # 같은 수 다중사용 가능 # 오름차순
numbers.sort()
visited = [False] * n
def dfs_7(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        visited[i] = True
        answer.append(numbers[i])
        dfs_7(depth+1, n, m)
        answer.pop()
        visited[i] = False

# dfs_7(0, n, m)

# n 과 m (8)
# 무작위로 주어진 n가지 자연수로 구성된 길이가 m인 수열 # 모든 경우의 수 # 같은 수 다중사용 가능 # 비내림차순
numbers.sort()
visited = [False] * n
def dfs_8(depth, n, m, before):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        if before <= numbers[i]:
            visited[i] = True
            answer.append(numbers[i])
            dfs_8(depth+1, n, m, numbers[i])
            answer.pop()
            visited[i] = False

# dfs_8(0, n, m, numbers[0])

# n 과 m (9)
# 무작위로 주어진 n가지 자연수로 구성된 길이가 m인 수열 # 모든 경우의 수 # 같은 수 다중사용 안 함 # 오름차순 # 같은 자연수가 2개 이상 주어질 수 있음
numbers.sort()
visited = [False] * n
answer_list = []
# 시간초과
def dfs_9_timeout(depth, n, m):
    if depth == m:
        if str(answer) not in answer_list:
            answer_list.append(str(answer.copy()))
            print(' '.join(map(str, answer)))
        return
    for i in range(n):
        if visited[i] is not True:
            visited[i] = True
            answer.append(numbers[i])
            dfs_9_timeout(depth+1, n, m)
            answer.pop()
            visited[i] = False

# 시간통과
numbers.sort()
visited = [False] * n
def dfs_9(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    temp = 0
    for i in range(n):
        if visited[i] is not True and temp != numbers[i]:
            visited[i] = True
            answer.append(numbers[i])
            temp = numbers[i]
            dfs_9(depth+1, n, m)
            answer.pop()
            visited[i] = False

# dfs_9(0, n, m)