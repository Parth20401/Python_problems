class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ele = None
        n = len(nums)

        for i in range(n):
            if cnt == 0:
                cnt = 1
                ele = nums[i]

            elif ele == nums[i]:
                cnt += 1
            
            else:
                cnt -= 1

        #now checking if the majority element is even occuring n/2 times
        #this part is used when there is not guarantee that majority eleent exists
        cnt_1 = 0

        for i in range(n):
            if ele == nums[i]:
                cnt_1 += 1

        if cnt_1 > (n / 2):
            return ele
        
        return -1
