# 최소 이동 거리
from collections import deque

T = int(input())
for tc in range(1, 1+T):
    N, E = map(int,input().split())
    matrix = [[0] for _ in range(N+1)]
    visited = [float("inf")]*(N+1)

    for _ in range(E):
        i,j,val=map(int,input().split())
        matrix[i][j] = val

        q = deque()

        for j in range(N+1):
            if matrix[0][j] > 0:
                q.append((j, matrix[0][j]))
                visited[j] = matrix[0][j]

        while q:
            idx, cost = q.popleft()

            if cost > visited[N]:
                continue

            for j in range(N+1):
                if matrix[idx][j] != 0 and visited[j] > cost + matrix[idx][j]:
                    q.append((j,cost+matrix[idx][j]))
                    visited[j] = cost + matrix[idx][j]
        
        print(f'#{tc} {visited[N]}')