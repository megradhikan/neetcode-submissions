class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind=[0]*numCourses
        adj=[[] for i in range(numCourses)]
        for s,d in prerequisites:
            adj[s].append(d)
            ind[d]+=1
        q=deque()
        for i in range(numCourses):
            if ind[i]==0:
                q.append(i)
        finish=0
        output=[]
        while q:
            node=q.popleft()
            output.append(node)
            finish+=1
            for n in adj[node]:
                ind[n]-=1
                if ind[n]==0:
                    q.append(n)
        if finish!=numCourses:
            return []
        return output[::-1]