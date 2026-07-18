class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre={i: [] for i in range(numCourses)}
        for crs,p in prerequisites:
            pre[crs].append(p)
        visiting=set()
        def dfs(crs):
            if crs in visiting:
                return False
            if pre[crs]==[]:
                return True
            visiting.add(crs)
            for p in pre[crs]:
                if not dfs(p):
                    return False
            visiting.remove(crs)
            pre[crs]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
