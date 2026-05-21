import math       #math.prod()
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        n=len(nums)
        for i in range(n):
            nums1=nums[:i]+nums[i+1:]
            output.append(math.prod(nums1))
        return output