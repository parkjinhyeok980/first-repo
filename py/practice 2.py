from collections import deque

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    q = deque()
    q.append((N,0))
    visited[N] = 1
    
    while q:
        now_value, op_counts = q.popleft()

        if now_value == M:
            answer = op_counts
            break

        for next_value in (now_value+1, now_value-1, now_value*2, now_value-10):
            if next_value > 1000000 or next_value < 1:
                continue
            if visited[next_value]:
                continue
            
            visited[next_value] = 1

            q.append((next_value, op_counts+1))

    print(f"#{tc} {answer}")

