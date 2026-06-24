class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent = [i for i in range(n + 1)]
        def find(u):
            if u==parent[u]:
                return u
            parent[u]=find(parent[u])
            return parent[u]
        res=[]
        for u,v in edges:
            uroot=find(u)
            vroot=find(v)
            if uroot==vroot:
                return [u,v]
            parent[uroot]=vroot
        return []
        