class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while n % p == 0: #find the mod to see divisibility by 2,3,5
                n //= p #keep dividing until we get 1
        
        return (n == 1)

#TC - O(log n)
