class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        for i in range(len(s)):
            charset=set()
            for j in range(i,len(s)):
                if s[j] in charset:
                    break
                charset.add(s[j])
            max_len=max(max_len,len(charset))
        return max_len

        