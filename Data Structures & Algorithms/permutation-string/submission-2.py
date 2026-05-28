from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1) #length of window to check
        l=0  #pointers to window
        if k>len(s2):
            return False
        s1_count=Counter(s1)
        for r in range(k,len(s2)+1):
            permu_str=s2[l:r]
            if Counter(s1)==Counter(permu_str):
                return True
            l+=1
        return False


        