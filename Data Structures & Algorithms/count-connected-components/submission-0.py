class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit=set()
        def dfs(i):
            visit.add(i)
            for nei in adj[i]:
                    if nei not in visit:
                         dfs(nei)
        count=0
        for j in range(n):
            if j not in visit:
                dfs(j)
                count+=1
        return count