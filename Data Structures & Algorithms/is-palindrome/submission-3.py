class Solution:
    def isPalindrome(self, s: str) -> bool:
        """s1=str()
        for char in s:
            if char.isalnum():
                s1+=char.lower()
        return s1==s1[::-1]"""
        l=0
        r=len(s)-1
        while l<r:
            while l<r and (s[l].isalnum()!=1):
                l+=1
            while l<r and (s[r].isalnum()!=1):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True