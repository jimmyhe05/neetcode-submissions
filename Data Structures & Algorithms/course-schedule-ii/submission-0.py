class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visiting = set()
        visited = set()
        order = list()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False

            if course in visited:
                return True
            
            visiting.add(course)

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)
            order.append(course)

            return True


        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return order