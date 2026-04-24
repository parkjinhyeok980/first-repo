# 최소 비용
from heapq import heappush, heappop

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    q = []
    heappush(q,(0,0,0))
    fuel[0][0] = 0

    while q:
        w, r, c = heappop(q)

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                height_diff = 0
                if arr[nr][nc] > arr[r][c]:
                    height_diff = arr[nr][nc] - arr[r][c]

                    cost = fuel[r][c] + height_diff + 1
                    if cost < fuel[nr][nc]:
                        fuel[nr][nc] = cost
                        heappush(q, (cost, nr, nc))
INF = 100000001

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fuel =[[INF]*N for _ in range(N)]
    fuel[0][0] = 0
    dijkstra()

    print(f'#{tc} {fuel[N-1][N-1]}')

