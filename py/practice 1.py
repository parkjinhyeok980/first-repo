T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    p = [i for i in range(N+1)]

    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]
    
    def union(x, y):
        px = find_set(x)
        py = find_set(y)

        if px != py:
            p[py] = px

    for i in range(0, M*2, 2):
        a = arr[i]
        b = arr[i+1]
        union(a, b)

    groups = set()
    for i in range(N+1):
        groups.add(find_set(p[i]))
    
    print(f'#{tc} {len(groups)}')


