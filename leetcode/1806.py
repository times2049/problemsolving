class Solution:
    def reinitializePermutation(self, n: int) -> int:
        list1 = list2 = list(range(n))
        list2 = [list2[0]] +list2[2::2]+ list2[1:-1:2] + [list2[-1]]
        res = 1
        while list1 != list2:
            res += 1
            list2 = [list2[0]] +list2[2::2]+ list2[1:-1:2] + [list2[-1]]
        return res
