class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        preSumMap = {}
        Sum = 0
        maxLen = 0
        
        for i in range(n):
            Sum += arr[i]
            
            if Sum == k:
                maxLen = max(maxLen, i + 1)
                
            #calculate remaining sum
            rem = Sum - k
            
            if rem in preSumMap:
                length = i - preSumMap[rem] #the index of the preSum element alread stored
                maxLen = max(maxLen, length)
                
            # Finally, update the map checking the conditions:
            if Sum not in preSumMap:
                preSumMap[Sum] = i
                
        return maxLen

  #TC - O(N)
  #SC - O(N)
