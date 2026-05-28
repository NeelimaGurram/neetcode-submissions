class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = set()
        freq = dict()
        currentMax = float('-inf')
        for i in range(k):
            window.add(nums[i])
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            currentMax = max(currentMax, nums[i])
        
        result = [currentMax]
        for right in range(k, len(nums)):
            currentMax = max(currentMax, nums[right])
            freq[nums[right-k]] -= 1
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            window.add(nums[right])
            if freq[nums[right-k]] == 0:
                window.remove(nums[right-k])
                if nums[right-k] == currentMax:
                    currentMax = max(window)
            result.append(currentMax)
        
        return result