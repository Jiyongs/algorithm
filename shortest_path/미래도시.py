# 실전문제 2. 미래도시

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)] # [[INF, INF, ...], [INF, INF, ...], ...]

# 자기 자신에게 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 초기화
for _ in range(m):
    a,b = map(int, input().split())
    #a->b 가는 비용이 1
    graph[a][b] = 1

# 가려는 목적지 입력
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
result = graph[1][x] + graph[x][k]
if result >= INF:
    print(-1)
else:
    print(result)