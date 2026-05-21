
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for x in nums:
            hashmap[x]=hashmap.get(x,0)+1
        sorted_nums=sorted(hashmap, key=hashmap.get,reverse=True)
        return sorted_nums[:k]
        

