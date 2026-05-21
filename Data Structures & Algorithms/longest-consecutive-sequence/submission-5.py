from itertools import groupby
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """uni_elements=set(nums)
        sorted_nums=sorted(uni_elements)
        max_len=0
        for _,group in groupby(enumerate(sorted_nums), lambda x:x[1]-x[0]):
            group_len=len(list(group))
            max_len=max(max_len,group_len)
       
        return max_len"""
        num_set=set(nums)
        max_len=0
        for num in num_set:
            if num-1 not in num_set:
                length=1
                while num+length in num_set:
                    length+=1
                max_len=max(max_len, length)
        return max_len
        