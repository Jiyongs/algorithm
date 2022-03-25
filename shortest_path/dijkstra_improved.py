# 개선된 구현 -> 시간복잡도가 O(ElogV)
# 최단 거리가 가장 짧은 노드를 찾을 때 순차탐색이 아닌, heap 구조를 사용하자

# heap
# 우선순위 큐를 구현하기 위해 사용하는 자료구조
# 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제한다.
# python 에서는 PriorityQueue 또는 heapq를 제공하는데, heapq가 더 빠르다.
# heapq는 기본적으로 최소 힙 구조 (기준 값이 가장 낮은 데이터부터 삭제)를 이용한다.
# heapq를 최대 힙으로 사용하려면, 우선순위 기준 값에 음수(-) 값을 붙였다가, 값을 꺼내서 사용할 때 다시 음수(-) 값을 붙여서 사용하면 된다.

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단경로는 0으로 설정해서 큐에 삽입
    heapq.heappush(q, (0, start)) # q = [(0, 1)]
    distance[start] = 0
    #큐가 비어있지 않는 동안
    while q:
        #최단거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있다면 무시하기
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접 노드들을 확인하기
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 실행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    #도달할 수 없는 경우, 무한 값 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i])

