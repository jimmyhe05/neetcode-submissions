class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_len = len(s)
        # mid = s_len // 2
        # result = ''.join(c.lower() for c in s if c.isalpha())
        # print(result)

        # # odd length
        # if s_len % 2 == 1:
        #     return result[:mid] == result[mid+1:]
        # else:
        #     return result[:mid] == result[mid:]
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

