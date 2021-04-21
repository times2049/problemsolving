class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        mx = 0
        i = 0
        for n2 in nums2:
            a = abs(nums1[i]-n2)
            res += a
            i += 1
            for n1 in nums1:
                if mx - a >= 0:
                    break
                d = a - abs(n1-n2)
                if d - mx > 0:
                    mx = d

        return (res - mx) % (10**9 + 7)
