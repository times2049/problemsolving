class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:

        q, r = divmod(primeFactors, 3)
        mod = 10 ** 9 +7
        
        if q == 0: return r
        
        if r == 2: return 2 * pow(3,q,mod) % mod
        if r == 1: return 4 * pow(3,q-1,mod) % mod
        if r == 0: return pow(3,q,mod)
