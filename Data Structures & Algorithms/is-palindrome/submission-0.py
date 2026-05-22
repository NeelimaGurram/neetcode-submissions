class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=str()
        for char in s:
            if char.isalnum():
                s1+=char.lower()
        return s1==s1[::-1]
        