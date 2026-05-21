class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for x in strs:
            res+=str(len(x))+"#"+x
        return res

    def decode(self, s: str) -> List[str]:

         result = []
         i = 0

         while i < len(s):

            # Find #
             j = i

             while s[j] != "#":
                 j += 1

            # Length of string
             length = int(s[i:j])

            # Extract actual word
             word = s[j+1 : j+1+length]

             result.append(word)

            # Move pointer
             i = j + 1 + length

         return result
