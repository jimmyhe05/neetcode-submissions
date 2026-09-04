class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visiting = set() # courses on the dfs path
        visited = set() # courses confirmed safe relationship

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for preq in adj[course]:
                if not dfs(preq):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True


        for course in range(numCourses):
            if not dfs(course):
                return False

        return True



        

        



        