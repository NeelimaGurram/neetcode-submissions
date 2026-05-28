class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1) #length of window to check
        l=0  #pointers to window
        if k>len(s2):
            return False
        for r in range(k,len(s2)+1):
            permu_str=s2[l:r]
            if sorted(s1)==sorted(permu_str):
                return True
            l+=1
        return False


        