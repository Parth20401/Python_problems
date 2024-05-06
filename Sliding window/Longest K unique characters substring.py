class Solution:

    def longestKSubstr(self, s, k):
        mp = {}
        maxi = -1
        i, j = 0, 0
        
        while(j < len(s)):
            mp[s[j]] = mp.get(s[j], 0) + 1  # Increment the count of s[j] or add s[j] if not present
            
            if (len(mp) < k): #simply increase the ptr if true
                j += 1
            
            elif (len(mp) == k): #we have got k unique elements in our map if true
                maxi = max(maxi, j - i + 1)
                j += 1
                
            elif (len(mp) > k): # we have got more than k elements
                while (len(mp) > k):
                    mp[s[i]] -= 1
                    if(mp[s[i]] == 0): #if any entry becomes zero then delete it
                        del mp[s[i]]
                    i += 1
                
                j += 1
        
        return maxi
