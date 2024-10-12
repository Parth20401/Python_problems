class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        #Code here
        maxi = 0
        ans = []
        
        #do reverse iteration
        for i in range(n - 1, -1, -1):
            if arr[i] >= maxi:
                ans.append(arr[i])
                
            maxi = max(maxi, arr[i])
        
        ans.sort(reverse = True)
            
        return ans
