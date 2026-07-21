class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj=[[] for i in range(n)]
        for a,b in edges:
            adj[b].append(a)
            adj[a].append(b)
        visit=set()
        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            for i in adj[node]:
                if i==parent:
                    continue
                if not dfs(i,node):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n

        