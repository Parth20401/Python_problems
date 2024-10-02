#this approach works only if array has only +ves and zeroes
class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        left, right = 0, 0
        Sum = arr[0]
        maxLen = 0
        
        while(right < n):
            
            while (left <= right and Sum > k): #if sum>k, then start removing elements from left side
                Sum =- arr[left]
                left += 1
            
            if Sum == k:
                maxLen = max(maxLen, right - left + 1)
            
            #increase right and then sum
            right += 1
            
            if right < n:
                Sum += arr[right]
            
            
        return maxLen

#TC - O(2N)
