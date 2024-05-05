class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        ans = 0
        sum_val = 0
        i = 0

        while i < k and i < len(nums):
            mp[nums[i]] += 1 # storing first k elements in map
            sum_val += nums[i]
            i += 1

        # checking for duplicate elements
        if len(mp) == k:
            ans = sum_val  # storing sum of first window of k elements

        #now process further windows
        while i < len(nums):
            mp[nums[i]] += 1
            mp[nums[i - k]] -= 1 # removing the 1st key from previous iteration

            if mp[nums[i - k]] == 0:
                del mp[nums[i - k]]

            #now similarly do for sum
            sum_val += nums[i]
            sum_val -= nums[i - k]

            if len(mp) == k:
                ans = max(ans, sum_val)

            i += 1
            

        return ans
#Time Complexity (TC): O(N)
#Space Complexity (SC): O(k)
