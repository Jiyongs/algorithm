# 플로이드 워셜 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 사용
# 시간복잡도는 O(N^3)
# 최단 거리를 2차원 리스트에 저장해야 한다.
# '바로 이동하는 거리'가 '특정 노드를 거쳐서 이동하는 거리'보다 더 많은 비용을 가진다면, 이를 더 짧은 것으로 갱신한다.

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
    a,b,c = map(int, input().split())
    #a->b 가는 비용이 c
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        #도달할 수 없으면, 무한 값 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        #도달할 수 있으면, 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()