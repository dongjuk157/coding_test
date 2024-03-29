# import sys; input = sys.stdin.readline
INF = 987654321
def bf(start):
    global N, M, g, dist

    dist[start] = 0
    for i in range(N):
        for cur in range(1,N + 1):
            for next, cost in g[cur]:
                if dist[next] > dist[cur] + cost:
                    dist[next] = dist[cur] + cost
                    if i == N - 1:
                        return True
    return False


def main():
    global N, M, g, dist
    answer = []
    for tc in range(int(input())):
        N, M, W = map(int, input().split())
        g = [[] for _ in range(N + 1)]
        dist = [INF for _ in range(N + 1)]

        for _ in range(M):
            s, e, t = map(int, input().split())
            g[s].append([e, t])
            g[e].append([s, t])
        for _ in range(W):
            s, e, t = map(int, input().split())
            g[s].append([e, -t])

        cycle = bf(1)
        if cycle:
            answer.append("YES")
        else:
            answer.append("NO")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
