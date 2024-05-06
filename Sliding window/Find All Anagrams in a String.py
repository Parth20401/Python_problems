class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        pCount, sCount = {}, {}#initialize to store freq of char of both strings

        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1

        res = [0] if pCount == sCount else [] #directly comparing both maps if they are equal (if true then insert idx 0 into ans otherwise empty list)
        left = 0
        for right in range (len(p), len(s)): #start from len(p) bcos we have already comapred all chars before that
            sCount[s[right]] = sCount.get(s[right], 0) + 1
            sCount[s[left]] -= 1 #remove the first char

            if sCount[s[left]] == 0:
                del sCount[s[left]]
            left += 1
            if sCount == pCount:
                res.append(left) #insert the left idx as ans

        return res
