# 실전문제 3. 전보
# 풀이 : 우선순위  이용한 다익스트라 알고리즘

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
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

# 도달할 수 있는 노드 개수(cnt), 최대 걸리는 시간(max_time) 을 출력하기
cnt = 0
max_time = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_time = max(max_time, d)
# 시작노드 제외하기 위해 cnt - 1 을 출력
print(cnt-1, max_time)