# 이것이 취업을 위한 코딩 테스트다 with 파이썬 (p.150)
# 실전문제 음료수 얼려 먹기 > dfs

# n, m = map(int, input().split())
n, m = 5, 6

graph = [
    [1, 0, 1, 0, 1, 0], 
    [1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 1, 1, 1], 
    [1, 1, 1, 1, 0, 0]
    ]

#graph = []
#for i in range(n):
#    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y+1) # 상
        dfs(x, y-1) # 하
        dfs(x-1, y) # 좌
        dfs(x+1, y) # 우
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)