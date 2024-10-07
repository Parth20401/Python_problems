class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0] * n

        posIndex, negIndex = 0, 1 # # positive elements start from 0 and negative from 1.

        for i in range (n):
            
            # Fill negative elements in odd indices and inc by 2.
            if nums[i] < 0:
                ans[negIndex] = nums[i]
                negIndex += 2 #next possible negative no. will be after 2 places
            else:
            # Fill positive elements in even indices and inc by 2
                ans[posIndex] = nums[i]
                posIndex += 2
            
        return ans

#TC - O(N)-> one pass solution instead of taking two seperate lists
#SC - O(N)
