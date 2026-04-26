import heapq

T = int(input())
for tc in range(1, 1+T):
    N, E = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())

        graph[s].append((e, w))

    dist = [float("inf")] * (N+1)
    dist[0] = 0

    pq = []

    heapq.heappush(pq, (0,0))

    while pq:
        now_dist, now_node = heapq.heappop(pq)

        if dist[now_node] < now_dist:
            continue

        for next_node, weight in graph[now_node]:
            if dist[next_node] > now_dist + weight:
                dist[next_node] = now_dist + weight
                heapq.heappush(pq,(dist[next_node], next_node))

    print(f'#{tc} {dist[N]}')
