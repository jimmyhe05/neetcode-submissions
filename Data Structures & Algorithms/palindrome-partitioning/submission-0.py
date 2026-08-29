class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int):
            if start == len(s):
                result.append(current.copy())

            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]

                if is_palindrome(piece):
                    current.append(piece)
                    backtrack(end)
                    current.pop()

        backtrack(0)

        return result

