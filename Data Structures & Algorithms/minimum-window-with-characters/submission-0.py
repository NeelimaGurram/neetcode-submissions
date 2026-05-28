class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        
        tcount={}
        window={}
        for c in t:
            tcount[c]=tcount.get(c,0)+1

        have=0 # how many characters currently meet requirement        
        need=len(tcount) #how many distinct characters we need to match
        res=[-1,-1]
        reslen=float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            if c in tcount and window[c]==tcount[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                
                window[s[l]]-=1
                if s[l] in tcount and window[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("infinity") else ""
