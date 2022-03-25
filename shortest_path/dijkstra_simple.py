# 다익스트라 최단 경로 알고리즘
# 1. 출발 노드 설정하기
# 2. 최단 거리 테이블 초기화하기
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택하기
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신하기
# 5. 위 과정에서 3, 4번 반복하기

# 간단히 구현 -> 시간복잡도가 O(V^2)로, 노드 개수가 10000개 이상이면 아래 코드로는 어려움.
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())    # 노드 개수, 간선 개수
start = int(input())                # 시작노드 번호
graph = [[] for i in range(n+1)]    # 노드에 연결된 노드에 대한 정보 담을 리스트   : [[], [], ...]
visited = [False] * (n+1)           # 방문여부 체크용 리스트                  : [False, False, ...]
distance = [INF] * (n+1)            # 최단 거리 테이블                      : [10억, 10억, ...]

# 모든 간선 정보 입력받기
#      [
# 0번째   []
# 1번째   [(2, 2), (4, 1), (3,5)],
# n번째   ...
#      ]
for _ in range(m):
    a,b,c = map(int, input().split())
    #a->b 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 최단 거리가 가장 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 최단 거리가 가장 짧은 노드의 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라
def dijkstra(start):
    #시작 노드의 거리, 방문여부 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 실행
dijkstra(start)
# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    #도달할 수 없으면 무한으로 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있으면 거리 출력
    else:
        print(distance[i])