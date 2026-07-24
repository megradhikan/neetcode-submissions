class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)+1
        ind=[0]*n
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            ind[u]+=1
            ind[v]+=1
        q=deque()
        for i in range(n):
            if ind[i]==1:
                q.append(i)
        while q:
            node=q.popleft()
            ind[node]-=1
            for i in adj[node]:
                ind[i]-=1
                if ind[i]==1:
                    q.append(i)
        for u,v in reversed(edges):
            if ind[u]==2 and ind[v]:
                return [u,v]
        return []
        