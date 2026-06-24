class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        adj_list = {i: [] for i in range(numCourses)}

        for dest, src in prerequisites:
            # 'src' is the prerequisite (b), 'dest' is the course (a)
            adj_list[src].append(dest)
            in_degree[dest] += 1
        queue = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        count=0
        results=[]
        while queue:
            el=queue.popleft()
            results.append(el)
            count+=1
            for i in adj_list[el]:
                in_degree[i]-=1
                if in_degree[i]==0:
                    queue.append(i)
        if count==numCourses:
            return results
        return []