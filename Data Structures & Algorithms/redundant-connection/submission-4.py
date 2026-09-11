class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # using union find
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            
            return node

        def union(a: int, b: int) -> bool:
            root_a, root_b = find(a), find(b)

            if root_a == root_b:
                return False # already connected, redundant

            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            rank[root_a] += rank[root_b]

            return True
        

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []