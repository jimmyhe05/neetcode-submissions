class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None # store complete word

class Solution:   

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]

            node.is_end_of_word = True
            node.word = word

        rows, cols = len(board), len(board[0])
        result = set()

        def backtrack(r: int, c: int, node: TrieNode) -> None:
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "#" or board[r][c] not in node.children):
                return

            char = board[r][c]
            next_node = node.children[char]

            if next_node.is_end_of_word:
                result.add(next_node.word)

            board[r][c] = "#" # a temp replacement as in-used
            backtrack(r + 1, c, next_node)
            backtrack(r - 1, c, next_node)
            backtrack(r, c + 1, next_node)
            backtrack(r, c - 1, next_node)
            board[r][c] = char # undo, free the cell

        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root)

        return list(result)
