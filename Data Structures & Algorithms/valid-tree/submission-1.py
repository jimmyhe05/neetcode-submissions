class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False # a tree with n nodes must have exactly n-1 edges

        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node: int, parent: int) -> None:
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                if neighbor not in visited:
                    dfs(neighbor, node)
            
        dfs(0, -1)
                

        return len(visited) == n