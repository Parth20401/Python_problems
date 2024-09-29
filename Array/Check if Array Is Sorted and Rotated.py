class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0

        for i in range(1, n):
            if nums[i - 1] > nums[i]: #this cond. for checking that if array is breaking the ascending order (hence it is sorted & rotated)
                cnt += 1
            
        if nums[n - 1] > nums[0]: # this for checking if array is not breaking but sorted (thus rotations = 0)
            cnt += 1
        
        return cnt <= 1
