class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = [] # declaring answer list to store our answer

        i = 0
        while i < n:
            j = i # declare another pointer that will move

             # run that pointer until our range does not break
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1

            # if j > i, that means we got our range more than one element
            if j > i:
                ans.append(str(nums[i]) + "->" + str(nums[j])) # store the range

            else: # we got only one element as range
                ans.append(str(nums[i])) # store that element
            
            i = j + 1 # move i to j for a fresh start

        return ans
        
