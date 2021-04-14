import sys
import heapq

def dijkstra(point):
    dist = [sys.maxsize] * (V+1)
    dist[point] = 0
    heap = [(0, point)]

    while heap:
        cv, cp = heapq.heappop(heap)
        if cv < dist[cp]:
            continue

        for np, nv in link[cp]:
            value = cv + nv
            if value < dist[np]:
                heapq.heappush(heap, (value, np))
                dist[np] = value
    return dist

sys.stdin = open('input.txt')

input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())

link = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    link[u].append((v, w))

result = dijkstra(K)
for i in range(1, V+1):
    if result[i] == sys.maxsize:
        print('INF')
    else:
        print(result[i])