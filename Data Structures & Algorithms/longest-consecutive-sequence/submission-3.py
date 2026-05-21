from itertools import groupby
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni_elements=set(nums)
        sorted_nums=sorted(uni_elements)
        #diffs=[b-a for a,b in zip(sorted_nums[:-1],sorted_nums[1:])]
        #n=diffs.count(1)
        n=0  
        groups=[]
        for key,group in groupby(enumerate(sorted_nums), lambda x:x[1]-x[0]):
            group_list = [val for idx, val in group]
            groups.append(len(group_list))
        while n==0 :
            if groups==[]:
                break
            else:
                groups.sort()
                n=groups.pop()
                
       
        return n

        