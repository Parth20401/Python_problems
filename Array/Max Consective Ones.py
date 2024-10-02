class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = ans = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != 1:
                cnt = 0
            else:
                cnt += 1

            ans = max(ans, cnt)
            
        return ans
