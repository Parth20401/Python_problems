class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = {}
        
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        
        
        n = n // 2
        for key, value in m.items():
            if value > n:
                return key
        
        return 0

#TC - O(N)
#SC - O(N)
