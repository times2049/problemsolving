class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        MAX = max(nums) + 1
        nums = set(nums)
        ans = 0
        for x in range(1,MAX):
            if x in nums:
                ans += 1
                continue
            g = -1
            for y in range(2*x, MAX, x):
                if y in nums:
                    g = gcd(g, y) if g > 0 else y
                if g == x:
                    ans += 1
                    break
        return ans
