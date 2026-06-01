class Solution:
    def isValid(self, s: str) -> bool:
       mapping={
        ")":"(",
        "}":"{",
        "]":"["
       }
       res=[]
       for c in s:
        if c in mapping:
            if res and res[-1]==mapping[c]:
                res.pop()
            else:
                return False
        else:
            res.append(c)
        
       return True if not res else False

