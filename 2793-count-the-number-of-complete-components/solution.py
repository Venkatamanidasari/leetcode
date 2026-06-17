from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        result = 0
        
        def dfs(node, nodes, edges_count):
            visited[node] = True
            nodes.append(node)
            for nei in graph[node]:
                edges_count[0] += 1   # count edge
                if not visited[nei]:
                    dfs(nei, nodes, edges_count)
        
        for i in range(n):
            if not visited[i]:
                nodes = []
                edges_count = [0]
                dfs(i, nodes, edges_count)
                
                v = len(nodes)
                e = edges_count[0] // 2   # each edge counted twice
                if e == v * (v - 1) // 2:
                    result += 1
        
        return result
