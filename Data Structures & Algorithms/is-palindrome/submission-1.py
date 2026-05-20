class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        j = len(s) - 1
        for i in s:
            if i != s[j]:    
                return False
            j -= 1
        
        return True



