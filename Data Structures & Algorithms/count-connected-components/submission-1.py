class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        visit=[False]*n
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei]=True
                    dfs(nei)
        count=0
        for i in range(n):
            if visit[i]==False:
                dfs(i)
                count+=1
        return count
