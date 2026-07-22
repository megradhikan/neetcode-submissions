class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=[set() for _ in range(numCourses)]
        ind=[0]*numCourses
        isPre=[set() for _ in range(numCourses)]
        for a,b in prerequisites:
            ind[b]+=1
            adj[a].add(b)
        q=deque([i for i in range(numCourses) if ind[i]==0])
        while q:
            node=q.popleft()
            for nei in adj[node]:
                isPre[nei].add(node)
                isPre[nei].update(isPre[node])
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        return [u in isPre[v] for u, v in queries]

