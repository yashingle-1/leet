class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        from collections import defaultdict
        import heapq

        n = len(source)
        INF = float('inf')

        # Build graph
        graph = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            graph[o].append((c, w))

        # FREEZE KEYS (must be here)
        keys = list(graph.keys())

        # Cache Dijkstra results
        dist_cache = {}

        def dijkstra(start):
            if start in dist_cache:
                return dist_cache[start]

            dist = defaultdict(lambda: INF)
            dist[start] = 0
            pq = [(0, start)]

            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    if dist[v] > d + w:
                        dist[v] = d + w
                        heapq.heappush(pq, (dist[v], v))

            dist_cache[start] = dist
            return dist

        # DP: dp[i] = min cost to convert source[i:]
        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            for o in keys:
                if source.startswith(o, i):
                    dmap = dijkstra(o)
                    for c, w in dmap.items():
                        if target.startswith(c, i):
                            ni = i + len(c)
                            if ni <= n:
                                dp[i] = min(dp[i], w + dp[ni])

        return dp[0] if dp[0] != INF else -1
